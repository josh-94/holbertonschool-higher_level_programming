#!/usr/bin/python3
"""
First Square
Class Square that inherits from Rectangle
"""
from unittest import skip
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of data"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Validation must inherit from Rectangle"""
        self.width = value
        self.height = value

    def __str__(self):
        square = "[Square] ({}) {}/{} - {}"
        square = square.format(self.id, self.x, self.y, self.width)
        return square

    def update(self, *args, **kwargs):
        """Assign attributes"""
        keys = ["id", "size", "x", "y"]

        if len(args) > 0:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """dictionary"""
        list_square = ["id", "size", "x", "y"]
        value_square = (self.id, self.size, self.x, self.y)
        return dict(zip(list_square, value_square))
