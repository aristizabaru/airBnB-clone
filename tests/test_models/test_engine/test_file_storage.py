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


# ------------ TEST -------------


class Test_all(unittest.TestCase):
    """ Test for the all method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_all_empty(self):
        """ Test Empty Dictionary """
        self.assertEqual(storage.all(), {})

    def test_basemodel(self):
        """ Test with basemodel object """
        b = BaseModel()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_user(self):
        """ Test with basemodel object """
        b = User()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_city(self):
        """ Test with basemodel object """
        b = City()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_amenity(self):
        """ Test with basemodel object """
        b = Amenity()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_place(self):
        """ Test with basemodel object """
        b = Place()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_review(self):
        """ Test with basemodel object """
        b = Review()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_state(self):
        """ Test with basemodel object """
        b = State()
        name = b.__class__.__name__ + '.' + b.id
        dic = {name: b}
        self.assertEqual(storage.all(), dic)

    def test_all_class(self):
        """ Test with all classes """
        b = BaseModel()
        u = User()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        s = State()

        alldic = storage.all()

        self.assertEqual(b, alldic["BaseModel" + '.' + b.id])
        self.assertEqual(u, alldic["User" + '.' + u.id])
        self.assertEqual(c, alldic["City" + '.' + c.id])
        self.assertEqual(a, alldic["Amenity" + '.' + a.id])
        self.assertEqual(p, alldic["Place" + '.' + p.id])
        self.assertEqual(r, alldic["Review" + '.' + r.id])
        self.assertEqual(s, alldic["State" + '.' + s.id])


class Test_new(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_no_arg(self):
        """ Test no passing argument """
        with self.assertRaises(TypeError):
            storage.new()

    def test_extra_arg(self):
        """ Test no passing argument """
        b = BaseModel()
        with self.assertRaises(TypeError):
            storage.new(b, b)

    def test_basenew(self):
        """ Tests new method with basemodel """
        dic = {"id": "123"}
        b = BaseModel(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_usernew(self):
        """ Tests new method with user """
        dic = {"id": "123"}
        b = User(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_city(self):
        """ Tests new method with city """
        dic = {"id": "123"}
        b = City(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_amenity(self):
        """ Tests new method with amenity """
        dic = {"id": "123"}
        b = Amenity(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_place(self):
        """ Tests new method with amenity """
        dic = {"id": "123"}
        b = Place(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_review(self):
        """ Tests new method with review """
        dic = {"id": "123"}
        b = Review(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])

    def test_state(self):
        """ Tests new method with state """
        dic = {"id": "123"}
        b = State(**dic)
        key = b.__class__.__name__ + '.' + "123"
        alldic = storage.all()
        self.assertEqual(alldic, {})
        storage.new(b)
        alldic = storage.all()
        self.assertEqual(b, alldic[key])


class Test_save(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_save_base_no_dic(self):
        """ Save method with base model no kwarg """
        b = BaseModel()
        key = b.__class__.__name__ + '.' + b.id
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])

    def test_save_base_no_dicX2(self):
        """ Save method with base model no kwarg """
        b = BaseModel()
        b2 = BaseModel()
        key = b.__class__.__name__ + '.' + b.id
        key2 = b2.__class__.__name__ + '.' + b2.id
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[key]["id"])
            self.assertEqual(b.__class__.__name__, pobj[key]["__class__"])
            self.assertEqual(b2.id, pobj[key2]["id"])
            self.assertEqual(b2.__class__.__name__, pobj[key2]["__class__"])

    def test_save_all_class_no_kwarg(self):
        """ Save method with all_classes no kwarg"""
        b = BaseModel()
        u = User()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        s = State()
        keyb = b.__class__.__name__ + '.' + b.id
        keyu = u.__class__.__name__ + '.' + u.id
        keyc = c.__class__.__name__ + '.' + c.id
        keya = a.__class__.__name__ + '.' + a.id
        keyp = p.__class__.__name__ + '.' + p.id
        keyr = r.__class__.__name__ + '.' + r.id
        keys = s.__class__.__name__ + '.' + s.id
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        with open(fname, encoding="utf-8") as myfile:
            pobj = json.load(myfile)
            self.assertEqual(b.id, pobj[keyb]["id"])
            self.assertEqual(b.__class__.__name__, pobj[keyb]["__class__"])
            self.assertEqual(u.id, pobj[keyu]["id"])
            self.assertEqual(u.__class__.__name__, pobj[keyu]["__class__"])
            self.assertEqual(c.id, pobj[keyc]["id"])
            self.assertEqual(c.__class__.__name__, pobj[keyc]["__class__"])
            self.assertEqual(a.id, pobj[keya]["id"])
            self.assertEqual(a.__class__.__name__, pobj[keya]["__class__"])
            self.assertEqual(p.id, pobj[keyp]["id"])
            self.assertEqual(p.__class__.__name__, pobj[keyp]["__class__"])
            self.assertEqual(r.id, pobj[keyr]["id"])
            self.assertEqual(r.__class__.__name__, pobj[keyr]["__class__"])
            self.assertEqual(s.id, pobj[keys]["id"])
            self.assertEqual(s.__class__.__name__, pobj[keys]["__class__"])


class Test_reload(unittest.TestCase):
    """ Test for the new method """

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Tear down for all methods """
        try:
            remove("file.json")
        except:
            pass

    def test_no_file(self):
        """ Test if no error happens when to file is present """
        fname = "file.json"
        self.assertFalse(path.isfile(fname))
        storage.reload()

    def test_reload_base(self):
        """ Test reload method with base model """
        fname = "file.json"
        b = BaseModel()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_user(self):
        """ Test reload method with user """
        fname = "file.json"
        b = User()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_city(self):
        """ Test reload method with city """
        fname = "file.json"
        b = City()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_amenity(self):
        """ Test reload method with amenity """
        fname = "file.json"
        b = Amenity()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_place(self):
        """ Test reload method with place """
        fname = "file.json"
        b = Place()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_review(self):
        """ Test reload method with review """
        fname = "file.json"
        b = Review()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_state(self):
        """ Test reload method with state """
        fname = "file.json"
        b = State()
        b.name = "Holberton"
        key = b.__class__.__name__ + '.' + b.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        self.assertFalse(b == alldic[key])
        self.assertEqual(b.id, alldic[key].id)
        self.assertEqual(b.__class__, alldic[key].__class__)
        self.assertEqual(b.created_at, alldic[key].created_at)
        self.assertEqual(b.updated_at, alldic[key].updated_at)
        self.assertEqual(b.name, alldic[key].name)

    def test_reload_all_clases(self):
        """ Test reload method for all classes """
        fname = "file.json"
        b = BaseModel()
        u = User()
        c = City()
        a = Amenity()
        p = Place()
        r = Review()
        s = State()
        keyb = b.__class__.__name__ + '.' + b.id
        keyu = u.__class__.__name__ + '.' + u.id
        keyc = c.__class__.__name__ + '.' + c.id
        keya = a.__class__.__name__ + '.' + a.id
        keyp = p.__class__.__name__ + '.' + p.id
        keyr = r.__class__.__name__ + '.' + r.id
        keys = s.__class__.__name__ + '.' + s.id
        self.assertFalse(path.isfile(fname))
        storage.save()
        self.assertTrue(path.isfile(fname))
        self.assertTrue(len(storage.all()) > 0)
        FileStorage._FileStorage__objects = {}
        self.assertEqual(storage.all(), {})
        storage.reload()
        alldic = storage.all()
        cl = [b, u, c, a, p, r, s]
        cln = ['b', 'u', 'c', 'a', 'p', 'r', 's']
        for i, j in zip(cl, cln):
            key = "key" + j
            self.assertFalse(i == alldic[eval(key)])
            self.assertEqual(i.id, alldic[eval(key)].id)
            self.assertEqual(i.__class__, alldic[eval(key)].__class__)
