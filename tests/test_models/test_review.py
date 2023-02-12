#!/usr/bin/python3
"""
=========================================
User unittest module for the class Review
=========================================
"""

import unittest
import os
from models.review import Review
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """test case for Place class"""

    def test_docstring(self):
        """ checks if docstring is there """

        self.assertIsNotNone(Review.__doc__)

    def test_Place_is_dict(self):
        """testing if is a  dictionary"""

        st = FileStorage()
        st_dict = st.all()
        self.assertEqual(dict, type(st_dict))

    def test_place(self):
        """testing Place class"""

        r = Review()
        self.assertEqual(type(r), Review)
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """

        bm = Review()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """

        self.assertTrue(hasattr(Review, "save"))

if __name__ == "__main__":
    unittest.main()
