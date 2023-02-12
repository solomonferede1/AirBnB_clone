#!/usr/bin/python3
"""
==========================================
User unittest module for the class City
==========================================
"""

import unittest
import os
from models.city import City
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """test case for City"""

    def test_docstring(self):
        """ checks if docstring is there """

        self.assertIsNotNone(City.__doc__)

    def test_City_is_dict(self):
        """testing if dict"""

        st = FileStorage()
        st_dict = st.all()
        self.assertEqual(dict, type(st_dict))

    def test_city(self):
        """testing user class"""

        c = City()
        self.assertEqual(type(c), City)
        self.assertEqual(c.name, "")
        self.assertEqual(c.state_id, "")
        c.state_id = 2020
        c.name = "Bogota"
        self.assertEqual(c.state_id, 2020)
        self.assertEqual(c.name, "Bogota")

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """

        bm = City()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """

        self.assertTrue(hasattr(City, "save"))

if __name__ == "__main__":
    unittest.main()
