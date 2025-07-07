import pandas as pd

# Chargement du fichier CSV
df = pd.read_csv('employees2.csv')

# Affichage des premières lignes
print("=== Premières lignes du DataFrame ===")
print(df.head())
print("\n" + "-"*50 + "\n")

# Vérification des types de données
print("=== Types de données par colonne ===")
print(df.dtypes)
print("\n" + "-"*50 + "\n")

# Identification des valeurs manquantes
print("=== Valeurs manquantes par colonne ===")
print(df.isnull().sum())