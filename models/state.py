#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base

class State(BaseModel):
    """ state in the application """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """
        Returns the list of City instances associated with the current state
        """
        from models import storage

        related_cities = []
        all_cities = storage.all(City)

        for city in all_cities.values():
            if city.state_id == self.id:
                related_cities.append(city)

        return related_cities
