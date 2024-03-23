#!/usr/bin/python3
""" test base model """
import unittest
import datetime
import json
import os
from models.base_model import BaseModel
from airbnb.settings import STORAGE_ENGINE, STORAGE_ENGINES


@unittest.skipIf((STORAGE_ENGINE == STORAGE_ENGINES["dbstorage"]),
                 "Tests not compatible with DBStorage")
class TestBaseModel(unittest.TestCase):
    """
        Base test class
    """
    @classmethod
    def setUpClass(cls):
        """setup class"""
        cls.dummy = BaseModel()

    def setUp(self):
        """ setup """
        pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_id(self):
        """
            test id is a valid UUID
        """
        dummy = self.dummy
        self.assertIsInstance(dummy, BaseModel)
        self.assertIsInstance(dummy.id, str)
        is_match = re.fullmatch(r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}", dummy.id)
        self.assertTrue(is_match)

    def test_id2(self):
        """ test_id """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_kwargs(self):
        """ test_kwarg """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ test_kwargs_int """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r', encoding="utf-8") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ test_str """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ test_todict """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ test_kwargs_none """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ test_kwargs_one """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_created_at(self):
        """ test_created_at """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ test_updated_at """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at != new.updated_at)
