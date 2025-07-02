# Demander un nombre entier
nombre = int(input("Entrez SVP un nombre entier et je vous dirai si c'est un carré parfait ou pas: "))

# Vérifier si c'est un carré parfait
if nombre < 0:
    print("Ce n'est pas un carré parfait (les nombres négatifs ne sont pas des carrés parfait)")
else:
    racine = nombre**0.5
    if racine == int(racine):
        print(f"Oui, {nombre} est un carré parfait ({int(racine)}²)")
    else:
        print(f"Non, {nombre} n'est pas un carré parfait")