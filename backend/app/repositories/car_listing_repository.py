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

    def create_car_listing(self, car_listing):
        with self.session_factory() as session:
            db_car_listing= CarListing(price=car_listing.price)
            session.add(db_car_listing)
            session.commit()
            session.refresh(db_car_listing)
            return db_car_listing