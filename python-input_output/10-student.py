#!/usr/bin/python3
"""
Définit une classe Student avec
méthodes pour gérer ses attributs en JSON.
"""


class Student:
    """
    Définit une classe Student avec
    méthodes pour gérer ses attributs en JSON.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire
        des attributs sélectionnés de l'étudiant.

        Args:
            attrs (list, optional): liste
            d'attributs à inclure. Si None,
            retourne tous les attributs.
        """
        obj = self.__dict__.copy()

        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered = {}
            for attr in attrs:
                if attr in obj:  # <-- le if explicite que tu voulais
                    filtered[attr] = obj[attr]
            return filtered
        return obj
