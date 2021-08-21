from app.schemas import CarListingCreate, AdvertiserCreate
from app.repositories import CarListingRepository, AdvertiserRepository
from app.models import CarListing, Advertiser
from typing import Iterator

class CarListingService:
    def __init__(self, car_listing_repository: CarListingRepository):
        self._repository = car_listing_repository

    def get_car_listings(self, skip, limit):
        return self._repository.get_car_listings(skip=skip, limit=limit)

    def create_car_listing(self, object_in):
        return self._repository.create_car_listing(object_in)

    def get_car_listing_by_id(self, car_listing_id):
        return self._repository.get_car_listing_by_id(car_listing_id)

    def get_car_listing_by_title(self, car_listing_title):
        return self._repository.get_car_listing_by_title(car_listing_title)


class AdvertiserService:
    def __init__(self, advertiser_repository: AdvertiserRepository):
        self._repository = advertiser_repository

    def get_advertisers(self, skip, limit):
        return self._repository.get_advertisers(skip=skip, limit=limit)

    def create_advertiser(self, object_in):
        return self._repository.create_advertiser(object_in)

    def get_advertiser_by_id(self, advertiser_id):
        return self._repository.get_advertiser_by_id(advertiser_id)

    def get_advertiser_by_name(self, advertiser_name):
        return self._repository.get_advertiser_by_name(advertiser_name)