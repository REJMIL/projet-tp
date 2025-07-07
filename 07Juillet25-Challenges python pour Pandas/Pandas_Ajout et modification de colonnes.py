import pandas as pd

# Création d'un exemple de DataFrame (à adapter avec vos données réelles)
data = {
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Âge': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
}
df = pd.DataFrame(data)

# Étape 1 : Ajout de la colonne "Année de Naissance"
df['Année de Naissance'] = 2025 - df['Âge']

# Étape 2 : Modification des noms en majuscules
df['Nom'] = df['Nom'].str.upper()

# Étape 3 : Renommage de la colonne "Ville" en "Localisation"
df = df.rename(columns={'Ville': 'Localisation'})

# Affichage du résultat
print("DataFrame modifié :")
print(df)