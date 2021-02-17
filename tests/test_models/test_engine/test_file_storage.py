#!/usr/bin/python3
""" Module for storing the tests for BaseModel instances. """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
import models
import uuid
import unittest
import os


class TestFileStorage(unittest.TestCase):
    '''
    TestCase class for testing the FileStorage instances and the storage
    variable.
    '''

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

    def test_FileStorage_no_args(self):
        ''' Tests for creation of FileStorage class. '''
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_JSON_file(self):
        ''' Tests for the file.json. '''
        base = BaseModel()
        base.save()
        pwd = os.getcwd()
        path = pwd + "/file.json"
        self.assertTrue(os.path.exists(path))

    def test_all(self):
        '''Test all callback dict '''
        new = BaseModel()
        tempo_dict = models.storage.all()
        self.assertIsInstance(tempo_dict, dict)

        # Test for checking BaseModel.id key in dictionary.
        string_id = "BaseModel" + "." + new.id
        self.assertIn(string_id, tempo_dict.keys())

        # Test for object in the dictionary.
        self.assertTrue(type(tempo_dict[string_id]), BaseModel)

    def test_new(self):
        '''test new instance in objects'''

        # Create BaseModel instance.
        base_x = BaseModel()

        with self.assertRaises(TypeError):
            models.storage.new(base_x, 1)
        tempo_dict = models.storage.all()

        # Concatenate ClassName.id string
        base_x_id = "BaseModel" + "." + base_x.id

        # Set attributes.
        user_x = User()
        user_x.email = "pruebas@prueba.com"
        user_x.first_name = "Don"
        user_x.last_name = "Pruebas"
        user_x.password = "tambienprueba"

        user_x_id = "User." + user_x.id

        for key, value in tempo_dict.items():
            if key == user_x_id:
                self.assertTrue(hasattr(user_x, "email"))
                self.assertTrue(hasattr(user_x, "first_name"))
                self.assertTrue(hasattr(user_x, "last_name"))
                self.assertTrue(hasattr(user_x, "password"))
                self.assertTrue(hasattr(user_x, "id"))

        self.assertIn(base_x_id, tempo_dict.keys())

        self.assertIn(user_x_id, tempo_dict.keys())

        models.storage.save()
        # Test file created after new
        pwd = os.getcwd()
        path = pwd + "/file.json"
        self.assertTrue(os.path.exists(path))

    def test_reload(self):
        """ Test fors the reload() method. """

        # Create test instances.
        bas = BaseModel()
        ame = Amenity()
        rev = Review()
        pla = Place()
        sta = State()
        usr = User()
        cit = City()

        # Create list of objects.
        list_objs = [bas, ame, rev, pla, sta, usr, cit]

        list_obj_id = []
        for obj in list_objs:
            list_obj_id.append(obj.__class__.__name__ + "." + obj.id)

        # Save objects into file.
        models.storage.save()

        # Start test for reload.
        models.storage.reload()

        for obj_id in list_obj_id:
            self.assertIn(obj_id, models.storage.all().keys())


if __name__ == '__main__':
    unittest.main()
