from data_handler import charger_donnees

def afficher_fournisseurs():
    fournisseurs = charger_donnees("fournisseurs")
    
    if not fournisseurs:
        print("⚠️ Aucun fournisseur trouvé.")
        return

    print("\n{:<5} | {:<15} | {:<25} | {:<10} | {:<20} | {:<15} | {:<15}".format(
        "ID", "Nom", "Email", "Capital", "Adresse", "Type Produit", "Nationalité"))
    print("-" * 110)

    for f in fournisseurs:
        print("{:<5} | {:<15} | {:<25} | {:<10} | {:<20} | {:<15} | {:<15}".format(
            f["ID"], f["Nom"], f["Email"], f["Capital"], f["Adresse"], f["Type_Produit"], f["Nationalité"]))


def separer_fournisseurs():
    fournisseurs = charger_donnees("fournisseurs")
    T1 = [f for f in fournisseurs if f["Nationalité"] == "Sénégal"]
    T2 = [f for f in fournisseurs if f["Nationalité"] != "Sénégal"]
    return T1, T2


def capital_max_min():
    fournisseurs = charger_donnees("fournisseurs")
    if fournisseurs:
        max_fournisseur = max(fournisseurs, key=lambda f: float(f["Capital"]))
        min_fournisseur = min(fournisseurs, key=lambda f: float(f["Capital"]))
        print("💰 Fournisseur avec le plus grand capital:", max_fournisseur)
        print("💸 Fournisseur avec le plus petit capital:", min_fournisseur)
