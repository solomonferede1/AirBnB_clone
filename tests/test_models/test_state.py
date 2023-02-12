#!/usr/bin/python3
"""User unittest module for the class State"""

import unittest
import os
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """test case for User"""

    def test_docstring(self):
        """ checks if docstring is there """
        self.assertIsNotNone(State.__doc__)

    def test_State_is_dict(self):
        """testing if is a  dictionary"""
        st = FileStorage()
        st_dict = st.all()
        self.assertEqual(dict, type(st_dict))

    def test_state(self):
        """testing State class"""
        s = State()
        self.assertEqual(type(s), State)
        self.assertEqual(s.name, "")
        s.name = "Arauca"
        self.assertEqual(s.name, "Arauca")

    def test_save_is_dict(self):
        """ tests to see if the return type of save is a string """
        bm = State()
        bm.save()
        self.assertIsInstance(bm.to_dict()['created_at'], str)
        self.assertIsInstance(bm.to_dict()['updated_at'], str)

    def test_has_attr(self):
        """ tests if the base model has the attr """
        self.assertTrue(hasattr(State, "save"))

if __name__ == "__main__":
    unittest.main()
