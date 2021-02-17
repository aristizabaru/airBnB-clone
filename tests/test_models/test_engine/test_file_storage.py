#!/usr/bin/python3
"""test_file_storage module """
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

    # ####NEW TEST####

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

    def test_file_storage(self):
        ''' Tests for the creation of FileStorage classes. '''
        # Test type of FileStorage.
        self.assertEqual(type(models.storage), type(engine.FileStorage()))

        # Test private attributes.
        self.assertTrue(hasattr(models.storage, "_FileStorage__objects"))
        self.assertTrue(hasattr(models.storage, "_FileStorage__file_path"))

        # Get empty dictionary as there is no .json file.
        no_dicto = models.storage.all()

        # Test for the empty dictionary.
        self.assertTrue(bool(no_dicto))

    def test_FileStorage_no_args(self):
        ''' Tests for creation of FileStorage class. '''
        self.assertEqual(type(engine.FileStorage()), engine.FileStorage)

    def test_json_path(self):
        """Test if json file exist"""
        my_base = base.BaseModel()
        my_base.save()
        pwd = os.getcwd()
        path = pwd + "/file.json"
        self.assertTrue(os.path.exists(path))

    def test_all(self):
        '''Test all callback dict '''
        new = base.BaseModel()
        tempo_dict = models.storage.all()
        self.assertIsInstance(tempo_dict, dict)

        # Test for checking BaseModel.id key in dictionary.
        string_id = "BaseModel" + "." + new.id
        self.assertIn(string_id, tempo_dict.keys())

        # Test for object in the dictionary.
        self.assertTrue(type(tempo_dict[string_id]), base.BaseModel)

    def test_new(self):
        """test new instance in objects"""

        # Create BaseModel instance.
        base_x = base.BaseModel()

        with self.assertRaises(TypeError):
            models.storage.new(base_x, 1)
        tempo_dict = models.storage.all()

        # Concatenate ClassName.id string
        base_x_id = "BaseModel" + "." + base_x.id

        # Set attributes.
        user_x = models.user.User()
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
        """Test fors the reload() method"""

        # Create test instances.
        bas = models.base_model.BaseModel()
        ame = models.amenity.Amenity()
        rev = models.review.Review()
        pla = models.place.Place()
        sta = models.state.State()
        usr = models.user.User()
        cit = models.city.City()

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
