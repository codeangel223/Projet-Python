import csv
import os

FICHIERS = {
    "users": "data/users.csv",
    "clients": "data/clients.csv",
    "fournisseurs": "data/fournisseurs.csv"
}

ENTETES = {
    "users": ["ID", "Nom", "Email"],
    "clients": ["ID", "Nom", "Email", "Adresse"],
    "fournisseurs": ["ID", "Nom", "Email", "Capital", "Adresse", "Type_Produit", "Nationalité"]
}

def initialiser_fichier(type_fichier):
    fichier = FICHIERS[type_fichier]
    en_tete = ENTETES[type_fichier]

    if not os.path.exists("data"):  
        os.makedirs("data")

    fichier_existe = os.path.exists(fichier)

    with open(fichier, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not fichier_existe or os.stat(fichier).st_size == 0:
            writer.writerow(en_tete)

def charger_donnees(type_fichier):
    fichier = FICHIERS[type_fichier]
    donnees = []

    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                donnees.append(row)
    
    return donnees

def ajouter_donnees(type_fichier, objet):
    fichier = FICHIERS[type_fichier]

    with open(fichier, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(objet.__str__().split(","))
