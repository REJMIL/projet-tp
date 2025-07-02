# Demander un nombre entier à l'utilisateur
while True:
    try:
        L = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")

# Vérifier si c'est un carré parfait
if L < 0:
    print(f"{L} n'est pas un carré parfait (les nombres négatifs ne sont pas des carrés réels).")
else:
    racine = L**0.5  # Calculer la racine carrée
    # Comparer avec la version arrondie
    if racine == int(racine):
        print(f"{L} est un carré parfait ! ({int(racine)}² = {L})")
    else:
        print(f"{L} n'est pas un carré parfait.")