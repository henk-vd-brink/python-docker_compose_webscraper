
from models import CarListing, WebPage, WebPageListing, CarListingAdvertiser
from bs4 import BeautifulSoup

from src.crud import Crud, MockCrud
from src.sleep import Sleep
from src.page import Page

crud = Crud()

listing_object = CarListing
advertiser_object = CarListingAdvertiser
page = Page(initial_page_number=50, base_url=listing_object.__webpageurl__)

def run():
    for _ in range(0, 1000):
        web_page_url = page.__next__
        web_page_listings = WebPage(web_page_url=web_page_url, crud=crud).get_listings()

        for web_page_listing in web_page_listings:
            Sleep.random_sleep(max_value=0.1)
            parsed_advertiser = CarListingAdvertiser(web_page_listing=web_page_listing, crud=crud)
            parsed_listing_object = listing_object(web_page_listing=web_page_listing, crud=crud)

            parsed_listing_object.advertiser_name = parsed_advertiser.name


            parsed_advertiser.post_data()
            parsed_listing_object.post_data()

    
        
        
        


        
        


