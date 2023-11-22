#!/usr/bin/python3
"""
This conatins the class place
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float


class Place(BaseModel, Base):
    """
    This is Place class that inherets from BaseModel
    """
    __tablename__ = 'places'

    city_id = Column(String(60), nullable=False)
    user_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship(
            "Review", cascade="all, delete-orphan", backref="place"
            )
