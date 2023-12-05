#!/usr/bin/python3
"""
This is the module containing the BaseModel class.
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for common attributes/methods.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Attributes:
        - id (string): Assigns a unique UUID when an instance is created.
        - created_at (datetime): Assigns current datetime instance is created.
        - updated_at (datetime): Assigns current datetime an instance is
                created and updates every time the object is changed.
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, form))
                else:
                    setattr(self, key, value)


    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, str(self.__dict__)
        )

    def save(self):
        """
        Updates public instance attribute updated_at with current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
        - Dictionary containing all keys/values of __dict__ of the instance.
        - A key '__class__' with the class name of the object.
        - 'created_at' and 'updated_at' converted to ISO format string object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__

        return obj_dict
