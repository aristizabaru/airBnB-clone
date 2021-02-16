#!/usr/bin/python3
"""test_base_model module """
import unittest
import pep8
import models
BaseModel = models.base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_base = BaseModel()
        my_base.name = "Betty"
        my_base.my_number = 60
        my_base.email = "betty.holberton@airbnb.com"
        base_dict = my_base.to_dict()
        attributes = ["id", "created_at", "updated_at",
                      "name", "my_number", "email", "__class__"]
        self.assertCountEqual(base_dict.keys(), attributes)
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(base_dict["name"], "Betty")
        self.assertEqual(base_dict["my_number"], 60)
        self.assertEqual(base_dict["email"], "betty.holberton@airbnb.com")
