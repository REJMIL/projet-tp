def ecrire_fichier(nom_fichier, lignes):
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            for ligne in lignes:
                f.write(ligne + "\n")
        print(f"Fichier {nom_fichier} créé avec succès")
        
        # Vérification
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
            print("Contenu vérifié:", contenu)
            
    except IOError:
        print("Erreur lors de l'écriture")

# Exemple d'utilisation
ecrire_fichier("journal.txt", ["Ligne 1: Début", "Ligne 2: Suite", "Ligne 3: Fin"])