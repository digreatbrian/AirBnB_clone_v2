#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from sqlalchemy.ext.declarative import declarative_base
from models import storage
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class BaseModel(Base):
    """
    Base class for all models in the HBNB clone.
    """

    __tablename__ = 'base_model'

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """
        Deletes the current instance from the storage.
        """
        storage.delete(self)
