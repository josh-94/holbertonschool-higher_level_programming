#!/usr/bin/python3
"""Class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            q = {}
            for a in attrs:
                if a in self.__dict__:
                    q[a] = self.__dict__[a]
                    return q
        return self.__dict__
