from bs4 import BeautifulSoup
import requests
import time

class WebPageListing:

    def __init__(self, title, listing_url):
        self.title = title
        self.listing_url = f"https://marktplaats.nl{listing_url}"

class WebPage:

    def __init__(self, web_page_url, crud):
        self._web_page_url = web_page_url
        self.crud = crud

    def get_listings(self):
        response_html = self._get_html_from_url(self._web_page_url)
        soup = BeautifulSoup(response_html, "html.parser")
        web_page_listings = soup.find_all(class_ = "mp-Listing mp-Listing--list-item")
        
        web_page_listing_objects = []
        for web_page_listing in web_page_listings:
            web_page_listing_object = self._get_web_page_listing_object(web_page_listing)
            web_page_listing_objects.append(web_page_listing_object)
        return web_page_listing_objects
        
    def _get_web_page_listing_object(self, web_page_listing):
        listing_url=web_page_listing.find("a", href=True)["href"]
        title = web_page_listing.find("h3").getText()
        web_page_listing_object = WebPageListing(title=title, listing_url=listing_url)
        return web_page_listing_object



    def _get_html_from_url(self, url):
        for i in range(0, 2):
            response = self.crud.get_data(url)
            if response.status_code == 200:
                break
            time.sleep(i)
        else:
            response = self.crud.change_ip()
            if response.status_code != 200: 
                raise ConnectionRefusedError("Could not connect with Privoxy/Tor")

        response = self.crud.get_data(url)
        if response.status_code != 200: 
                raise ConnectionRefusedError("Could not connect with Marktplaats")
        return response.text

        
                
                



            
