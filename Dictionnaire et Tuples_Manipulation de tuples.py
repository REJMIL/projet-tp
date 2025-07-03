#Challenge : Manipulation de tuples 
#Objectif : Comprendre la structure des tuples, leur immutabilité, et leur utilisation pour stocker des données groupées et ordonnées.
#Travail a faire: Crée un tuple nommé etudiant_info contenant les informations suivantes dans cet ordre : Prénom : "Yasmine", Âge : 22, Filière : "Informatique", Moyenne générale : 17.4
#Affiche les informations stockées dans le tuple, une par ligne, avec un texte explicite. (ex: “Prénom : Yasmine”)
#Tente de modifier la filière dans le tuple. Que se passe-t-il ? Explique pourquoi.
#Utilise l'opérateur de slicing pour afficher uniquement le prénom et l'âge.
#Crée un nouveau tuple en combinant etudiant_info avec un second tuple contenant la mention "Très Bien" et l’année d’obtention du diplôme (2024), puis affiche le tuple final

# Création du tuple etudiant_info
etudiant_info = ("Yasmine", 22, "Informatique", 17.4)

# Affichage des informations ligne par ligne
print("Prénom :", etudiant_info[0])
print("Âge :", etudiant_info[1])
print("Filière :", etudiant_info[2])
print("Moyenne générale :", etudiant_info[3])

# Tentative de modification de la filière (décommenter pour tester l'erreur)
# etudiant_info[2] = "Mathématiques"  # Lève une TypeError

# Explication de l'immutabilité
print("\nExplication : Les tuples sont immutables en Python, on ne peut pas modifier leurs éléments après création.")

# Slicing pour afficher prénom et âge
print("\nPrénom et âge (slicing) :", etudiant_info[0:2])

# Création du nouveau tuple combiné
second_tuple = ("Très Bien", 2024)
nouveau_tuple = etudiant_info + second_tuple

# Affichage du tuple final
print("\nTuple combiné :", nouveau_tuple)