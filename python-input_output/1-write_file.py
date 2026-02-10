#!/usr/bin/python3
"""
fonction qui écrit une chaîne dans un fichier texte (UTF8)
et renvoie le nombre de caractères écrits :
"""


def write_file(filename="", text=""):
    """
    Dans cette fonction j'ai utiliser l'instruction
    with pour ouvrir le fichier
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
