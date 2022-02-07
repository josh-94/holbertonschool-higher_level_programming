#!/usr/bin/python3
"""Class Base"""


class Base:
    def __init__(self, id=None):
        __nb_objects = 0
        self.id=None
        if  id is not None:
            self.id = id

