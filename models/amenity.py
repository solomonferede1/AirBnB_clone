#!/usr/bin/python3
"""
========================================================
Module whit the Amenity class that inherits from BaseModel
========================================================
"""

import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class that inherits from BaseModel and save the amenity"""

    name = ""
