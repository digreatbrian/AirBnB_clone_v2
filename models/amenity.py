#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from airbnb.settings import MODELS_DIR
from airbnb.settings import DB_MODELS_DIR
from airbnb._import import _import


class Amenity(BaseModel):
    name = ""

if MODELS_DIR == DB_MODELS_DIR:
    Amenity = _import(MODELS_DIR + f".amenity.Amenity")

