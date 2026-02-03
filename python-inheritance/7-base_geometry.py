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