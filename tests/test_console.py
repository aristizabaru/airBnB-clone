#!/usr/bin/python3
"""test_console module """
import unittest
import pep8
import io
from unittest.mock import patch
from console import HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestModels(unittest.TestCase):
    def test_create_invalid_class(self):
        """  Test for create with invalid class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_show_invalid_class(self):
        """  Test for show non-existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_all_invalid_class(self):
        """Test for all with invalid class"""
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            pre_cmd = HBNBCommand().precmd("MyModel.all()")
            HBNBCommand().onecmd(pre_cmd)
            st = f.getvalue()
            if st[0] == "\n":
                msg = "\n" + msg
            self.assertEqual(msg, st)

    def test_destroy_invalid_class(self):
        """Test for destroy with invalid class"""
        msg = "** class doesn't exist **\n"

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_all_invalid_class(self):
        """  Test for all with no existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)

    def test_update_invalid_class(self):
        """  Test for update with no existent class """
        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)
