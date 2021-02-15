#!/usr/bin/python3
"""place module

Classes
    Place
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Creates Place intances

    Atributes:
        city_id (str): city id <City>.<id>
        user_id (str): user id <User>.<id>
        name (str): Place's name
        description (str): desctription
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): number of max guest
        price_by_night (int): price by night
        latitude (float): latitude
        longitude (float): longitude
        amenity_ids (list): list of string of <Amenity>.<id>
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list()
