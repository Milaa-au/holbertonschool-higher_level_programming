#!/usr/bin/python3
"""This class defines a square."""


class Square:
    """
    Initializes a new Square instance.

    Args:
        size (int): The size of the square's sides. Must be an integer
                greater than or equal to 0.
    """
    def __init__(self, size=0):
        self.size = size  # Uses the setter for validation

    """
    Retrieves the size of the square.

    Returns:
        int: The size of the square.
    """
    @property
    def size(self):
        return self.__size

    """
    Sets the size of the square.

    Args:
        value (int): The new size of the square.

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
    Calculates and returns the area of the square.

    Returns:
        int: The area of the square.
    """
    def area(self):
        return self.__size * self.__size
