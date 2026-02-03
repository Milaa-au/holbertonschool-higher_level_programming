#!/usr/bin/python3
"""Class qui hérite de (list) et qui contient une fonction qui 
affiche la liste hérité par ordre croissant sans la modifier"""

class MyList(list):

    """Fonction qui affiche la liste self tirée par ordre croissant et sans la modifier"""
    def print_sorted(self):
        print(sorted(self))