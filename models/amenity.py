#!/usr/bin/python3
"""amenity module

Classes
    Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Creates Amenity intances

    Attributes:
        name (str): amenity's name
    """
    name = ""
