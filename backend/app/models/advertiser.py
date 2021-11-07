from sqlalchemy import Column, String
from app.database import Base


class AdvertiserBase(Base):
    __tablename__ = "advertisers"
    
    name = Column(String, primary_key=True, index=True)
    activity = Column(String)
    rating = Column(String)

    



