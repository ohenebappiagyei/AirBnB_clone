#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
from os.path import exists
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a json file and deserializes json file
    to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets ___objects with key"""
        if not obj:
            return
        attr = obj.to_dict()
        key = attr['__class__'] + '.' + attr['id']
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to json file"""
        objs = {}
        for key in self.__objects:
            objs[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(objs, f, indent=4)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
