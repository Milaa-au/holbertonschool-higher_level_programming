#!/usr/bin/python3

"""
Deux fonctions qui envoie une requete et reçoive une réponse
et si ça fonctionne font des choses différentes.
"""
import requests
import csv

def fetch_and_print_posts():

    """
    Fonction qui récupère tout les articles depuis 
    JSONPlaceholder. Donc j'envoie ma requete à l'api je vérifie la 
    reponse ensuite si ça fonctionne alors j'affiche les titres.
    """

    url = "https://jsonplaceholder.typicode.com/posts"
    ma_requete = requests.get(url)

    print(f"Status Code: {ma_requete.status_code}")

    if ma_requete.status_code == 200:
        data = ma_requete.json()
        
        for post in data:
            print(post["title"])

def fetch_and_save_posts():

    """
    Fonction qui récupère tout les articles depuis 
    JSONPlaceholder. Donc j'envoie ma requete à l'api je vérifie la 
    reponse ensuite si ça fonctionne alors je créer une liste et j'ajoute
    l'id des postes, le titre et le contenu puis j'enregistre ces donnees
    avec cvs
    """

    url = "https://jsonplaceholder.typicode.com/posts"
    ma_requete = requests.get(url)

    print(f"Status Code: {ma_requete.status_code}")

    if ma_requete.status_code == 200:
        data = ma_requete.json()

        post_list = []

        for post in data:
            post_list.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(post_list)
