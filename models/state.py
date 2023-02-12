#!/usr/bin/python3
"""
========================================================
Module whit the state class that inherits from BaseModel
========================================================
"""

import models
from models.base_model import BaseModel


class State(BaseModel):
    """class that inherits form BaseModel and save the state name"""

    name = ""
