import pandas as pd
import numpy as np

# Création des données
data = [
    ["Amine", 28, "Casablanca"],
    ["Lina", 22, "Rabat"],
    ["Youssef", 35, "Fès"],
    ["Salma", 30, "Casablanca"],
    ["Nora", np.nan, "Tanger"]
]

# Création du DataFrame
df = pd.DataFrame(data, columns=['Nom', 'Âge', 'Ville'])

# Affichage des 5 premières lignes
print("Premières 5 lignes :")
print(df.head())

# Affichage de la structure
print("\nInformations sur le DataFrame :")
print(df.info())

# Statistiques descriptives
print("\nStatistiques descriptives :")
print(df.describe())