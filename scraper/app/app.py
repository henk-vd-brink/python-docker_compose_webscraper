from models import CarListing, WebPage, WebPageListing
from bs4 import BeautifulSoup

def run():

    web_page_url = "https://www.marktplaats.nl/q/auto/"
    web_page_listings = WebPage(web_page_url=web_page_url).get_listings()

    for web_page_listing in web_page_listings[0:1]:
        listing_object = CarListing(web_page_listing=web_page_listing)
        
        


        
        


