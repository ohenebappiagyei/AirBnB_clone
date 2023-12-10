#!/usr/bin/python3
"""Defines a user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor for User class."""
        super().__init__(*args, **kwargs)
