from app.schemas import CarListingCreate
from app.repositories.car_listing_repository import CarListingRepository
from app.models import CarListing
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