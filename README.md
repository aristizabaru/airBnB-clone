# 0x00. AirBnB clone - The console

---

![Logo AirBnb](https://i.ibb.co/BT08MTv/65f4a1dd9c51265f49d0.png)

---

## Overview

---

The goal of the project is to deploy on your server a simple copy of the AirBnB website.
Some of the functions that will cover the fundamental concepts will be implemented of the higher level programming track.
Al final se obtendra una aplicacion web completa compuesta por:

-  A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-  A website (the front-end) that shows the final product to everybody: static and dynamic
-  A database or files that store data (data = objects)
-  An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them

In this project we will do the first part.

---

# The console

---

-  create your data model
-  manage (create, update, destroy, etc) objects via a console / command interpreter
-  store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.

This means: from your console code (the command interpreter itself)

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine
![](https://i.ibb.co/Qk2QD5S/815046647d23428a14ca.png)

---

### target of command interpreter

---

-  Create and save a new object.(Example: New User, ew place, new atrribute, etc)
-  Read Objects created from a json file
-  Interact and modify the object (show, count, modify, etc)
-  Update object attributes
-  Destroy an object

---

## Table of Content

---

-  [Environment](#environment)
-  [Installation](#installation)
-  [File Descriptions](#file-descriptions)
-  [Usage](#usage)
-  [Examples of use](#examples)
-  [Bugs](#bugs)
-  [Authors](#authors)
-  [License](#license)

---

## Environment

---

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

---

## Installation

---

-  Clone this repository: `git clone "https://github.com/aristizabaru/AirBnB_clone.git"`
-  Run **interactive** mode: `(./console.py)`

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```

-  Run **non interactive** mode: `echo "<command>" | ./console.py`

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

---

## File Descriptions

---

[console.py](console.py): Contains the entry point of the command interpreter. The commands accepted by the console are:

-  `create`: Creates a new instance of a model.
   -  Ussage: `create <class name>`
   -  Ussage [optional]: `<class name>.create()`
-  `count`: Return number of istances of a class.
   -  Ussage: `count <class name>`
   -  Ussage [optional]: `<class name>.count()`
-  `show`: Prints the string representation of an instance based on the class name.
   -  Ussage: `show <class name> <id>`
   -  Ussage [optional]: `<class name>.show(<id>)`
-  `destroy`: Deletes an instance based on the classname and id.
   -  Ussage: `destroy <class name> <id>`
   -  Ussage [optional]: `<class name>.destroy(<id>)`
-  `all`: Prints all string representation of all instances based or not on the class name.
   -  Ussage: `all <class name>`
   -  Ussage: [optional]: `<class name>.all()`
-  `update`: Updates an instance based on the class name and id by adding or updating attribute. (save the change into the JSON file).
   -  Ussage: `update <class name> <id> <attribute name> '<attribute value>'`
   -  Ussage: [optional]: `<class name>.update(<id>, <attribute name>, <attribute value>)`
-  `quit`: Exit the console.
   -  Ussage: `quit`
-  `EOF`: "Exit the console.
   -  Ussage: `EOF`
   -  Ussage: `[optional]: ctrl + D`

#### `models/` ---> Directory that contains main classes:

[base_model.py](/models/base_model.py): The class BaseModel is the main class that defines all common attributes/methods for other classes.

**Methods inside this class:**

-  `def __init__(self, *args, **kwargs)`: Constructor for BaseModel.
-  `def save(self)`: Saves current time to updated_at attribute.
-  `def to_dict(self)`: Return a dicctionary all the attributres keys/values.
-  `def __str__(self)`: return readable object with format `[<class name>] (<self.id>) <self.__dict__`.

**Classes inherited from Base Model:**

-  [amenity.py](/models/amenity.py): Creates Amenity intances.
   -  Public class attributes:
      -  **name**: string - empty string
-  [city.py](/models/city.py): Creates City intances.
   -  Public class attributes:
      -  **state_id**: string - empty string: it will be the State.id
      -  **name**: string - empty string
-  [place.py](/models/place.py): Creates Place intances.
   -  **city_id:** string - empty string: it will be the City.id
      -  **user_id:** string - empty string: it will be the User.id
      -  **name:** string - empty string
      -  **description:** string - empty string
      -  **number_rooms:** integer - 0
      -  **number_bathrooms:** integer - 0
      -  **max_guest:** integer - 0
      -  **price_by_night:** integer - 0
      -  **latitude**: float - 0.0
      -  **longitude**: float - 0.0
      -  **amenity_ids**: list of string - empty list: it will be the list of Amenity.id later
-  [review.py](/models/review.py): Creates Review intances.
   -  Public class attributes:
      -  **place_id:** string - empty string: it will be the Place.id
      -  **user_id:** string - empty string: it will be the User.id
      -  **text:** string - empty string
-  [state.py](/models/state.py): Creates State intances.
   -  Public class attributes: - **name:** will be the name of teh state to
-  [user.py](/models/user.py): Creates User intances.

#### `/models/engine` ---> Directory that contains File Storage class that manages JSON serialization and deserialization:

[file_storage.py](/models/engine/file_storage.py): The class FileStorage serializes instances to a JSON file and deserializes JSON file to instances.

-  `def all(self)`: Returns the dictionary \_\_objects
-  `def new(self, obj)`: Sets in \_\_objects the obj with key <obj class name>.id
-  `def save(self)`: Serializes **objects to the JSON file (path: **file_path)
-  ` def reload(self)`: Deserializes the JSON file to \_\_objects

#### `/tests` ---> Directory contains all unit test cases for this project:

[/test_models/test_base_model.py](/tests/test_models/test_base_model.py): Contains the TestBaseModel and TestBaseModelDocs classes

---

## Examples

---

`mode interactive`
`help`

```
KLICH84->/...->/AirBnB_clone/$ ./console.py
(hbnb) help

Documented commands (type `help <commad>` for more info):
---------------------------------------------------------
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help all
Prints all string representation of all
instances based or not on the class name
Ussage: all <class name>
Ussage [optional]: <class name>.all()

(hbnb)
```

`create and all`

```
KLICH84->/...->/AirBnB_clone/$ ./console.py
(hbnb) comandinvalid
*** Unknown syntax: comandinvalid
(hbnb) create classIncalid
** class doesn't exist **
(hbnb) create BaseModel
a38dec44-75e1-414d-8f6b-d8d9aa030ad2
(hbnb) BaseModel.create()
ef9d643e-578c-4f6e-9527-9037570abce0
(hbnb) all
["[BaseModel] (a38dec44-75e1-414d-8f6b-d8d9aa030ad2) {'id': 'a38dec44-75e1-414d-8f6b-d8d9aa030ad2', 'created_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536), 'updated_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536)}", "[BaseModel] (ef9d643e-578c-4f6e-9527-9037570abce0) {'id': 'ef9d643e-578c-4f6e-9527-9037570abce0', 'created_at': datetime.datetime(2021, 2, 17, 20, 28, 30, 695839), 'updated_at': datetime.datetime(2021, 2, 17, 20, 28, 30, 695839)}"]
(hbnb) EOF
```

`count`

```
KLICH84->/...->/AirBnB_clone/$ ./console.py
(hbnb) count User
0
(hbnb) count BaseModel
2
(hbnb) BaseModel.count()
2
(hbnb) all
["[BaseModel] (a38dec44-75e1-414d-8f6b-d8d9aa030ad2) {'id': 'a38dec44-75e1-414d-8f6b-d8d9aa030ad2', 'created_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536), 'updated_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536)}", "[BaseModel] (ef9d643e-578c-4f6e-9527-9037570abce0) {'id': 'ef9d643e-578c-4f6e-9527-9037570abce0', 'created_at': datetime.datetime(2021, 2, 17, 20, 28, 30, 695839), 'updated_at': datetime.datetime(2021, 2, 17, 20, 28, 30, 695839)}"]
(hbnb) quit
```

`show`

```
KLICH84->/...->/AirBnB_clone/$ ./console.py
(hbnb) show
** class name missing **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel a38dec44-75e1-414d-8f6b-d8d9aa030ad2
[BaseModel] (a38dec44-75e1-414d-8f6b-d8d9aa030ad2) {'id': 'a38dec44-75e1-414d-8f6b-d8d9aa030ad2', 'created_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536), 'updated_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536)}
(hbnb) BaseModel.show(a38dec44-75e1-414d-8f6b-d8d9aa030ad2)
[BaseModel] (a38dec44-75e1-414d-8f6b-d8d9aa030ad2) {'id': 'a38dec44-75e1-414d-8f6b-d8d9aa030ad2', 'created_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536), 'updated_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536)}
(hbnb) all
["[BaseModel] (a38dec44-75e1-414d-8f6b-d8d9aa030ad2) {'id': 'a38dec44-75e1-414d-8f6b-d8d9aa030ad2', 'created_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536), 'updated_at': datetime.datetime(2021, 2, 17, 20, 27, 10, 707536)}", "[BaseModel] (ef9d643e-578c-4f6e-9527-9037570abce0) {'id': 'ef9d643e-578c-4f6e-9527-9037570abce0', 'created_at': datetime.datetime(2021, 2, 17, 20, 28, 30, 695839), 'updated_at': datetime.datetime(2021, 2, 17, 20, 28, 30, 695839)}"]
(hbnb)
```

`mode non-interactive`

```
KLICH84->/...->/AirBnB_clone/$ echo "help" | ./console.py
(hbnb)
Documented commands (type `help <commad>` for more info):
---------------------------------------------------------
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

```
KLICH84->/...->/AirBnB_clone/$ echo "help create" | ./console.py
(hbnb) Creates a new instance of a model
Ussage: create <class name>

(hbnb)
KLICH84->/...->/AirBnB_clone/$ echo create User | ./console.py
(hbnb) 3083236a-c1e3-4689-8626-9182a9493f5c
(hbnb)
KLICH84->/...->/AirBnB_clone/$ echo "count User" | ./console.py
(hbnb) 3
(hbnb)
KLICH84->/...->/AirBnB_clone/$ echo "all User" | ./console.py
(hbnb) ["[User] (6b4053db-f35e-4bb0-8b85-ec7e67e1f50a) {'id': '6b4053db-f35e-4bb0-8b85-ec7e67e1f50a', 'created_at': datetime.datetime(2021, 2, 15, 21, 35, 23, 92533), 'updated_at': datetime.datetime(2021, 2, 15, 21, 37, 35, 717612), 'email': 'matias@gmailco', 'password': '12345', 'first_name': 'Orrego'}", "[User] (31a7dc8c-782d-46bb-b71a-840fd5089d25) {'id': '31a7dc8c-782d-46bb-b71a-840fd5089d25', 'created_at': datetime.datetime(2021, 2, 15, 21, 53, 29, 148435), 'updated_at': datetime.datetime(2021, 2, 15, 21, 53, 29, 148435)}", "[User] (3083236a-c1e3-4689-8626-9182a9493f5c) {'id': '3083236a-c1e3-4689-8626-9182a9493f5c', 'created_at': datetime.datetime(2021, 2, 15, 21, 54, 44, 927164), 'updated_at': datetime.datetime(2021, 2, 15, 21, 54, 44, 927164)}", "[User] (6ae55233-5738-434e-960b-0a17f5326ff2) {'id': '6ae55233-5738-434e-960b-0a17f5326ff2', 'created_at': datetime.datetime(2021, 2, 15, 21, 57, 6, 616332), 'updated_at': datetime.datetime(2021, 2, 15, 21, 57, 6, 616332)}"]
```

---

## Bugs

There was not found bugs, if you find one, contact to the Authors.

---

## Authors

Carlso Andres Ariztisabal - [Github](https://github.com/aristizabaru) / [Twitter](https://twitter.com/aristizabaru)  
Carlos Alberto Usuga Martinez - [Github](https://github.com/klich1984) / [Twitter](https://twitter.com/usuga_martinez)

---

## License

Public Domain. No copy write protection.
