#!/usr/bin/env python3
"""Convertion CSV en JSON"""
import csv
import json


def convert_csv_to_json(filename_csv):
    """Convertie un fichier CSV en JSON et écrit dans data.json"""
    try:
        with open(filename_csv, "r", encoding="utf-8") as fcsv:
            reader = csv.DictReader(fcsv)
            liste = []
            for row in reader:
                liste.append(row)
            with open("data.json", "w", encoding="utf-8") as fjson:
                json.dump(liste, fjson)
        return True
    except (FileNotFoundError):
        return False