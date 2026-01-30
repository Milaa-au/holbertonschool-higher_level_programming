#!/usr/bin/python3
"""
Rectangle class with private width and height,
managed using getters and setters
"""


class Rectangle:
    """
    Defines the Rectangle class with width and height
    """
    def __init__(self, width=0, height=0):
        """
        Creates the rectangle and sets width and height.
        Default values are (0, 0) if not provided.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Modifies the width after validation.
        The value must be a valid integer greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Modifies the height after validation.
        The value must be a valid integer greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        Returns 0 if width or height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result = ""
        for i in range(self.__height):
            result += "#" * self.__width
            if i != self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """
        Returns an official string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Message displayed when the instance (rectangle) is deleted
        """
        print("Bye rectangle...")
