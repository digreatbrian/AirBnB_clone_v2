#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from airbnb.settings import MODELS_DIR
from airbnb.settings import DB_MODELS_DIR
from airbnb._import import _import


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

if MODELS_DIR == DB_MODELS_DIR:
    User = _import(MODELS_DIR + f".user.User")

