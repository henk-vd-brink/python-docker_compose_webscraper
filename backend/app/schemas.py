from typing import List, Optional
from pydantic import BaseModel


class CarListingBase(BaseModel):
    price: int
    title: str
    brand_model: str
    mileage: int
    fuel_type: str
    year_of_construction: int
    advertiser_name: str
    category: str

class CarListing(CarListingBase):
    id: int

    class Config:
        orm_mode = True

class CarListingCreate(CarListingBase):
    pass


class AdvertiserBase(BaseModel):
    name: str
    activity: str
    rating: str
    

class Advertiser(AdvertiserBase):

    class Config:
        orm_mode = True

class AdvertiserCreate(AdvertiserBase):
    pass