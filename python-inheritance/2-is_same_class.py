#!/usr/bin/python3
"""
Fonction qui renvoie True ou False selon que l'objet
est une instance de la classe donnée.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class,
    otherwise False.
    """
    return type(obj) is a_class
