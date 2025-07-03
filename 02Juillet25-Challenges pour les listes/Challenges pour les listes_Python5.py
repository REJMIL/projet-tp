# Liste donnée
L = [7, 23, 5, 23, 7, 19, 23, 12, 29]

# Demander la valeur à chercher
a = int(input("Entrez la valeur à chercher : "))

# Initialisation du compteur
compteur = 0

# Parcourir chaque élément de la liste
i = 0
while i < len(L):
    if L[i] == a:
        compteur += 1
    i += 1

# Afficher le résultat
print("La valeur", a, "apparaît", compteur, "fois dans la liste.")