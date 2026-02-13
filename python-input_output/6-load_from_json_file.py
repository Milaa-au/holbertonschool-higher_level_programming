#!/usr/bin/python3
"""
Définit une fonction qui lit
un objet depuis un fichier JSON.
"""
import json


def load_from_json_file(filename):
    """
    Lire un objet Python
    depuis un fichier au format JSON.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
