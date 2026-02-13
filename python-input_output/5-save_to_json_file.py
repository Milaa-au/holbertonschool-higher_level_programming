#!/usr/bin/python3
"""
Définit une fonction qui écrit un
objet dans un fichier au format JSON.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Écrire un objet Python dans un
    fichier en utilisant le format JSON.
    """
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
