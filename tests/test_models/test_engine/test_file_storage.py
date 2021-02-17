#!/usr/bin/python3
"""test_file_storage module """
from os import path, remove
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import io
from datetime import datetime
import unittest
import pep8
import models.engine.file_storage as engine
import json
import models.base_model as base
import os
import models


class TestFileStorageDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_storage_all(self):
        """Test that storage returns the FileStorage.__objects attr"""
        storage = engine.FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        # Take name of private attribute from __dict__
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_reload(self):
        """Test reload when the file is not present"""
        storage = engine.FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        fname = "file.json"
        self.assertFalse(os.path.isfile(fname))
        storage.reload()

    def test_save_json(self):
        """Test that save properly saves objects to file.json"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        storage = engine.FileStorage()
        back_up = storage.all()
        storage.save()
        # FILE -> json.load() -> <dict>
        with open("file.json", encoding="utf-8") as fd:
            json_data = json.load(fd)
        # <obj> -> <dict>
        for key in back_up:
            back_up[key] = back_up[key].to_dict()
        # compare both back_up and json_data
        self.assertDictEqual(json_data, back_up)

    def test_new(self):
        """Test that add an object to the FileStorage instance"""
        storage = engine.FileStorage()
        back_up = storage._FileStorage__objects
        my_base = base.BaseModel()
        storage._FileStorage__objects = {}
        new_dict = storage._FileStorage__objects
        count_new = len(new_dict)
        count_back_up = len(back_up)
        self.assertNotEqual(count_new, count_back_up,
                            "Both dictionaries have same number of items")

    def test_intance_type(self):
        """Test that variable  storage is a FileStorage instance"""
        self.assertEqual(FileStorage, type(FileStorage()))
