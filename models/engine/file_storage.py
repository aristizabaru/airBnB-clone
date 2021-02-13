#!/usr/bin/python3
"""file_storage module

Classes
    FileStorage
"""

# create docstrings
import json
import os.path


class FileStorage:
    __file_path = "file.json"
    __objects = dict()

    # methods
    def all(self):
        return type(self).__objects

    def new(self, obj):
        type(self).__objects[str(obj.__class__.__name__) +
                             "." + obj.id] = obj.to_dict()

    def save(self):
        with open(type(self).__file_path, "w", encoding="utf-8") as fd:
            json.dump(type(self).__objects, fd)

    def reload(self):
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, encoding="utf-8") as fd:
                type(self).__objects = json.load(fd)
