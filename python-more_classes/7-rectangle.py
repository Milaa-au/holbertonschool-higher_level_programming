#!/usr/bin/python3
"""
Rectangle class with private width and height attributes.
Managed using getters and setters.
"""


class Rectangle:
    """
    Represents a rectangle.

    Instance attributes (private):
        width (int): rectangle width
        height (int): rectangle height

    Class attributes:
        number_of_instances (int): number of Rectangle instances
            incremented on each creation and decremented on each deletion
        print_symbol: symbol used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): width of the rectangle (default: 0)
            height (int): height of the rectangle (default: 0)
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle after validation.

        Args:
            value (int): new width value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle after validation.

        Args:
            value (int): new height value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: perimeter of the rectangle, or 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representation of the rectangle using `print_symbol`.

        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = getattr(self, "print_symbol", Rectangle.print_symbol)
        if not isinstance(symbol, str):
            symbol = str(symbol)

        result = []
        for _ in range(self.__height):
            result.append(symbol * self.__width)

        return "\n".join(result)

    def __repr__(self):
        """
        Returns the official string representation of the rectangle.

        This representation can be used to recreate the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when a Rectangle instance is deleted.
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
