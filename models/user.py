#!/usr/bin/python3
"""
This conatins the class user
"""
from models.base_model import BaseModel
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship


class User(BaseModel):
    """
    This is User class that inherets from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", cascade="delete", backref="user")"""
