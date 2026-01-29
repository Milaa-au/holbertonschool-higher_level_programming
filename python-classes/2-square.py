#!/usr/bin/python3
"""It is a class named Square that defines a square."""


class Square:
    """
    The __init__ method initializes a new instance of the Square class.
    It takes one optional parameter, size, which represents t
    he length of the sides of the square and defaults to 0.

    The method checks that size is an
    integer and raises a TypeError if it is not.
    It also verifies that size is not
    negative and raises a TypeError if the value is less than 0.
    If all checks pass, the value of size is
    stored as a private instance attribute.
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
