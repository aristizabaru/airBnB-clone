#!/usr/bin/python3
"""test_console module """
import unittest
import pep8
import io
from console import HBNBCommand
from os import path, remove
from unittest.mock import patch
from models.engine.file_storage import FileStorage


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestInvalidCommand(unittest.TestCase):
    """Test output of an non existing command"""

    def test_unknown(self):
        """Test command that doesn't exist"""
        message = "*** Unknown syntax: kreate\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("kreate")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)


class TestHelpCommand(unittest.TestCase):
    """Test help command"""

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        # Boot __objects private attribute
        FileStorage._FileStorage__objects = {}

    def test_help_help(self):
        """Test <help> <help>"""
        message = "List available commands with \"help\" or " \
            "detailed help with \"help cmd\".\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help help")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_quit(self):
        """Test <help> <quit>"""
        message = "Exit the console\n\nUssage: quit\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help quit")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_EOF(self):
        """Test <help> <EOF>"""
        message = "Exit the console\n\nUssage: EOF\n" \
            "Ussage [optional]: ctrl + D\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help EOF")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_create(self):
        """Test <help> <create>"""
        message = "Creates a new instance of a model\n\n" \
            "Ussage: create <class name>\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help create")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_show(self):
        """Test <help> <show>"""
        message = "Prints the string representation of\n" \
            "an instance based on the class name\n\nUssage: " \
            "show <class name> <id>\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help show")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_destroy(self):
        """Test <help> <destroy>"""
        message = "Deletes an instance based on the\nclassname " \
            "and id\n\nUssage: destroy <class name> <id>\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help destroy")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_all(self):
        """Test <help> <all>"""
        message = "Prints all string representation of all\ninstances " \
            "based or not on the class name\n\nUssage: all " \
            "<class name>\nUssage [optional]: " \
            "<class name>.all()\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help all")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_update(self):
        """Test <help> <update>"""
        message = "Updates an instance based on the class name\n" \
            "and id by adding or updating attribute\n\n" \
            "Ussage: update <class name> <id> <attribute name> " \
            "'<attribute value>'\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help update")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_help_count(self):
        """Test <help> <count>"""
        message = "Return number of istances of a class\n\n" \
            "Ussage: count <class name>\n" \
            "Ussage [optional]: <class name>.all()\n        \n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("help count")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)
