#!/usr/bin/python3
"""Ce module définit une fonction qui lit un fichier texte et affiche son contenu."""


def read_file(filename=""):
    """Lit un fichier texte (UTF-8) et affiche son contenu sur la sortie standard."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
