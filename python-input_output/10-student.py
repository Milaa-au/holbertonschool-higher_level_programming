#!/usr/bin/python3
"""Définit une classe Student avec
méthode pour obtenir certains attributs."""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retourner un dictionnaire des
        attributs sélectionnés de l'étudiant."""
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj
            d_list = {}
            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list
        return obj

