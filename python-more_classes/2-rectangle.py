#!/usr/bin/python3
"""It is an empty class named Rectangle."""


class Rectangle:
    """This class defines a rectangle."""

    """Retrieves the width of the rectangle."""
    @property
    def width(self):
        return self.__width

    """Sets the width of the rectangle."""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """Retrieves the height of the rectangle."""
    @property
    def height(self):
        return self.__height

    """Sets the height of the rectangle."""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Initializes a Rectangle instance with width and height."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """
    Calculates and returns the area of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    def area(self):
        return self.__height * self.__width

    """
    Calculates and returns the perimeter of the rectangle.

    Returns:
        int: The perimeter of the rectangle.
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
