#!/usr/bin/python3
"""test_file_storage module """
import unittest
import pep8
import models.engine.file_storage as engine
import json
import models.base_model as base
import os
from models import models_dict


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

    def test_save_json(self):
        """Test that save properly saves objects to file.json"""
        os.remove("file.json")
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
        save = engine.FileStorage._FileStorage__objects
        engine.FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in models_dict.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        engine.FileStorage._FileStorage__objects = save
