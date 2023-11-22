#!/usr/bin/python3
"""
This conatins the class amenity
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

# Define the association table
association_table = Table('place_amenity', Base.metadata,
        Column('place_id', String(60),
            ForeignKey('places.id'), nullable=False,
            primary_key=True),
        Column('amenity_id', String(60),
            ForeignKey('amenities.id'), nullable=False,
            primary_key=True)


class Amenity(BaseModel, Base):
    """
    This is Amenity class that inherets from BaseModel
    """

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place",
        secondary='place_amenity',
        back_populates="amenities", viewonly=False)"""
