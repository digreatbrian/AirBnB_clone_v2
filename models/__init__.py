#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage depending of env variables"""
from airbnb.settings import STORAGE_ENGINE
from airbnb._import import _import
from airbnb.environ import load_environ

#loading envronment
load_environ()

from .amenity import Amenity
from .city import City
from .place import Place
from .state import State
from .user import User

try:
    from .base_model import Base
except ImportError:
    pass

storage = _import(STORAGE_ENGINE)() #loading storage engine
storage.reload()
