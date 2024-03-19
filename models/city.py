#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from airbnb.settings import MODELS_DIR
from airbnb.settings import DB_MODELS_DIR
from airbnb._import import _import


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

if MODELS_DIR == DB_MODELS_DIR:
    User = _import(MODELS_DIR + f".city.City")

