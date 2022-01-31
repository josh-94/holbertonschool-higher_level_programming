#!/usr/bin/python3
"""Function"""
def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object is
    an instance of, or if the object is an instance of a
    class that inherited from, the specified class ;
    otherwise False.
    """
    if a_class == type(obj):
        return False
    return isinstance(obj, a_class)
