#!/usr/bin/python3
"""A City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """A class for City objects"""
    state_id: str = ""
    name: str = ""
