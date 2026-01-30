#!/usr/bin/python3
"""
Rectangle class with private width and height attributes
Managed using getters and setters
"""


class Rectangle:
    """
    Represents a rectangle

    Instance attributes (private):
        width: rectangle width
        height: rectangle height

    Class attributes:
        number_of_instances: number of Rectangle instances
            incremented on each creation and decremented on each deletion
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Creates a rectangle and defines its width and height
        Default values are (0, 0)
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width after validation
        The value must be an integer greater than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height after validation
        The value must be an integer greater than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
