#!/usr/bin/python3
"""
Fonction qui écrit un objet dans un fichier texte,
en utilisant une représentation JSON.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
    def to_json(self):
        """A modifier"""
        new_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                new_dict[attr] = self.__dict__[attr]
        return new_dict