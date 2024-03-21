#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from airbnb.settings import MODELS_DIR
from airbnb.settings import DB_MODELS_DIR
from airbnb._import import _import

class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

if MODELS_DIR == DB_MODELS_DIR:
    Place = _import(MODELS_DIR + f".place.Place")

