#!/usr/bin/python3
"""
Définit une fonction qui retourne
le dictionnaire descriptif d'un objet.
"""


def class_to_json(obj):
    """Retourner le dictionnaire des attributs d'un objet."""
    return obj.__dict__
