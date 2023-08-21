#!/usr/bin/env python3

"""
A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicate the same code.

"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """
        ...
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
