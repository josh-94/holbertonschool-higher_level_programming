#!/usr/bin/python3
"""
First Rectangle
Class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializa the data"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width to a value"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height to a value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Retrieves the x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x to a value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Retrieves the y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y to a value"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Method returns the area rectangule"""
        return self.width * self.height

    def display(self):
        """prints in stdout the
        Rectangle"""
        for j in range(0, self.y):
            print()
        for j in range(0, self.height):
            print(" " * self.x, end='')
            print("#" * self.width)
        # print("\n".join([("#" * self.width)for i in range(0, self.height)]))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        ''' assigns attributes'''
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, (list(self.__dict__.keys()))[i], args[i])
        else:
            for key in kwargs:
                if hasattr(self, key) is True:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """dictionary representation rectangle"""
        list = ["id", "width", "height", "x", "y"]
        value_ID = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(list, value_ID))
