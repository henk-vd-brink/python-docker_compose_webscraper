from abc import ABCMeta, abstractmethod

class ListingBaseClass(metaclass=ABCMeta):

    def __init__(self, web_page_listing, crud, *args, **kwargs):
        self._listing_url = web_page_listing.listing_url
        self._title = web_page_listing.title
        self.crud = crud

    @abstractmethod
    def get_attributes(self):
        pass

    def post_data(self):
        url = "test"+self.__postendpoint__
        self.crud.post_data(url=url, payload=self.__repr__)

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def __repr__(self):
        pass
    
