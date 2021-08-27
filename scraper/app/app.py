from models import CarListing, WebPage, WebPageListing
from bs4 import BeautifulSoup

from src.crud import Crud, MockCrud
from src.sleep import Sleep
from src.page import Page

crud = MockCrud()
listing_object = CarListing
page = Page(initial_page_number=2, base_url=listing_object.__webpageurl__)

def run():
    web_page_url = page.__next__
    web_page_listings = WebPage(web_page_url=web_page_url).get_listings()

    for web_page_listing in web_page_listings[20:22]:
        Sleep.random_sleep()
        parsed_listing_object = listing_object(web_page_listing=web_page_listing, crud=crud)
        parsed_listing_object.post_data()

        
        
        


        
        


