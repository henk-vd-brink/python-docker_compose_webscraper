from .abc_listing import ListingBaseClass
from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class CarListing(ListingBaseClass):

    __postendpoint__ = "/car_listings"
    __webpageurl__ = "https://www.marktplaats.nl/l/auto-s/"
    
    _title: str = ""

    price: int = 0
    brand_model: str = ""
    mileage: int = 0
    fuel_type: str = ""
    year_of_construction: int = 0
    advertiser_name: str = ""
    category: str = ""

    _attribute_map_table = {    "Prijs": {"key": "price" , "type": "int"}, 
                                "Merk & Model": {"key": "brand_model", "type": "str"},
                                "Brandstof": {"key": "fuel_type", "type": "str"},
                                "Kilometerstand": {"key": "mileage", "type": "int"},
                                "Bouwjaar" : {"key": "year_of_construction", "type": "int"}  }

    _attribute_map = {  **_attribute_map_table,
                        "title": {"key": "titel", "type": "str"},
                        "advertiser_name": {"key": "advertiser_name", "type": int}  }
                        

    def __init__(self, web_page_listing, crud, *args, **kwargs):
        super().__init__(web_page_listing, crud, *args, **kwargs)

    @property
    def listing_url(self):
        return self._listing_url

    @listing_url.setter
    def listing_url(self, listing_url):
        self._listing_url = listing_url

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def _table_keys(self):
        return [value["key"] for key, value in self._attribute_map_table.items()]

    def get_attributes(self):
        response_html = self.crud.get_html(self._listing_url)
        soup = BeautifulSoup(response_html, "html.parser")

        # self._set_advertiser_name(soup)
        self._set_information_table(soup)

        output_json = {}
        
        for table_key in self._table_keys:
            output_json[table_key] = getattr(self, table_key)
        return output_json

    # def _set_advertiser_name(self, page_soup):
    #     try:
    #         self.advertiser_name = page_soup.find("h2", class_ = "name mp-text-header3")["title"]
    #     except TypeError:
    #         self.advertiser_name = "_"
        
    def _set_information_table(self, soup):
        information_table_elements = self._get_information_table_elements(soup)
        for information_table_element in information_table_elements:
            key = information_table_element.find("span", class_ = "key").getText()
            value = information_table_element.find("span", class_ = "value").getText()    
            formatted_key = key.replace(":", "")
            if formatted_key in (table_attributes:=self._attribute_map_table):
                attribute_key = table_attributes[formatted_key]["key"]
                attribute_type = table_attributes[formatted_key]["type"]

                if attribute_type == "int": value = self._format_value(value)
                setattr(self, attribute_key, value)
            
    def _format_value(self, value):
        formatted_value = value.replace(" ", "").replace("€", "").replace(".","").replace("km", "")
        if (comma:=",") in formatted_value:
            index = formatted_value.find(comma)
            formatted_value = formatted_value[0:index]
        try:
            return int(formatted_value)
        except ValueError:
            return 0

    def _get_information_table_elements(self, page_soup):
        information_table_elements = page_soup.find_all("div", class_ = "spec-table-item")
        return information_table_elements

    def _get_category(self):
        return self.__webpageurl__.split("/")[-2]

    @property
    def __repr__(self):
        repr_json = {}
        for table_key in self._table_keys:
            repr_json[table_key] = getattr(self, table_key)
        repr_json["category"] = self._get_category()
        repr_json["title"] = self._title
        repr_json["advertiser_name"] = self.advertiser_name
        return repr_json

    def __str__(self):
        return str(self.__repr__)

    