from typing import List

from fastapi import APIRouter, Depends, HTTPException

from . import schemas

from dependency_injector.wiring import inject, Provide
from app.container import Application
from app.service import CarListingService

router = APIRouter()

@router.get("/car_listings", response_model=List[schemas.CarListing])
@inject
def read_car_listings(
    skip: int = 0,
    limit: int = 100,
    car_listing_service: CarListingService = Depends(Provide[Application.car_listing.car_listing_service]),
):
    car_listings = car_listing_service.get_car_listings(skip=skip, limit=limit)
    return car_listings

@router.get("/car_listings/{car_listing_id}", response_model=schemas.CarListing)
@inject
def read_car_listing(
    car_listing_id: int,
    car_listing_service: CarListingService = Depends(Provide[Application.car_listing.car_listing_service]),
):
    db_car_listing = car_listing_service.get_car_listing_by_id(car_listing_id)
    if db_car_listing is None:
        raise HTTPException(status_code=404, detail="Car listing not found")
    return db_car_listing

@router.post("/car_listings", response_model=schemas.CarListing)
@inject
def create_car_listing(
    car_listing: schemas.CarListingCreate,
    car_listing_service: CarListingService = Depends(Provide[Application.car_listing.car_listing_service])
):
    db_car_listing=car_listing_service.get_car_listing_by_id(car_listing.price)
    if db_car_listing:
        raise HTTPException(status_code=400, detail="price already registered")
    return car_listing_service.create_car_listing(car_listing)