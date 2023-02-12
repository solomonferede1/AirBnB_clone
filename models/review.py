#!/usr/bin/python3
"""
========================================================
Module whit the Revies class that inherits from BaseModel
========================================================
"""

import models
from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherits from BaseModel and save the review features"""

    place_id = ""
    user_id = ""
    text = ""
