import numpy as np

# Création de deux matrices 2x2
matrice_A = np.array([[1, 2], [3, 4]])
matrice_B = np.array([[5, 6], [7, 8]])

# Multiplication matricielle
produit_matriciel = np.dot(matrice_A, matrice_B)

# Transposée et inverse
transposee = produit_matriciel.T
inverse = np.linalg.inv(produit_matriciel)

# Affichage
print("Challenge Opérations Matricielles:")
print(f"Produit matriciel:\n{produit_matriciel}")
print(f"Transposée:\n{transposee}")
print(f"Inverse (arrondie):\n{np.round(inverse, 2)}\n")
