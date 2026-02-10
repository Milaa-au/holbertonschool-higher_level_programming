#!/usr/bin/python3
"""
Fonction qui écrit une chaîne a la fin d'un fichier
et qui renvoie le nombre de caractères ajoutés. 
"""


def append_write(filename="", text=""):
    """
    Dans cette fonction j'ai utiliser l'instruction
    with pour ouvrir le fichier
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
