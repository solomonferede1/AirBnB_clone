#!/usr/bin/python3
"""test for the class Base_model"""


import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
# from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_base_model(self):
        """testing the BaseModel"""
        dog = BaseModel()
        self.assertIs(type(dog.id), str)
        self.assertIs(type(dog.created_at), datetime)
        self.assertIs(type(dog.updated_at), datetime)
        self.assertNotEqual(dog.created_at, dog.updated_at)
        self.assertFalse(dog.updated_at == datetime.utcnow())
        old_updated = dog.updated_at
        dog.save()

    def test_save_model(self):
        """ tests to see if the return type of save is a string """
        dog = BaseModel()
        dog.save()
        self.assertIsInstance(dog.to_dict()['created_at'], str)
        self.assertIsInstance(dog.to_dict()['updated_at'], str)
        old_updated = dog.created_at
        self.assertNotEqual(old_updated, dog.updated_at)
        d = dog.to_dict()
        self.assertEqual(type(d), dict)
        self.assertEqual(d['__class__'], "BaseModel")
        self.assertEqual(d['created_at'], dog.created_at.isoformat())
        self.assertEqual(d['updated_at'], dog.updated_at.isoformat())
        self.assertEqual(d['id'], dog.id)

    def test_save(self):
        """test if the model method save"""
        dog = self.value()
        dog.save()
        key = self.name + "." + dog.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], dog.to_dict())


if __name__ == '__main__':
    unittest.main()
