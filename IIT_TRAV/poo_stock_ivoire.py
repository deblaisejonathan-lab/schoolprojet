class Produit:
    TV=0.18

    def __init__(self,nom,prix_ht,stock=0):
        self.nom= nom
        self.stock= stock
        self.prix_ht=prix_ht
jus = Produit("Carton de jus 12x1L ", 6000, 50)
riz = Produit("Sac de riz 25kg", 17500, 8)

    def prix_ttc(self) -> float:
        """Calcule et retourne le prix TTC arrondi à 2 décimales."""
        calcul_ttc = self.prix_ht * (1 + Produit.TV)
        return round(calcul_ttc, 2)

    def valeur_stock(self) -> float:
        """Calcule et retourne la valeur totale du stock (prix HT × stock)."""
        return self.prix_ht * self.stock

    def vendre(self, quantite: int) -> float:
        if quantite > self.stock:
            raise ValueError(f"Stock insuffisant : demandé {quantite}, disponible {self.stock}")

        self.stock -= quantite
        return self.prix_ttc() * quantite

    def __str__(self) -> str:
        return f"{self.nom} — {self.prix_ht} FCFA HT ({self.stock} en stock)"



class Panier:
        def __init__(self, client: str):
            self.client = client
            self.lignes = []  # Liste pour stocker les produits et leurs quantités

        def ajouter(self, produit, quantite: int):
            # On peut aussi vérifier le stock via la méthode vendre ou directement ici
            if quantite > produit.stock:
                raise ValueError(f"Stock insuffisant pour ajouter {produit.nom} au panier.")

            self.lignes.append({"produit": produit, "quantite": quantite})

        def total_ttc(self) -> float:
            """Calcule la somme des prix_ttc × quantité pour tous les articles du panier."""
            total = 0.0
            for ligne in self.lignes:
                p = ligne["produit"]
                q = ligne["quantite"]
                total += p.prix_ttc() * q
            return round(total, 2)


jus = ("Carton de jus 12x1L", 6000.0, 50)
riz = ("Sac de riz 25kg", 22000.0, 20)

    print(jus)  # Affiche : Carton de jus 12x1L — 6000.0 FCFA HT (50 en stock)

    panier_awa = Panier("Maquis Chez Awa")

    panier_awa.ajouter(jus, 2)
    panier_awa.ajouter(riz, 1)

    print(f"Client : {panier_awa.client}")
    print(f"Montant total TTC du panier : {panier_awa.total_ttc()} FCFA")


