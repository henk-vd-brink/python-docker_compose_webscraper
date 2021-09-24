from app.models import Advertiser
from app.schemas import AdvertiserCreate

class AdvertiserRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def get_advertisers(self, skip: int=0, limit: int=100):
        with self.session_factory() as session:
            return session.query(Advertiser).offset(skip).limit(limit).all()

    def get_advertiser_by_name(self, advertiser_name):
        with self.session_factory() as session:
            return session.query(Advertiser).filter(Advertiser.name == advertiser_name).first()

    def create_advertiser(self, advertiser):
        with self.session_factory() as session:
            db_advertiser= Advertiser(  name=advertiser.name,
                                        activity=advertiser.activity,
                                        rating=advertiser.rating)
            session.add(db_advertiser)
            session.commit()
            session.refresh(db_advertiser)
            return db_advertiser