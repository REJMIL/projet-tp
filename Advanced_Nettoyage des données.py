import pandas as pd
import numpy as np

# Charger les données (remplacer 'votre_fichier.csv' par votre fichier réel)
df = pd.read_csv('votre_fichier.csv')

# 5.1 Remplacer les valeurs manquantes dans 'Age' par la médiane
df['Age'] = df['Age'].fillna(df['Age'].median())

# 5.2 Remplir les valeurs manquantes dans 'Salaire' avec la moyenne par département
df['Salaire'] = df.groupby('Departement')['Salaire'].transform(
    lambda x: x.fillna(x.mean())
)

# 5.3 Convertir les colonnes numériques en type approprié
# Identification automatique des colonnes numériques
colonnes_numeriques = df.select_dtypes(include=[np.number]).columns
# Conversion explicite en float ou int
for col in colonnes_numeriques:
    # Conversion en int si toutes les valeurs sont entières
    if df[col].dropna().apply(float.is_integer).all():
        df[col] = pd.to_numeric(df[col], errors='coerce', downcast='integer')
    else:
        df[col] = pd.to_numeric(df[col], errors='coerce', downcast='float')

# 5.4 Remplacer 'Yes'/'No' dans 'Remote' par 'Oui'/'Non'
df['Remote'] = df['Remote'].replace({
    'Yes': 'Oui',
    'No': 'Non'
})

# 5.5 Créer la colonne 'Ancienneté_Catégorie'
conditions = [
    df['Anciennete'] < 3,
    (df['Anciennete'] >= 3) & (df['Anciennete'] <= 7),
    (df['Anciennete'] >= 8) & (df['Anciennete'] <= 15),
    df['Anciennete'] > 15
]

categories = ['Junior', 'Intermédiaire', 'Senior', 'Expert']

df['Ancienneté_Catégorie'] = np.select(conditions, categories, default='Autre')

# Sauvegarder le résultat (optionnel)
df.to_csv('donnees_nettoyees.csv', index=False)

print("Nettoyage terminé avec succès !")
print(df.head())