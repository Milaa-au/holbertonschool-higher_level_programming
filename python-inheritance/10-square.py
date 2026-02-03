#!/usr/bin/python3
"""Fonction qui renvoie true ou false en fonction que si 
l'objet est une instance de la class donné."""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise TypeError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
    def area(self):
        return self.__height * self.__width
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
    def area(self):
        return self._Rectangle__width * self._Rectangle__height