from typing import List
from fastapi import APIRouter, Depends, HTTPException

from . import schemas

from dependency_injector.wiring import inject, Provide
from app.container import Application
from app.service import CarListingService, AdvertiserService
from app.tor_controller import TorController

router = APIRouter()
proxies = {"http": "http://privoxy:8118", "https": "https://privoxy:8118"}

@router.get("/car_listings", response_model=List[schemas.CarListing], tags=["car_listings"])
@inject
def read_car_listings(
    skip: int = 0,
    limit: int = 100,
    car_listing_service: CarListingService = Depends(Provide[Application.car_listing.car_listing_service]),
):
    car_listings = car_listing_service.get_car_listings(skip=skip, limit=limit)
    return car_listings

@router.get("/car_listings/{car_listing_id}", response_model=schemas.CarListing, tags=["car_listings"])
@inject
def read_car_listing(
    car_listing_id: int,
    car_listing_service: CarListingService = Depends(Provide[Application.car_listing.car_listing_service]),
):
    db_car_listing = car_listing_service.get_car_listing_by_id(car_listing_id)
    if db_car_listing is None:
        raise HTTPException(status_code=404, detail="Car listing not found")
    return db_car_listing

@router.post("/car_listings", response_model=schemas.CarListing, tags=["car_listings"])
@inject
def create_car_listing(
    car_listing: schemas.CarListingCreate,
    car_listing_service: CarListingService = Depends(Provide[Application.car_listing.car_listing_service])
):
    print(car_listing)
    db_car_listing=car_listing_service.get_car_listing_by_title(car_listing.title)

    if db_car_listing:
        raise HTTPException(status_code=400, detail="Title already registered")
    return car_listing_service.create_car_listing(car_listing)

@router.get("/advertisers", response_model=List[schemas.Advertiser], tags=["advertisers"])
@inject
def read_advertisers(
    skip: int = 0,
    limit: int = 100,
    advertiser_service: AdvertiserService = Depends(Provide[Application.advertiser.advertiser_service]),
):
    advertisers = advertiser_service.get_advertisers(skip=skip, limit=limit)
    return advertisers

@router.get("/advertisers/{advertiser_name}", response_model=schemas.Advertiser, tags=["advertisers"])
@inject
def read_advertiser(
    advertiser_name: str,
    advertiser_service: AdvertiserService = Depends(Provide[Application.advertiser.advertiser_service]),
):
    db_advertiser = advertiser_service.get_advertiser_by_name(advertiser_name)
    
    if db_advertiser is None:
        raise HTTPException(status_code=404, detail="Advertiser not found")
    return db_advertiser

@router.post("/advertisers", response_model=schemas.Advertiser, tags=["advertisers"])
@inject
def create_advertiser(
    advertiser: schemas.AdvertiserCreate,
    advertiser_service: AdvertiserService = Depends(Provide[Application.advertiser.advertiser_service])
):

    db_advertiser = advertiser_service.get_advertiser_by_name(advertiser.name)

    if db_advertiser:
        raise HTTPException(status_code=400, detail=f"Advertiser '{advertiser.name}' is already registered.")
    return advertiser_service.create_advertiser(advertiser)


@router.post("/tor_controller", tags=["tor"])
def set_tor_controller():
    response_json = {}
    tor_controller = TorController()

    old_ip_address = tor_controller.get_ip()
    tor_controller.change_ip()
    new_ip_address = tor_controller.get_ip()

    response_json["old_ip"] = old_ip_address
    response_json["new_ip"] = new_ip_address
    return response_json