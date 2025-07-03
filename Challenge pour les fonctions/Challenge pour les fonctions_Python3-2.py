# Demander à l’utilisateur un nombre entier m et afficher sa table de multiplication de 1 à 10.

# Saisie utilisateur
entree = input("Entrez SVP un nombre ENTIER et je vous donnerai sa table de multiplication: ")

# Vérification avec while 
while not entree.isdigit():
    entree = input("Erreur. Entrez un nombre ENTIER valide : ")

m = int(entree)

# Affichage de la table avec while
print(f"\nTable de multiplication de {m} :")
i = 1
while i <= 10:
    print(f"{m} x {i} = {m * i}")
    i += 1