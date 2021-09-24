from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.car_listing import Base, CarListingBase
from app.models.advertiser import AdvertiserBase

class CarListing(CarListingBase):
    advertiser_name = Column(String, ForeignKey("advertisers.name"))

class Advertiser(AdvertiserBase):
    pass