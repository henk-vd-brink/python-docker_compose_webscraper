from abc import ABCMeta, abstractmethod
import json


class ListingBaseClass(metaclass=ABCMeta):

    @classmethod
    def __init_subclass__(cls):
        required_class_variables = ["__webpageurl__",  "__postendpoint__"]
        for required_class_variable in required_class_variables:
            if not hasattr(cls, required_class_variable):
                raise NotImplementedError(f"Class lacks required attribute {required_class_variable}")

    def __init__(self, web_page_listing, crud, *args, **kwargs):
        self._listing_url = web_page_listing.listing_url
        self._title = web_page_listing.title
        self.crud = crud

        self.get_attributes()

    @abstractmethod
    def get_attributes(self):
        ...

    def post_data(self):
        url = "http://localhost:5000"+self.__postendpoint__
        self.crud.post_data(url=url, payload=self.__repr__)

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def __repr__(self):
        pass
    
