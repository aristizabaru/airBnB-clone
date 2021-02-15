#!/usr/bin/python3
"""review module

Classes
    Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Creates Review intances

    Atributes:
        place_id (str): Place.id <Place>.<id>
        user_id (str): User.id <User>.<id>
        text (str): review from user
    """
    place_id = ""
    user_id = ""
    text = ""
