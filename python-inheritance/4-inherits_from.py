#!/usr/bin/python3
"""Fonction qui renvoie true ou false en fonction que si 
l'objet est une instance de la class donné."""

def inherits_from(obj, a_class):
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
