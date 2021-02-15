#!/usr/bin/python3
"""user module

Classes
    User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Creates User intances

    Attributes:
        email (str): email from user
        password (str): password from user
        first_name (str): first name from user
        last_name (str): last_name from user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
