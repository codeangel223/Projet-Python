class User:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"{self.id},{self.nom},{self.email}"


class Client(User):
    def __init__(self, id, nom, email, adresse):
        super().__init__(id, nom, email)
        self.adresse = adresse

    def __str__(self):
        return f"{self.id},{self.nom},{self.email},{self.adresse}"


class Fournisseur(User):
    def __init__(self, id, nom, email, capital, adresse, type_produit, nationalite):
        super().__init__(id, nom, email)
        self.capital = capital
        self.adresse = adresse
        self.type_produit = type_produit
        self.nationalite = nationalite

    def __str__(self):
        return f"{self.id},{self.nom},{self.email},{self.capital},{self.adresse},{self.type_produit},{self.nationalite}"
