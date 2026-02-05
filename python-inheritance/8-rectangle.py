#!/usr/bin/python3
"""
Defines a class Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    based on 7-base_geometry.
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height.
        width and height must be private. No getter or setter.
        width and height must be positive integers,
            validated by integer_validator.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
