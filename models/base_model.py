#!/usr/bin/python3
"""base_model module

Classes
    BaseModel
"""
import uuid
from datetime import datetime
import models

_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Class for BaseModel objects

    Attributes
        id (string): Universal unique identifier
        created_at(datatime): creation time
        updated_at(datatime): update time

    Methods
        __init__(*args, **kwargs)
        save()
        to_dict()
        __str__()
    """

    # constructor
    def __init__(self, *args, **kwargs):
        """constructor for BaseModel

        Arguments
            *args: values for each attribute of BaseModel
            **kwargs: key/value for each attribute of BaseModel
        """
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(
                            kwargs[key], _format))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    # methods
    def save(self):
        """saves current time to updated_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dicctionary all the attributres keys/values"""
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict

    # magic methods
    def __str__(self):
        """return readable object with format
        [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
