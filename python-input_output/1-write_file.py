#!/usr/bin/python3
"""
Définit une fonction qui écrit
une chaîne dans un fichier texte UTF-8.
"""


def write_file(filename="", text=""):
    """
    Écrire une chaîne dans un fichier
    et retourner le nombre de caractères écrits.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
