#!/usr/bin/python3
"""
========================================================
Module whit the City class that inherits from BaseModel
========================================================
"""

import models
from models.base_model import BaseModel


class City(BaseModel):
    """class that inherits form BaseModel and save the city name"""

    state_id = ""
    name = ""
