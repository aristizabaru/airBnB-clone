#!/usr/bin/python3
''' Module for storing the tests for BaseModel instances. '''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import models
import uuid
import unittest
import os


class TestBaseModel(unittest.TestCase):
    ''' Test for BaseModel class instances. '''

    def setUp(self):
        ''' Setup for erasing file.json when starting every test. '''
        # Get Current Working Directory.
        cwd = os.getcwd()
        # Concat. the cwd to the name of the .json file
        file_path = cwd + "/file.json"
        # Try to remove it.
        try:
            os.remove(file_path)
        # Except it is not there.
        except Exception as e:
            pass
        # Reset dictionary of storage.
        models.storage._FileStorage__objects = {}

    def test_create_instance(self):
        ''' Tests for creation of basic BaseModel instances'''
        # Create BaseModel instance.
        base = BaseModel()
        base.name = "Holberton"
        base.my_number = 50

        # Test for proper type.
        self.assertEqual(type(base), type(BaseModel()))

        # Test for methods.
        self.assertIn("save", dir(base))
        self.assertIn("to_dict", dir(base))

        # Test if the instance has initial attributes.
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

        # Test for proper return of to_dict()
        self.assertEqual(type(base.to_dict()), type({}))
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

        # Test for properly setting a name attribute.
        self.assertEqual(base.name, "Holberton")
        self.assertEqual(base.my_number, 50)

        # Test if the type of the id is correct.
        version = uuid.UUID(base.id).version
        self.assertEqual(version, 4)

    def test_save_method(self):
        ''' Tests for the save method of BaseModel. '''
        # Create test BaseModel instance.
        base = BaseModel()

        # Test for dictionary from to dict method
        self.assertEqual(type(base.to_dict()), dict)

        # Save the instance in file.json
        base.save()

        # Test if file was created successfully
        cwd = os.getcwd()
        file_path = cwd + "/file.json"
        self.assertTrue(os.path.exists(file_path))

        # Create test strings of BaseModel
        string_base_id = "BaseModel" + "." + base.id
        string_base__class__ = "BaseModel"
        string_base_created = base.created_at.isoformat()
        string_base_updated = base.updated_at.isoformat()

        # Open and test if string is present in the file.
        with open("file.json", "r") as f:
            file_string = f.read()
            self.assertIn(string_base_id, file_string)
            self.assertIn(string_base__class__, file_string)
            self.assertIn(string_base_created, file_string)
            self.assertIn(string_base_updated, file_string)


if __name__ == '__main__':
    unittest.main()
