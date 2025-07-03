# Demander à l'utilisateur de saisir un nombre entier
n = int(input("Entrez un nombre entier positif et je vous calculerai la factorielle: "))

# Vérifier que le nombre est positif
if n < 0:
    print("Erreur : La factorielle n'est définie que pour les nombres positifs")
elif n == 0 or n == 1:
    print(f"{n}! = 1")
else:
    # Initialiser les variables pour la boucle while
    factorielle = 1
    i = 1
    
    # Calculer la factorielle avec une boucle while
    while i <= n:
        factorielle = factorielle * i
        i = i + 1
    
    # Afficher le résultat
    print(f"{n}! = {factorielle}")