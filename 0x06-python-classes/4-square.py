#!/usr/bin/python3

# 0-square.py by Kwabena Boakye
"""This class is a blueprint for making square instances."""


class Square:
    """Defines a square"""

    def __init__(self, size=0) -> None:
        """Initializes a square and validates it
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self) -> int:
        """Returns size of squares"""
        return self.__size

    @size.setter
    def size(self, value) -> None:
        """Sets size of square to a different value, `value`
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """Calculates the area of the square using size"""
        return self.__size ** 2
