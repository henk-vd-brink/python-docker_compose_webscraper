from abc import ABCMeta, abstractmethod

class ListingBaseClass(metaclass=ABCMeta):

    @abstractmethod
    def get_attributes(self):
        pass