#!/usr/bin/python3
"""
========================================
User unittest module for the class State
========================================
"""

import unittest
import os
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """test case for Amenity class"""

    def test_docstring(self):
        """ checks if docstring is there """

        self.assertIsNotNone(Amenity.__doc__)

    def test_Amenity_is_dict(self):
        """testing if is a  dictionary"""

        st = FileStorage()
        st_dict = st.all()
        self.assertEqual(dict, type(st_dict))

    def test_Amenity(self):
        """testing Amenity class"""

        a = Amenity()
        self.assertEqual(type(a), Amenity)
        self.assertEqual(a.name, "")
        a.name = "Muy bueno"
        self.assertEqual(a.name, "Muy bueno")

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """

        bm = Amenity()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """

        self.assertTrue(hasattr(Amenity, "save"))

if __name__ == "__main__":
    unittest.main()
