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

    def area(self) -> int:
        """Calculates the area of the square using size"""
        return self.__size ** 2
