#!/usr/bin/python3
"""test_base_model module """
import unittest
import pep8
import models
import datetime
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

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        # Boot __objects private attribute
        FileStorage._FileStorage__objects = {}

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

    def test_attributes(self):
        """Test attributes id, created_at and updated_at"""
        my_base = BaseModel()
        my_base2 = BaseModel()
        self.assertTrue(hasattr(my_base, "id"), "'id' attribute not found")
        self.assertTrue(hasattr(my_base, "created_at"),
                        "'created_at' attribute not found")
        self.assertTrue(hasattr(my_base, "updated_at"),
                        "'updated_at' attribute not found")
        self.assertNotEqual(my_base.id, my_base2.id,
                            "BaseModels instances has the same 'id'")

    def test_datetime(self):
        """Test if instances are created with different times"""
        my_base1 = BaseModel()
        my_date = datetime.datetime.now()
        my_base2 = BaseModel()
        self.assertTrue(my_base1.created_at <= my_date <= my_base2.created_at,
                        "There are some equal dates")
        self.assertEqual(my_base1.created_at,
                         my_base1.updated_at, "Dates are not equal")
        self.assertEqual(my_base2.created_at,
                         my_base2.updated_at, "Dates are not equal")

    def test_save(self):
        """Test 'update_at' and 'created_at' after some updates"""
        my_base = BaseModel()
        updated = my_base.updated_at
        self.assertEqual(my_base.created_at, updated,
                         "Dates are not equal")
        my_base.save()
        self.assertNotEqual(my_base.updated_at, updated,
                            "updated_at is equal than previous updated_at")
        self.assertNotEqual(my_base.created_at, my_base.updated_at,
                            "created_at is equal than updated_at")
