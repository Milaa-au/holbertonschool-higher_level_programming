#!/usr/bin/python3
"""This class defines a square."""


class Square:

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides. Must be an integer
                        greater than or equal to 0.
        """
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
