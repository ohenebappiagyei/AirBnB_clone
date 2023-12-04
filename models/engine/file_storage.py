#!/usr/bin/python3
"""Defines a FileStorage class"""
import json
from os.path import exists


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if exists(FileStorage.__file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                cls = globals()[class_name]
                obj = cls(**value)
                FileStorage.__objects[key] = obj
