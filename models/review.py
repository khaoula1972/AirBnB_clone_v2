#!/usr/bin/python3
"""
This conatins the class reviews
"""
from models.base_model import BaseModel
# from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """
    This is Review class that inherets from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    """
    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)"""
