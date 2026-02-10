#!/usr/bin/python3
"""
Fonction qui écrit un objet dans un fichier texte,
en utilisant une représentation JSON.
"""
import json 


def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)