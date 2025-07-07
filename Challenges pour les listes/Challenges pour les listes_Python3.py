stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]

# Afficher la liste initiale
print("Liste initiale :")
print(stock)

# Séparation des chaînes et des nombres
chaines = []
nombres = []

for element in stock:
    if isinstance(element, str):
        chaines.append(element)
    elif isinstance(element, (int, float)):
        nombres.append(element)

# Tri des listes
chaines_triees = sorted(chaines)           # Ordre alphabétique croissant
nombres_tries = sorted(nombres, reverse=True) # Ordre numérique décroissant

# Affichage des résultats
print("\nListe des chaînes triées (ordre alphabétique) :")
print(chaines_triees)
print("\nListe des nombres triés (ordre décroissant) :")
print(nombres_tries)