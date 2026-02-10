#!/usr/bin/python3
"""
Fonction qui écrit un objet dans un fichier texte,
en utilisant une représentation JSON.
"""
import json 


def save_to_json_file(my_obj, filename):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
