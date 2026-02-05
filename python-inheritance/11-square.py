#!/usr/bin/python3
"""
Defines a class Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle (9-rectangle),
    based on 10-square.
    """
    def __init__(self, size):
        """
        Instantiation with size:
        size must be private. No getter or setter.
        size must be a positive integer,
            validated by integer_validator.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the square area.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Square] {self.__size}/{self.__size}"
