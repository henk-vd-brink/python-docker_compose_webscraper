from typing import Type
from .abc_listing import ListingBaseClass
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class CarListingAdvertiser(ListingBaseClass):

    __postendpoint__ = "/advertisers"
    __webpageurl__ = "https://www.marktplaats.nl/v/"

    name: str = "_"
    activity: str = "_"
    rating: str = "_"

    advertiser_url: str = ""

    def __init__(self, web_page_listing, crud, *args, **kwargs):
        super().__init__(web_page_listing, crud, *args, **kwargs)

    def get_attributes(self):
        response_html = self.crud.get_html(self._listing_url)
        soup = BeautifulSoup(response_html, "html.parser")

        self._set_advertiser_url(soup)
        if self.advertiser_url:
            response_html_advertiser = self.crud.get_html(self.advertiser_url)
            soup_advertiser = BeautifulSoup(response_html_advertiser, "html.parser")

            self._set_advertiser_name_activity_rating(soup_advertiser)
        else:
            self._set_advertiser_name_activity_rating(None)

    def _set_advertiser_url(self, page_soup):
        top_info = page_soup.find("div", class_ = "top-info")
        try:
            self.advertiser_url = top_info.find("a", href=True)["href"]
        except AttributeError:
            self.advertiser_url = None
        
    def _set_advertiser_name_activity_rating(self, page_soup):
        if not self.advertiser_url: 
            return

        try:
            self.name = page_soup.find("div", class_ = "mp-TopSection-TitleWrap-Name").string
        except Exception:
            pass

        try:
            activity_block = page_soup.find_all("div", class_ = "mp-SellerHeaderInfo-item")
            self.activity = activity_block[1].string if activity_block[1].string else "_"
            self.rating = activity_block[0].string if activity_block[0].string else "_"
        except Exception:
            pass

    @property
    def __repr__(self):
        return {"name": self.name,
                "activity": self.activity,
                "rating": self.rating}

    def __str__(self):
        return str(self.__repr__)