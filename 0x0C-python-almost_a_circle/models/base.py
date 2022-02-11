#!/usr/bin/python3
"""Class"""


import json
from queue import Empty


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
        list_dictionaries """
        if list_dictionaries is None or Empty:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
