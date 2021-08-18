from typing import List, Optional
from pydantic import BaseModel


class CarListingBase(BaseModel):
    price: int

class CarListing(CarListingBase):
    id: int

    class Config:
        orm_mode = True

class CarListingCreate(CarListingBase):
    pass