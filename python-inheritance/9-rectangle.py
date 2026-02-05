#!/usr/bin/python3
"""
Définition de classes de géométrie.

Ce module contient la classe BaseGeometry et une classe Rectangle
qui hérite de BaseGeometry.
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.
    """

    def area(self):
        """
        Méthode non implémentée.

        Doit être redéfinie dans les classes filles.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que la valeur est un entier strictement positif.

        Args:
            name (str): nom du paramètre
            value (int): valeur à valider

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est inférieur ou égal à 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (int): largeur du rectangle
            height (int): hauteur du rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne une représentation lisible du rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
