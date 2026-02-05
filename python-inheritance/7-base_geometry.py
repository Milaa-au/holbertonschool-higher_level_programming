#!/usr/bin/python3
"""Fonction qui renvoie true ou false en fonction que si 
l'objet est une instance de la class donné."""

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