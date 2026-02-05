#!/usr/bin/python3
"""
Fonction qui renvoie True ou False selon que l'objet
est une instance d'une classe qui hérite de la classe donnée
(mais pas une instance directe de cette classe).
"""


def inherits_from(obj, a_class):
    """
    Vérifie si l'objet est une instance d'une classe
    qui hérite de a_class, sans être une instance directe
    de a_class.

    Args:
        obj: l'objet à tester
        a_class: la classe de référence

    Returns:
        True si obj hérite de a_class, sinon False
    """

    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
