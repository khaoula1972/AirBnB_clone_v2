#!/usr/bin/python3
"""
This conatins a class calle Basemodel
"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.types import DateTime

Base = declarative_base()


class BaseModel:
    """
    This is a class that defines all common attributes/methods
    for other classes.
    """
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initialization...
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue  # To skip the class attribute
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        """
            if 'id' not in kwargs:
                # To generate a unique ID
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                # To set creation timestamp
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()  # Initial update
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  n# New element
            """

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        import models

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """
        To print
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """
        class_name = self.__class__.__name__
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = class_name
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def delete(self):
        """delete instance"""
        import models
        models.storage.delete(self)
