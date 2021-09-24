from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base


class CarListingBase(Base):

    __tablename__ = "car_listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    price = Column(Integer)
    brand_model = Column(String)
    mileage = Column(Integer)
    fuel_type = Column(String)
    year_of_construction = Column(Integer)
    category = Column(String)
