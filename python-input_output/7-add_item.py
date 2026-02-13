#!/usr/bin/python3
"""
Ajouter des arguments à une liste et
les enregistrer dans un fichier JSON.
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_args = sys.argv[1:]
if os.path.exists("add_item.json"):
    files = load_from_json_file("add_item.json")
else:
    files = []
files.extend(list_args)
save_to_json_file(files, "add_item.json")