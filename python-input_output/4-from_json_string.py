#!/usr/bin/python3
"""
Définit une fonction qui
convertit une chaîne JSON en objet Python.
"""


def from_json_string(my_str):
    """Convertir une chaîne JSON en objet Python."""
    return json.loads(my_str)
