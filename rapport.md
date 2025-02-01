# 📌 Projet de Gestion des Utilisateurs, Clients et Fournisseurs en Python

## 📖 Description du Projet
Ce projet est une application en Python permettant de gérer des **utilisateurs, clients et fournisseurs** avec stockage des données dans des fichiers CSV. Il intègre un **menu interactif** permettant d'ajouter, afficher et organiser ces données efficacement.

## 🏗️ Structure du Projet
```
/ProjetPython
│── main.py                   # Menu interactif
│── models.py                 # Définition des classes avec héritage
│── data_handler.py           # Gestion des fichiers CSV
│── traitementFonctions.py    # Fonctions spécifiques aux fournisseurs
│── data/                     # Dossier contenant les fichiers CSV
│    │── users.csv
│    │── clients.csv
│    │── fournisseurs.csv
```

## 🛠️ Technologies Utilisées
- Python 3
- Gestion des fichiers **CSV** avec `csv`
- Programmation orientée objet (POO)

## 📌 Fonctionnalités
✅ Ajout et gestion des **Utilisateurs, Clients et Fournisseurs**
✅ Stockage sécurisé des données dans des fichiers CSV
✅ **Affichage formaté** sous forme de tableau dans le terminal
✅ **Tri et séparation** des fournisseurs en fonction de leur nationalité
✅ **Identification** des fournisseurs avec le plus grand et plus petit capital
✅ **Création automatique** des fichiers CSV avec leurs en-têtes
✅ Interface **interactive** avec un menu de navigation

## 🏛️ Modèle Objet
### **Classe `User` (Parent)**
```python
class User:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email
```

### **Classe `Client` (Hérite de `User`)**
```python
class Client(User):
    def __init__(self, id, nom, email, adresse):
        super().__init__(id, nom, email)
        self.adresse = adresse
```

### **Classe `Fournisseur` (Hérite de `User`)**
```python
class Fournisseur(User):
    def __init__(self, id, nom, email, capital, adresse, type_produit, nationalite):
        super().__init__(id, nom, email)
        self.capital = capital
        self.adresse = adresse
        self.type_produit = type_produit
        self.nationalite = nationalite
```

## 📂 Gestion des Fichiers CSV (`data_handler.py`)
- 📌 `users.csv` → Stocke les **utilisateurs** (ID, Nom, Email)
- 📌 `clients.csv` → Stocke les **clients** (ID, Nom, Email, Adresse)
- 📌 `fournisseurs.csv` → Stocke les **fournisseurs** (ID, Nom, Email, Capital, Adresse, Type_Produit, Nationalité)

### **Fonctions Principales :**
- **`initialiser_fichier(type_fichier)`** → Vérifie et crée les fichiers CSV
- **`charger_donnees(type_fichier)`** → Lit les données du CSV et les retourne sous forme de dictionnaire
- **`ajouter_donnees(type_fichier, objet)`** → Ajoute une nouvelle entrée dans le fichier CSV

## 🎮 Menu Interactif (`main.py`)
### **Options disponibles :**
```
1. Ajouter un utilisateur
2. Ajouter un client
3. Ajouter un fournisseur
4. Afficher les fournisseurs
5. Afficher les utilisateurs
6. Afficher les clients
7. Séparer les fournisseurs
8. Afficher capital max et min
9. Quitter
```

## 🖥️ Exécution du Programme
### **Installation et Exécution :**
1. **Cloner le projet**
   ```sh
   git clone https://github.com/ton-repo/projet-python-gestion.git
   cd projet-python-gestion
   ```
2. **Lancer le programme**
   ```sh
   python main.py
   ```

## ✅ Résultats Attendus
### **Affichage des utilisateurs :**
```
ID    | Nom            | Email                    
--------------------------------------------------
1     | CodeAngel      | codeangel@gmail.com      
2     | Moussa        | moussa@example.com      
```
### **Affichage des fournisseurs :**
```
ID    | Nom            | Email                      | Capital   | Adresse         | Type Produit    | Nationalité     
------------------------------------------------------------------------------------------------------
001   | CodeANGEL      | codeangel@gmail.com        | 2000.0    | Bamako          | Informatique    | Malienne       
```

## 🚀 Améliorations Possibles
🔹 Interface graphique avec `Tkinter` ou `PyQt`
🔹 Connexion à une **base de données SQLite ou MySQL**
🔹 Ajout d’un **système d’authentification**

## 👨‍💻 Auteur
👤 **Moussa MALLE** (mallemoussa091@gmail.com) - Master1 IA - DIT

