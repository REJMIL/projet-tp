# Étape 1 : Création du dictionnaire initial
dico = {"maths": 18, "français": 15, "histoire": 12, "sport": 20}

# Étape 2 : Obtenir les paires clé-valeur avec items()
paires = dico.items()

# Étape 3 : Trier les paires par valeur (croissant)
# - key=lambda x: x[1] spécifie qu'on trie par le 2ème élément de chaque tuple (la valeur)
paires_triees = sorted(paires, key=lambda x: x[1])

# Étape 4 : Créer un nouveau dictionnaire à partir des paires triées
dico_trie = dict(paires_triees)

# Affichage du résultat
print("Dictionnaire original :", dico)
print("Dictionnaire trié par valeurs :", dico_trie)