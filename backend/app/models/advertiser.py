from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from app.database import Base


class AdvertiserBase(Base):

    __tablename__ = "advertisers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    activity = Column(Integer)
    rating = Column(Integer)

    



