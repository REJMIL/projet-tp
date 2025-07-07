import pandas as pd
import numpy as np

# Création d'un DataFrame exemple
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Âge': [25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)

print("DataFrame initial :")
print(df)

# Étape 1: Introduction manuelle d'une valeur NaN
df.at[2, 'Âge'] = np.nan  # Remplace l'âge de Charlie par NaN

print("\nDataFrame après introduction de NaN :")
print(df)

# Étape 2: Affichage des lignes avec valeurs manquantes
print("\nLignes avec valeurs manquantes :")
print(df[df.isnull().any(axis=1)])

# Étape 3: Remplacer les valeurs manquantes par la moyenne
moyenne_age = df['Âge'].mean()
df['Âge'] = df['Âge'].fillna(moyenne_age)

print("\nDataFrame après remplacement des NaN :")
print(df)