#!/usr/bin/python3
"""
=========================================
User unittest module for the class Place
=========================================
"""

import unittest
import os
from models.place import Place
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """test case for Place class"""

    def test_docstring(self):
        """ checks if docstring is there """

        self.assertIsNotNone(Place.__doc__)

    def test_Place_is_dict(self):
        """testing if is a  dictionary"""

        st = FileStorage()
        st_dict = st.all()
        self.assertEqual(dict, type(st_dict))

    def test_place(self):
        """testing Place class"""

        p = Place()
        self.assertEqual(type(p), Place)
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, [])
        p.name = "Chapinhero"
        p.number_rooms = 2
        self.assertEqual(p.name, "Chapinhero")
        self.assertEqual(p.number_rooms, 2)

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """

        bm = Place()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """

        self.assertTrue(hasattr(Place, "save"))

if __name__ == "__main__":
    unittest.main()
