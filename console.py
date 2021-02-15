#!/usr/local/bin/python3
"""module console"""
import cmd
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
# list of valid models
models_dict = {"BaseModel": BaseModel,
               "User": User, "State": State, "City": City,
               "Amenity": Amenity, "Place": Place, "Review": Review}
# List of attributes prohibited for updating
no_update = ["id", "created_at", "updated_at"]


class HBNBCommand(cmd.Cmd):
    """Command line console

    Class attributes
        prompt (str) = CML prompt
        doc_header (str) = header for documented methods
        undoc_header (str) = header for undocumented methods
        misc_header (str) = header for misc messages
        ruler (str) = separator for headers

    Methods
        do_create()
        do_show()
        do_destroy()
        do_all()
        do_update()
        emptyline()
        do_quit()
        do_EOF()

    Static methods
        check_class()
        check_id()
        check_attribute()
        get_arguments(list_arg)
    """
    prompt = "(hbnb)"
    doc_header = "Documented commands (type `help <commad>` for more info):"
    misc_header = "hbnb console"
    undoc_header = "Undocumented commands:"
    ruler = "-"

    # methods
    def precmd(self, line):
        """Modify line if command has the following sintax:

<class name>.<command([arguments])>
"""
        line_list = line.split(".")
        class_name = str(line_list[0])
        if len(line_list) > 1:
            last_idx = line_list[1].index("(")
            command = line_list[1][:last_idx]
            first_idx = line.index("(") + 1
            arguments = self.get_arguments(line[first_idx:-1])
            line = command+" "+class_name+" "+arguments
        return line

    def do_create(self, line):
        """Creates a new instance of a model

Ussage: create <class name>
        """
        if self.check_class(line) is False:
            return
        line = line.split()
        new_model = models_dict[line[0]]()
        storage.save()
        print(new_model.id)

    def do_count(self, line):
        """Return number of istances of a class

Ussage: count <class name>
Ussage [optional]: <class name>.all()
        """
        line = line.split()
        count = 0
        for key in storage.all().keys():
            key = key.split(".")
            if key[0] == line[0]:
                count += 1
        print(count)

    def do_show(self, line):
        """Prints the string representation of
an instance based on the class name

Ussage: show <class name> <id>
        """
        if self.check_class(line) is False:
            return
        if self.check_id(line) is False:
            return
        line = line.split()
        my_key = line[0]+"."+line[1]
        objects = storage.all()
        if my_key in objects.keys():
            print(objects[my_key])

    def do_destroy(self, line):
        """Deletes an instance based on the
classname and id

Ussage: destroy <class name> <id>
        """
        if self.check_class(line) is False:
            return
        if self.check_id(line) is False:
            return
        line = line.split()
        my_key = line[0]+"."+line[1]
        objects = storage.all()
        if my_key in objects.keys():
            objects.pop(my_key)
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all
instances based or not on the class name

Ussage: all <class name>
Ussage [optional]: <class name>.all()
        """
        objects = storage.all()
        my_objects = list()
        for key in objects:
            my_objects.append(str(objects[key]))
        if line == "":
            print(my_objects)
        else:
            if self.check_class(line) is False:
                return
            line = line.split()
            filtered_list = list()
            for obj_str in my_objects:
                last_idx = obj_str.index("]")
                class_name = obj_str[1:last_idx]
                if class_name == line[0]:
                    filtered_list.append(obj_str)
            print(filtered_list)

    def do_update(self, line):
        """Updates an instance based on the class name
and id by adding or updating attribute

Ussage: update <class name> <id> <attribute name> '<attribute value>'
        """
        if self.check_class(line) is False:
            return
        if self.check_id(line) is False:
            return
        if self.check_attribute(line) is False:
            return
        line = shlex.split(line)
        attribute = line[2]
        value = line[3]
        if attribute not in no_update:
            objects = storage.all()
            my_key = line[0]+"."+line[1]
            if hasattr(objects[my_key], attribute):
                if type(getattr(objects[my_key], attribute)) is int:
                    value = int(value)
                elif type(getattr(objects[my_key], attribute)) is float:
                    value = float(value)
                if type(getattr(objects[my_key], attribute)) is list:
                    attributes_list = getattr(objects[my_key], attribute)
                    attributes_list.append(value)
                    value = attributes_list
            setattr(objects[my_key], attribute, value)
            objects[my_key].save()

    # Manage exit and empty commands methods
    def emptyline(self):
        """Override default behavior when empty line + ENTER
        is typed by doing nothing
        """
        pass

    def do_quit(self, line):
        """Exit the console

Ussage: quit
        """
        return True

    def do_EOF(self, line):
        """"Exit the console

Ussage: EOF
Ussage [optional]: ctrl + D
        """
        return True

    def postloop(self):
        """print new line when at console exit"""
        print()

    # static methods
    @staticmethod
    def check_class(line):
        """Check if class name is valid in Data Base"""
        if line == "":
            print("** class name missing **")
            return False
        line = line.split()
        if line[0] not in models_dict.keys():
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def check_id(line):
        """Check if id is valid in Data Base"""
        line = line.split()
        if len(line) < 2:
            print("** instance id missing **")
            return False
        else:
            my_key = line[0]+"."+line[1]
            objects = storage.all()
            if my_key not in objects.keys():
                print("** no instance found **")
                return False
        return True

    @staticmethod
    def check_attribute(line):
        """Check if attribute and value arguments are present"""
        line = line.split()
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True

    @staticmethod
    def get_arguments(line):
        """Check if in a list there are arguments to be retrieved.
The argumentes are parse using as limits the `()`chars"""

        arg_str = ""
        if line != "":
            arg = shlex.split(line)
            for idx, item in enumerate(arg):
                if idx < 3:
                    try:
                        temp_idx = item.rindex(",")
                    except Exception:
                        temp_idx = len(item)
                    if idx == 0:
                        arg_str += item[:temp_idx]
                    elif idx == 1:
                        arg_str += " "+item[:temp_idx]
                    else:
                        arg_str += " "+"\""+item[:temp_idx]+"\""
        return arg_str


if __name__ == "__main__":
    # call class and cmdloop() method to start the commmand line
    console = HBNBCommand()
    console.cmdloop()
