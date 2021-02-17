#!/usr/bin/python3
"""test_console module """
import unittest
import pep8
import io
from console import HBNBCommand
from os import path, remove
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from models import storage


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

    def tearDown(self):
        """Tear down for all methods"""
        try:
            remove("file.json")
        except:
            pass

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


class TestCreateCommand(unittest.TestCase):
    """Test create command"""

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        # Boot __objects private attribute
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down for all methods"""
        try:
            remove("file.json")
        except:
            pass

    def test_create_no_class(self):
        """Test for create with class missing"""
        message = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("create")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_create_invalid_class(self):
        """Test for create with invalid class"""
        message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("create MyModel")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_create_valid_class(self):
        """Test for create with existing id"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for id_class in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("create " + id_class)
                id_st = fd.getvalue()
                alldic = storage.all()
                self.assertTrue((id_class + '.' + id_st[:-1]) in alldic.keys())
        self.assertEqual(len(alldic), len(classes))


class TestDestroyCommand(unittest.TestCase):
    """Test destroy command"""

    def setUp(self):
        """ Set up for all methods """
        try:
            remove("file.json")
        except:
            pass
        # Boot __objects private attribute
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down for all methods"""
        try:
            remove("file.json")
        except:
            pass

    def test_destroy_no_class(self):
        """Test for destroy with class missing"""
        message = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("destroy")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_new_destroy_no_class(self):
        """Test for destroy with class missing by second method """
        message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            pre_cmd = HBNBCommand().precmd("MyModel.destroy()")
            HBNBCommand().onecmd(pre_cmd)
            stdout = fd.getvalue()
            if stdout[0] == "\n":
                message = "\n" + message
            self.assertEqual(message, stdout)

    def test_destroy_invalid_class(self):
        """Test for destroy with invalid class"""
        message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("destroy MyModel")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_destroy_no_id(self):
        """Test for destroy with id missing"""
        message = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("destroy " + i)
                stdout = fd.getvalue()
                self.assertEqual(message, stdout)

    def test_new_destroy_no_id(self):
        """Test for destroy with id missing"""
        message = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                pre_cmd = HBNBCommand().precmd(i + ".destroy()")
                HBNBCommand().onecmd(pre_cmd)
                stdout = fd.getvalue()
                if stdout[0] == "\n":
                    message = "\n" + message
                self.assertEqual(message, stdout)

    def test_destroy_no_existent_id(self):
        """Test for destroy with non-existent id"""
        message = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("destroy " + i + " 123")
                stdout = fd.getvalue()
                self.assertEqual(message, stdout)

    def test_new_destroy_no_existent_id(self):
        """  Test for destroy with non-existent id """
        message = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                pre_cmd = HBNBCommand().precmd(i + ".destroy(123)")
                HBNBCommand().onecmd(pre_cmd)
                stdout = fd.getvalue()
                if stdout[0] == "\n":
                    message = "\n" + message
                self.assertEqual(message, stdout)

    def test_destroy_valid_class(self):
        """Test for destroy with existing id"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        lencl = len(classes)
        id_cl = []
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("create " + i)
                id_st = fd.getvalue()
                id_cl.append(id_st)
                alldic = storage.all()
                self.assertTrue((i + '.' + id_st[:-1]) in alldic.keys())
        self.assertEqual(len(alldic), lencl)
        for i, j in zip(classes, id_cl):
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("destroy " + i + " " + j)
                alldic = storage.all()
                self.assertFalse((i + '.' + id_st[:-1]) in alldic.keys())
                lencl -= 1
                self.assertEqual(len(alldic), lencl)


class TestShowCommand(unittest.TestCase):
    """Test show command"""

    def setUp(self):
        """Set up for all methods"""
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down for all methods"""
        try:
            remove("file.json")
        except:
            pass

    def test_show_no_arg(self):
        """Test for show with no command"""
        message = "** class name missing **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("show")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_show_no_exist_class(self):
        """Test for show non-existent class"""
        message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("show MyModel")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)

    def test_new_show_no_exist_class(self):
        """Test for show non-existent class"""
        message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            pre_cmd = HBNBCommand().precmd("MyModel.show()")
            HBNBCommand().onecmd(pre_cmd)
            stdout = fd.getvalue()
            if stdout[0] == "\n":
                message = "\n" + message
            self.assertEqual(message, stdout)

    def test_show_no_id(self):
        """Test for show with id missing"""
        message = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("show " + i)
                stdout = fd.getvalue()
                self.assertEqual(message, stdout)

    def test_new_show_no_id(self):
        """Test for show with id missing"""
        message = "** instance id missing **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                pre_cmd = HBNBCommand().precmd(i + ".show()")
                HBNBCommand().onecmd(pre_cmd)
                stdout = fd.getvalue()
                if stdout[0] == "\n":
                    message = "\n" + message
                self.assertEqual(message, stdout)

    def test_show_no_existent_id(self):
        """Test for show with non-existent id"""
        message = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("show " + i + " 123")
                stdout = fd.getvalue()
                self.assertEqual(message, stdout)

    def test_new_show_no_existent_id(self):
        """  Test for show with non-existent id """
        message = "** no instance found **\n"
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                pre_cmd = HBNBCommand().precmd(i + ".show(123)")
                HBNBCommand().onecmd(pre_cmd)
                stdout = fd.getvalue()
                if stdout[0] == "\n":
                    message = "\n" + message
                self.assertEqual(message, stdout)

    def test_show_existing_id(self):
        """Test for show with existing id"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("create " + i)
                id_st = fd.getvalue()
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("show " + i + " " + id_st)
                stdout = fd.getvalue()
                alldic = storage.all()
                objst = str(alldic[i + '.' + id_st[:-1]])
                self.assertEqual(stdout[:-1], objst)

    def test_show_show_existing_id(self):
        """Test for show with existing id"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("create " + i)
                id_st = fd.getvalue()
            with patch('sys.stdout', new=io.StringIO()) as fd:
                pre_cmd = HBNBCommand().precmd(i + ".show(\"" + id_st + "\")")
                HBNBCommand().onecmd(pre_cmd)
                stdout = fd.getvalue()
                alldic = storage.all()
                objst = str(alldic[i + '.' + id_st[:-1]])
                self.assertEqual(stdout[:-1], objst)


class TestAll(unittest.TestCase):
    """Test all command"""

    def setUp(self):
        """Set up for all methods"""
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down for all methods"""
        try:
            remove("file.json")
        except:
            pass

    def test_update_no_existent_class(self):
        """Test for all with no existent class"""
        message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("all MyModel")
            st = fd.getvalue()
            self.assertEqual(message, st)

    def test_new_update_no_existent_class(self):
        """Test for all with no existent class"""
        message = "** class doesn't exist **\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            pre_cmd = HBNBCommand().precmd("MyModel.all()")
            HBNBCommand().onecmd(pre_cmd)
            stdout = fd.getvalue()
            if stdout[0] == "\n":
                message = "\n" + message
            self.assertEqual(message, stdout)

    def test_empty(self):
        """Tests for empty storage"""
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        message = "[]\n"
        with patch('sys.stdout', new=io.StringIO()) as fd:
            HBNBCommand().onecmd("all")
            stdout = fd.getvalue()
            self.assertEqual(message, stdout)
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as fd:
                HBNBCommand().onecmd("all " + i)
                stdout = fd.getvalue()
                self.assertEqual(message, stdout)

    def test_all_classes(self):
        """ Tests All command for classes_double """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]
        classes += classes
        for i in classes:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create " + i)
                st = f.getvalue()
            alldic = storage.all()
            all_cl = []
            all_full = []
            for j in alldic.keys():
                all_full.append(str(alldic[j]))
                if i in j:
                    all_cl.append(str(alldic[j]))
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("all " + i)
                st = f.getvalue()
                self.assertEqual(str(all_cl) + "\n", st)
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("all")
                st = f.getvalue()
                self.assertEqual(str(all_full) + "\n", st)
