#!/usr/bin/python3
"""Class inherent"""


Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Class"""

def __init__(self, size):
    self.__size = size
    self.integer_validator("size", size)

def area(self)
"""area rectangle"""
return self.__size * self.__size
