#!/usr/bin/python3
"""Fonction qui lis un fichier spécifique et qui affiche sa sortie."""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")