class CompteBancaire:
    def __init__(self, nom_proprietaire, solde=0.0):
        self.nom_proprietaire = nom_proprietaire
        self.solde = solde
    
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"ok {montant:.2f} € déposés")
        else:
            print("X Erreur : Montant de dépôt invalide")
    
    def retirer(self, montant):
        if montant <= 0:
            print("X Erreur : Montant de retrait invalide")
        elif montant > self.solde:
            print(f"X Erreur : Solde insuffisant (solde actuel : {self.solde:.2f} €)")
        else:
            self.solde -= montant
            print(f"ok {montant:.2f} MAD retirés")
    
    def afficher_solde(self):
        print(f"\nPropriétaire : {self.nom_proprietaire}")
        print(f"Solde actuel : {self.solde:.2f} €")
        print("-" * 30)

# Correction de la condition d'exécution
if __name__ == '__main__': 
    compte = CompteBancaire("Amine", 1500)
    compte.deposer(500)
    compte.retirer(300)
    compte.retirer(3000)
    compte.deposer(-200)
    compte.afficher_solde()