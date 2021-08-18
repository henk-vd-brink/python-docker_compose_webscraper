from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class CarListing(Base):

    __tablename__ = "car_listings"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer, unique=True, index=True)