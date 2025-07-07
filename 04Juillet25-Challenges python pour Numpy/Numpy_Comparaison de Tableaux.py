import numpy as np

# Création de deux tableaux similaires avec différences
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([10, 21, 30, 42, 50])

# Trouver les indices où les éléments diffèrent
indices_diff = np.where(arr1 != arr2)[0]

# Affichage des différences
print("Challenge Comparaison:")
print(f"Tableau 1: {arr1}")
print(f"Tableau 2: {arr2}")
print("Différences aux indices:")
for i in indices_diff:
    print(f"Index {i}: {arr1[i]} vs {arr2[i]}\n")