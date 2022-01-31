#!/usr/bin/python3
"""Definition of class"""


class MyList(list):
        """Class MyList inherited"""
        def print_sorted(self):
            """prints sorted list"""
            print(sorted(self))
