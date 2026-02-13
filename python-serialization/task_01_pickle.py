#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialisation des attributs name, age et si c'est un etudiants
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Afficher les attributs"""
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """Utilise le fichier save pour sérialiser"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Change et renvoie une instance"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, OSError, EOFError):
            return None
