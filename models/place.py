#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer, Table


# Define association table for many-to-many relationship between Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # Define relationships for ORM
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', cascade='all, delete, delete-orphan', backref='place')
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, back_populates='place_amenities')
    else:
        @property
        def reviews(self):
            """list of Review instances associated with the place """
            from models import storage
            review_instances = storage.all("Review").values()
            return [review for review in review_instances if review.place_id == self.id]

        @property
        def amenities(self):
            from models import storage
            amenity_instances = storage.all("Amenity").values()
            return [amenity for amenity in amenity_instances if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
      		""" Setter attribute for amenities """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
