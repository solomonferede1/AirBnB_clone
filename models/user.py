#!/usr/bin/python3
"""
=====================================
Module with the class user
=====================================
"""

import models
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
