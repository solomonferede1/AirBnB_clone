#!/usr/bin/python3
"""
============================================
Module for serialization/deserealization JSON
============================================
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class FileStorage:
    """class for serialization/deserealization JSON"""

    def __init__(self):
        """the constructor"""

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns all objects storage in the file"""
        return self.__objects

    def new(self, obj):
        """sets a new object"""

        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """serialize objects in json file"""

        my_dict = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            for k, v in self.__objects.items():
                my_dict[k] = v.to_dict()
            f.write(json.dumps(my_dict))

    def reload(self):
        """ deserializes the JSON file to __objects, if path exists or do
        nothing. no exceptions should raise """

        obj_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                    "State": State, "City": City, "Amenity": Amenity,
                    "Review": Review}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                x = json.loads(f.read())
                for k, v in x.items():
                    self.__objects[k] = obj_dict[v["__class__"]](**v)
