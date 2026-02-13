#!/usr/bin/python3
"""
Définit une fonction qui
convertit un objet en chaîne JSON.
"""


def to_json_string(my_obj):
    """Convertir un objet en chaîne de caractères."""
    return json.dumps(my_obj)
