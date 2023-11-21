#!/usr/bin/python3
"""
This conatins the class city
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    This is City class that inherets from BaseModel
    """
    __tablename__ = 'cities'

    state_id = Column(String(128), nullable=False)
    name = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship(
            "Place", cascade="all, delete-orphan", backref="city"
            )
