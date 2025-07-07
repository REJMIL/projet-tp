import numpy as np
# Création d'un tableau de données
donnees = np.array([15, 28, 32, 12, 24])

# Normalisation (moyenne=0, écart-type=1)
donnees_normalisees = (donnees - np.mean(donnees)) / np.std(donnees)

# Affichage
print("Challenge Normalisation:")
print(f"Original: {donnees}")
print(f"Normalisé: {np.round(donnees_normalisees, 2)}\n")