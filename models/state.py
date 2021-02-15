#!/usr/bin/python3
"""state module

Classes
    State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Creates State intances

    Attributes:
        name (str): state's name
    """
    name = ""
