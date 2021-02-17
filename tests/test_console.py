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


class Test_destroy(unittest.TestCase):
    def test_destroy_invalid_class(self):
        """  Test for destroy with invalid class """
        msg = "** class doesn't exist **\n"

        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            st = f.getvalue()
            self.assertEqual(msg, st)
