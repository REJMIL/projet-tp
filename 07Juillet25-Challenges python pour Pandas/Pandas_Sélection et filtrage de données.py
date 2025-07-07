import pandas as pd

# Création d'un exemple de DataFrame
data = {
    'Nom': ['Alice', 'Bob', 'Claire', 'David', 'Emma'],
    'Âge': [28, 22, 35, 40, 24],
    'Ville': ['Paris', 'Casablanca', 'Casablanca', 'Lyon', 'Casablanca']
}
df = pd.DataFrame(data)

print("DataFrame original :")
print(df)
print("\n" + "-"*50 + "\n")

# 1. Sélection de la colonne Ville
villes = df['Ville']
print("1. Colonne 'Ville' :")
print(villes)
print("\n" + "-"*50 + "\n")

# 2. Filtrage des âges > 25
age_sup_25 = df[df['Âge'] > 25]
print("2. Personnes de plus de 25 ans :")
print(age_sup_25)
print("\n" + "-"*50 + "\n")

# 3. Filtrage des personnes de Casablanca (nom et ville)
casablanca = df[df['Ville'] == 'Casablanca']
resultat_casablanca = casablanca[['Nom', 'Ville']]
print("3. Personnes de Casablanca :")
print(resultat_casablanca)