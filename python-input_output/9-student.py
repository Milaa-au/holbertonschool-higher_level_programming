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
        return self.__dict__