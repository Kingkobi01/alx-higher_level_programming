#!/usr/bin/python3

# 0-square.py by Kwabena Boakye
"""This class is a blueprint for making square instances."""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)) -> None:
        """Initializes a square and validates it
        Args:
            size: represents the size of the square defined
            position: represents the position of the square defined
                    in space
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        if (
            not isinstance(position, tuple)
            or len(position) != 3
            or any(x < 0 for x in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self) -> int:
        """Returns size of square"""
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

    @property
    def position(self) -> tuple:
        """Returns position of square in space"""
        return self.__position

    @position.setter
    def position(self, value) -> None:
        """Sets size of square to a different value, `value`
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0"""
        if not isinstance(value, tuple) or len(value) != 3 or any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def pos_print(self):
        pos = ""
        if self.__size == 0:
            return pos

        for y in range(self.__position[1]):
            pos += "\n"

        for x in range(self.__size):
            for j in range(self.__position[0]):
                pos += " "
            for k in range(self.__size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Prints the square in position"""
        print(self.pos_print())

    def area(self) -> int:
        """Calculates the area of the square using size"""
        return self.__size ** 2
