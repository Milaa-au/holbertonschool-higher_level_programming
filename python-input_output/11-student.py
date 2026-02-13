#!/usr/bin/python3
"""
Définit une classe Student avec
méthodes pour gérer ses attributs en JSON.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def to_json(self, attrs=None):
        """
        ok ok
        """
        obj = self.__dict__.copy()

        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered = {}
            for attr in attrs:
                if attr in obj:  # only add existing attributes
                    filtered[attr] = obj[attr]
            return filtered

        return obj

    def reload_from_json(self, json):
        """Mettre à jour les attributs de
        l'étudiant à partir d'un dictionnaire JSON."""
        for key, value in json.items():
            setattr(self, key, value)
