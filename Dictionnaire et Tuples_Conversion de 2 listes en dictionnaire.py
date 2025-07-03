#Challenge : Conversion de Deux Listes en Dictionnaire
#Objectif : Créer un dictionnaire à partir de deux listes (une pour les clés, une pour les valeurs).
#Travail à faire :
#Utilisez zip() pour combiner les deux listes.
#Convertissez le résultat en dictionnaire.
#Affichez le dictionnaire créé.

# Définition des deux listes
cles = ["pomme", "banane", "orange"]
valeurs = [1.2, 0.8, 1.5]

# Conversion en dictionnaire avec zip() et dict()
fruit_prix = dict(zip(cles, valeurs))

# Affichage du résultat
print("Dictionnaire fruits-prix :", fruit_prix)