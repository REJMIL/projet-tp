import os

# Spécifiez le chemin du répertoire contenant les fichiers
chemin_repertoire = "./chemin/vers/repertoire"

# Liste pour stocker le contenu de chaque fichier
contenus = []

# Lister tous les fichiers dans le répertoire
for nom_fichier in os.listdir(chemin_repertoire):
    chemin_complet = os.path.join(chemin_repertoire, nom_fichier)
    
    # Vérifier si c'est un fichier texte (extension .txt)
    if os.path.isfile(chemin_complet) and nom_fichier.endswith('.txt'):
        try:
            # Ouvrir et lire le fichier
            with open(chemin_complet, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
                contenus.append(contenu)
        except Exception as e:
            print(f"Erreur lors de la lecture de {nom_fichier} : {e}")

# Combiner tous les contenus en un seul texte
texte_combine = "\n\n".join(contenus)

# Afficher le résultat
print("Texte combiné :")
print(texte_combine)