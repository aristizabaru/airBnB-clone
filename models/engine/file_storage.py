#!/usr/bin/python3
"""file_storage module

Classes
    FileStorage
"""

# create docstrings
import json
import os.path
import models
"""from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
# list of valid models
"""models_dict = {"BaseModel": BaseModel,
"User": User, "State": State, "City": City,
"Amenity": Amenity, "Place": Place, "Review": Review}
"""


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances

    Methods
        all()
        new(obj)
        save()
        reload()
    """
    __file_path = "file.json"
    __objects = dict()

    # methods
    def all(self):
        """returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Parameters
            obj (BaseClass): object to append into dict
        """
        if obj:
            type(self).__objects[str(obj.__class__.__name__) +
                                 "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        # <class 'BaseModel'> -> to_dict()
        json_data = type(self).__objects.copy()
        for key in json_data:
            json_data[key] = json_data[key].to_dict()
        # <class 'dict'> -> JSON dump -> FILE
        with open(type(self).__file_path, "w", encoding="utf-8") as fd:
            json.dump(json_data, fd, indent=4, ensure_ascii=False)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(type(self).__file_path):
            # FILE -> <class 'str'> -> JSON load -> <class 'dict'>
            with open(type(self).__file_path, encoding="utf-8") as fd:
                json_data = json.load(fd)
            # <class 'dict'> -> <class 'Models'>
            for key in json_data:
                new_key = json_data[key]["__class__"]
                type(self).__objects[key] = models.models_dict[new_key](
                    **json_data[key])
