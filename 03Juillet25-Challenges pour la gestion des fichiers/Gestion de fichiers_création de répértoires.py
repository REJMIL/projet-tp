import os

def creer_structure(repertoire_principal, sous_repertoires):
    try:
        os.mkdir(repertoire_principal)
        print(f"Répertoire principal créé: {repertoire_principal}")
        
        for sous_rep in sous_repertoires:
            chemin_sous_rep = os.path.join(repertoire_principal, sous_rep)
            os.mkdir(chemin_sous_rep)
            print(f"Sous-répertoire créé: {chemin_sous_rep}")
            
    except FileExistsError:
        print("Erreur: Le répertoire existe déjà")

# Exemple d'utilisation
creer_structure("Projet", ["docs", "data", "scripts"])