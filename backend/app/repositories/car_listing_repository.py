from app.models import CarListing
from app.schemas import CarListingCreate

class CarListingRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def get_car_listings(self, skip: int=0, limit: int=100):
        with self.session_factory() as session:
            return session.query(CarListing).offset(skip).limit(limit).all()

    def get_car_listing_by_id(self, car_listing_id):
        with self.session_factory() as session:
            return session.query(CarListing).filter(CarListing.id == car_listing_id).first()

    def get_car_listing_by_title(self, car_listing_title):
        with self.session_factory() as session:
            return session.query(CarListing).filter(CarListing.title == car_listing_title).first()

    def create_car_listing(self, car_listing):
        with self.session_factory() as session:
            db_car_listing= CarListing( title=car_listing.title,
                                        price=car_listing.price,
                                        brand_model=car_listing.brand_model,
                                        mileage=car_listing.mileage,
                                        fuel_type=car_listing.fuel_type,
                                        year_of_construction=car_listing.year_of_construction,
                                        advertiser_name=car_listing.advertiser_name,
                                        category=car_listing.category)
            session.add(db_car_listing)
            session.commit()
            session.refresh(db_car_listing)
            return db_car_listing