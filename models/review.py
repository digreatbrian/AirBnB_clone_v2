#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from airbnb.settings import MODELS_DIR
from airbnb.settings import DB_MODELS_DIR
from airbnb._import import _import


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""

if MODELS_DIR == DB_MODELS_DIR:
    Review = _import(MODELS_DIR + f".review.Review")

