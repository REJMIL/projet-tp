#Challenge 5 : Somme d’entiers
#Objectif : Apprendre à utiliser la boucle while pour répéter une opération jusqu’à une condition donnée.
#Travail à faire :
#Ecrivez un programme en Python qui calcule la somme de 1 à N, où N est saisi par l'utilisateur. En utilisant la boucle "while".


# Demander à l'utilisateur de saisir un nombre N
N = int(input("Entrez SVP un nombre entier N : "))

# Initialiser les variables
somme = 0  # Variable pour stocker la somme totale
i = 1      # Compteur qui commencera à 1

# Boucle while : répéter tant que i est inférieur ou égal à N
while i < N+1 :
    somme = somme + i  # Ajouter la valeur actuelle de i à la somme
    i = i + 1          # Incrémenter le compteur pour passer au nombre suivant

# Afficher le résultat final
print(f"La somme de 1 à {N} est : {somme}")