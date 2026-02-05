#!/usr/bin/python3
"""
Fonction qui renvoie True ou False selon que l'objet
est une instance de la classe donnée.
"""

def is_kind_of_class(obj, a_class):
    """
    Vérifie si l'objet est une instance de la classe spécifiée.

    Args:
        obj: l'objet à tester
        a_class: la classe à comparer

    Returns:
        True si obj est une instance de a_class, sinon False
    """
    return(isinstance(obj, a_class))