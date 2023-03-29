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
            and len(position) != 3
            and any(x < 0 for x in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self) -> tuple:
        return self.__position

    def my_print(self):
        """Prints the square in position"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()

    def area(self) -> int:
        """Calculates the area of the square using size"""
        return self.__size ** 2
