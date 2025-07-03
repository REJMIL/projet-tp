def calculation(a, b):
    somme = a + b
    difference = a - b
    return somme, difference

# Demande des nombres à l'utilisateur
nombre1 = int(input("Entrez SVP un 1 ier nombre: "))
nombre2 = int(input("Entrer SVP un 2 ième nombre et je vous donnerai la somme et la différence: "))

# Appel de la fonction avec décomposition du tuple
somme, difference = calculation(nombre1, nombre2)

# Affichage des résultats
print(f"Somme: {somme}")
print(f"Différence: {difference}")