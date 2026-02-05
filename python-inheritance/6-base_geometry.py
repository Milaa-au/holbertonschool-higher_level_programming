#!/usr/bin/python3
"""
Définition de la classe BaseGeometry.

Cette classe sert de classe de base pour des formes géométriques.
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
