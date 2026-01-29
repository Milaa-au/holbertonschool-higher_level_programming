#!/usr/bin/python3
"""This class defines a square."""


class Square:

    """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square's sides. Must be an integer
                        greater than or equal to 0.
            position (tuple): A tuple of two positive integers representing
                              the position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        Retrieves the position of the square.

        Returns:
            tuple: A tuple of two positive integers representing the position.
    """
    @property
    def position(self):
        return self.__position

    """
        Sets the position of the square.

        Args:
            value (tuple): A tuple of two positive integers.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
    """
    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

    """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
    """
    def area(self):
        return self.__size ** 2

    """
        Prints the square using the character '#', taking into account
        the position of the square.

        If the size of the square is 0, an empty line is printed.
    """
    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
