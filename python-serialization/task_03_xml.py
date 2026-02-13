#!/usr/bin/env python3
"""Sérialiser un dictionnaire plat en XML et le désérialiser à nouveau"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Ecris un  dictio dans le fichier XML"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Lis un fichier XML et renvoie en dictio"""
    tree_2 = ET.parse(filename)
    root = tree_2.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data