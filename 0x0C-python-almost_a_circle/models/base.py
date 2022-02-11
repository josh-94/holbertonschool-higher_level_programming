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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
        list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    # def save_to_file(cls, list_objs):

    @staticmethod
    def from_json_string(json_string):
        """return list of the JSON"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
