from data_handler import *
from models import User, Client, Fournisseur
from traitementFonctions import *

for type_fichier in FICHIERS.keys():
    initialiser_fichier(type_fichier)


def afficher_utilisateurs():
    utilisateurs = charger_donnees("users")
    
    if not utilisateurs:
        print("⚠️ Aucun utilisateur trouvé.")
        return

    print("\n{:<5} | {:<15} | {:<25}".format("ID", "Nom", "Email"))
    print("-" * 50)

    for u in utilisateurs:
        print("{:<5} | {:<15} | {:<25}".format(u["ID"], u["Nom"], u["Email"]))


def afficher_clients():
    clients = charger_donnees("clients")
    
    if not clients:
        print("⚠️ Aucun client trouvé.")
        return

    print("\n{:<5} | {:<15} | {:<25} | {:<20}".format("ID", "Nom", "Email", "Adresse"))
    print("-" * 70)

    for c in clients:
        print("{:<5} | {:<15} | {:<25} | {:<20}".format(c["ID"], c["Nom"], c["Email"], c["Adresse"]))


def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Ajouter un utilisateur")
        print("2. Ajouter un client")
        print("3. Ajouter un fournisseur")
        print("4. Afficher les fournisseurs")
        print("5. Afficher les utilisateurs")
        print("6. Afficher les clients")
        print("7. Séparer les fournisseurs")
        print("8. Afficher capital max et min")
        print("9. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            id = input("ID : ")
            nom = input("Nom : ")
            email = input("Email : ")
            user = User(id, nom, email)
            ajouter_donnees("users", user)
            print("✅ Utilisateur ajouté !")

        elif choix == "2":
            id = input("ID : ")
            nom = input("Nom : ")
            email = input("Email : ")
            adresse = input("Adresse : ")
            client = Client(id, nom, email, adresse)
            ajouter_donnees("clients", client)
            print("✅ Client ajouté !")

        elif choix == "3":
            id = input("ID : ")
            nom = input("Nom : ")
            email = input("Email : ")
            capital = input("Capital : ")
            adresse = input("Adresse : ")
            type_produit = input("Type de produit/service : ")
            nationalite = input("Nationalité : ")
            fournisseur = Fournisseur(id, nom, email, capital, adresse, type_produit, nationalite)
            ajouter_donnees("fournisseurs", fournisseur)
            print("✅ Fournisseur ajouté !")

        elif choix == "4":
            afficher_fournisseurs()

        elif choix == "5":
            afficher_utilisateurs()

        elif choix == "6":
            afficher_clients()

        elif choix == "7":
            T1, T2 = separer_fournisseurs()
            print("📌 Fournisseurs Sénégalais :", T1)
            print("📌 Autres fournisseurs :", T2)

        elif choix == "8":
            capital_max_min()

        elif choix == "9":
            print("Au revoir !")
            break
        else:
            print("❌ Option invalide.")

if __name__ == "__main__":
    menu()
