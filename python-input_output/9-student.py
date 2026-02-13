#!/usr/bin/python3
"""
Définit une classe Student avec
méthode pour obtenir ses attributs.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def to_json(self):
        """Retourner le dictionnaire des attributs de l'étudiant."""
        return self.__dict__
