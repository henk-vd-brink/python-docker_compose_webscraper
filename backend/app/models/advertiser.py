from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.database import Base


class AdvertiserBase(Base):

    __tablename__ = "advertisers"
    
    name = Column(String, primary_key=True, index=True)
    activity = Column(String)
    rating = Column(String)

    



