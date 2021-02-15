#!/usr/bin/python3
"""city module

Classes
    City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Creates City intances

    Attributes:
        state_id (str): state's id <State>.<id>
        name (str): city's name
    """
    state_id = ""
    name = ""
