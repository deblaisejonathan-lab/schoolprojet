class Produit:
    TVA=0.18
    def __init__(self,nom,prix_ht,stock=0):
        self.nom=nom
        self.prix_ht=prix_ht
        self.stock=stock


        def prix_ttc() ->float:
            calcul_ttc= self.prix_ht*(1+Produit.TVA)
            return round(calcul_ttc)
        def valeur_stock()->int:
            return self.prix_ht*self.stock

        def vendre(quantite):
            if quantite>self.stock:
               raise ValueError("stock insuffisant")
            self.stock=-quantite
            return self.stock* self.prix_ht
        #def __str__():

jus = Produit("Carton de jus 12x1L ", 6000, 50)
riz = Produit("sacde riz 25Kg", 17500, 8)

class Panier:
        def __init__(self,client,lignes):
            self.client=client
            self.lignes=[]
        def ajouter(self,produit,quantite):
            #produit.vendre(quantite)
            self.lignes.append({"produit":produit,"quantite":quantite})
        def total(self):
            to=0.0
            for ligne in self.lignes:
                q=ligne["produit"]
                e=ligne["quantite"]
                to += q.self.prix_ht * e
            return round(to,2)
panier_awa =Panier("maquis awa","3")
panier_awa.ajouter('cartons de jus',2)
panier_awa.ajouter( "sac de riz",1)
print(f"Client : {panier_awa.client}")
print(f"Montant total TTC du panier : {panier_awa.total()} FCFA")


