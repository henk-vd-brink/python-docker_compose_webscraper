from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.models.car_listing import Base, CarListingBase
from app.models.advertiser import AdvertiserBase

class CarListing(CarListingBase):
    advertiser_id = Column(Integer, ForeignKey("advertisers.id"))

class Advertiser(AdvertiserBase):
    pass