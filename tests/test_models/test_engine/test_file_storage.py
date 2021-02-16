#!/usr/bin/python3
"""test_file_storage module """
import unittest
import pep8
import models.engine.file_storage as engine


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

    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = engine.FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        # Take name of private attribute from __dict__
        self.assertIs(new_dict, storage._FileStorage__objects)
