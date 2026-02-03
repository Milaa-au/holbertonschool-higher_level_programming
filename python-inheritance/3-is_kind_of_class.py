#!/usr/bin/python3
"""Fonction qui renvoie true ou false en fonction que si 
l'objet est une instance de la class donné."""

def is_kind_of_class(obj, a_class):
    return(isinstance(obj, a_class))