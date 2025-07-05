import numpy as np
# Création d'un tableau numérique
valeurs = np.array([12, 35, 7, 42, 19, 28, 3, 15])

# Sélection des éléments > 20
seuil = 20
indices_selection = np.where(valeurs > seuil)[0]
valeurs_selectionnees = valeurs[valeurs > seuil]

# Affichage
print("Challenge Sélection Conditionnelle:")
print(f"Tableau original: {valeurs}")
print(f"Éléments > {seuil}: {valeurs_selectionnees}")
print(f"Indices correspondants: {list(indices_selection)}")