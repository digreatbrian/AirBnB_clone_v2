#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Objects will be stored.
    """

    def __init__(self):
        """Initialize FileStorage class"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects or objects of a specific class.

        Args:
            cls (class, optional): Class of the objects to filter.

        Returns:
            dict: Dictionary of objects.
        """
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        else:
            return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: Object to be added.
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize the objects to JSON and write to file."""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize the JSON file and load objects into memory."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    cls_name = value.get('__class__')
                    if cls_name:
                        cls = eval(cls_name)
                        obj = cls(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an existing object from storage."""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Close the file storage."""
        self.reload()
