#Challenge 6 : Calcul de distance entre deux points
#Objectif : Apprendre à manipuler les nombres flottants et à appliquer une formule mathématique en Python. Cet exercice permet d’utiliser l’entrée utilisateur (input()), la conversion de types (float()), et la fonction math.sqrt() pour calculer la distance euclidienne entre deux points 
#Travail à faire :
#Écrire un programme Python pour calculer la distance entre deux points. image
#Remarque: x1, y1, x2, y2 sont tous des valeurs flottants.

import math

# Demander les coordonnées du premier point
x1 = float(input("Entrez x1 : "))
y1 = float(input("Entrez y1 : "))

# Demander les coordonnées du deuxième point
x2 = float(input("Entrez x2 : "))
y2 = float(input("Entrez y2 : "))

# Calculer la distance euclidienne
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Afficher le résultat
print(f"La distance entre les points ({x1}, {y1}) et ({x2}, {y2}) est : {distance}")