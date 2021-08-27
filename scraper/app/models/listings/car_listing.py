from .abc_listing import ListingBaseClass
from dataclasses import dataclass
import time
import requests
from bs4 import BeautifulSoup

class CarListing(ListingBaseClass):

    __postendpoint__ = "/car_listings"
    __webpageurl__ = "https://www.marktplaats.nl/l/auto-s/"
    
    _title: str = ""

    price: int = 0
    brand: str = ""
    model: str = ""
    mileage: int = 0
    fuel_type: str = ""
    year_of_construction: int = 0

    _attribute_dict= {  "Prijs": "price", 
                        "Merk": "brand",
                        "Model": "model", 
                        "Brandstof": "fuel_type",
                        "Kilometerstand": "mileage",
                        "Bouwjaar": "year_of_construction",
                        "Titel": "title"} 

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

    def _get_html_from_url(self, url):
        for i in range(0, 2):
            response = requests.get(url)
            if response.status_code == 200:
                break
            time.sleep(i)
        else:
            raise ConnectionRefusedError(f"Could not get web page {url} \n {response.text}")
        return response.text

    def get_attributes(self):
        response_html = self._get_html_from_url(self._listing_url)
        soup = BeautifulSoup(response_html, "html.parser")

        self._get_information_table(soup)

        output_json = {}
        for key, value in self._attribute_dict.items():
            output_json[value] = getattr(self, value)

        return output_json

    def _get_information_table(self, soup):
        information_table_elements = self._get_information_table_elements(soup)
        for information_table_element in information_table_elements:
            key = information_table_element.find("span", class_ = "key").getText()
            value = information_table_element.find("span", class_ = "value").getText()
    
            formatted_key = key.replace(":", "")
            if formatted_key in self._attribute_dict:
                if isinstance(getattr(self, self._attribute_dict[formatted_key]), int):
                    value = self._format_value(value)
                
                setattr(self, self._attribute_dict[formatted_key], value)
            
    def _format_value(self, value):
        formatted_value = value.replace(" ", "").replace("€", "").replace(".","")
        if "," in formatted_value:
            index = formatted_value.find(formatted_value)
            formatted_value = formatted_value[0:index]
        return formatted_value

    def _get_information_table_elements(self, page_soup):
        information_table_elements = page_soup.find_all("div", class_ = "spec-table-item")
        return information_table_elements
 
    @property
    def __repr__(self):
        repr_json = {}
        for key, value in self._attribute_dict.items():
            repr_json[value] = getattr(self, value)
        return repr_json

    def __str__(self):
        return str(self.__repr__())

    