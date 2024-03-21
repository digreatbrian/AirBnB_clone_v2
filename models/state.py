#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from airbnb.settings import MODELS_DIR
from airbnb.settings import DB_MODELS_DIR
from airbnb._import import _import


class State(BaseModel):
    """ State class """
    name = ""

if MODELS_DIR == DB_MODELS_DIR:
    State = _import(MODELS_DIR + f".state.State")

