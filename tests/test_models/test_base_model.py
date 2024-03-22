#!/usr/bin/python3
<<<<<<< HEAD
""" """
import unittest
import datetime
import json
from models.base_model import BaseModel
from airbnb.settings import STORAGE_ENGINE, STORAGE_ENGINES

@unittest.skipIf((STORAGE_ENGINE == STORAGE_ENGINES["dbstorage"]), "Tests not compatible with DBStorage ")
class Test_Basemodel(unittest.TestCase):
    """ Test Basemodel """
=======
"""
    tests for BaseModel
"""
import unittest
from datetime import datetime
import time
import re
import os
from models.base_model import BaseModel

>>>>>>> 7d849a5c058916a2f2082cebc92626da93674115

class Test_BaseModel(unittest.TestCase):
    """
        Base test class
    """
    @classmethod
    def setUpClass(cls):
        """setup class"""
        cls.dummy = BaseModel()

<<<<<<< HEAD
    def setUp(self):
        """ setup """
        pass

    def tearDown(self):
=======
    @classmethod
    def tearDownClass(cls):
        """tear down"""
        del cls.dummy
>>>>>>> 7d849a5c058916a2f2082cebc92626da93674115
        try:
            os.remove("file.json")
        except:
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

<<<<<<< HEAD
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

    def test_id(self):
        """ test_id """
        new = self.value()
        self.assertEqual(type(new.id), str)

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
=======
    def test_unique_id(self):
        """
            test unique ID's
        """
        dummy_1 = BaseModel()
        dummy_2 = BaseModel()
        self.assertNotEqual(dummy_1.id, dummy_2.id)
        del dummy_1
        del dummy_2

    def test_creation_time(self):
        """
            test initial creation time and updation time
        """
        dummy = self.dummy
        self.assertIsInstance(dummy.created_at, datetime)
        self.assertIsInstance(dummy.updated_at, datetime)
        self.assertEqual(dummy.updated_at, dummy.created_at)

    def test_str(self):
        """
            test string representation of an object
        """
        dummy = self.dummy
        correct = "[{}] ({}) {}".format("BaseModel", dummy.id, dummy.__dict__)
        self.assertEqual(str(dummy), correct)

    def test_dict(self):
        """
            test dictionary representation of a model
        """
        dummy = self.dummy
        test_dict = dummy.to_dict()
        self.assertTrue("__class__" in test_dict)
        self.assertIsInstance(test_dict["__class__"], str)
        self.assertTrue("id" in test_dict)
        self.assertIsInstance(test_dict["id"], str)
        self.assertTrue("created_at" in test_dict)
        self.assertIsInstance(test_dict["created_at"], str)
        self.assertTrue("updated_at" in test_dict)
        self.assertIsInstance(test_dict["updated_at"], str)
        dummy.test = 10
        test_dict = dummy.to_dict()
        self.assertTrue("test" in test_dict)

    def test_fromdict(self):
        """
            test instance retrival from a dictionary
        """
        dummy = self.dummy
        dummy.test = 10
        test_instance = BaseModel(**dummy.to_dict())
        self.assertTrue("__class__" not in test_instance.__dict__)
        self.assertTrue(hasattr(test_instance, "id"))
        self.assertTrue(hasattr(test_instance, "created_at"))
        self.assertTrue(hasattr(test_instance, "updated_at"))
        self.assertTrue(hasattr(test_instance, "test"))
        self.assertIsInstance(test_instance.created_at, datetime)
        self.assertIsInstance(test_instance.updated_at, datetime)
        self.assertEqual(test_instance.created_at, dummy.created_at)
        self.assertEqual(test_instance.updated_at, dummy.updated_at)


if __name__ == "__main__":
        unittest.main()
>>>>>>> 7d849a5c058916a2f2082cebc92626da93674115
