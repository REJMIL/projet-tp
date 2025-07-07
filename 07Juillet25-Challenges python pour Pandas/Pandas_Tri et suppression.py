import pandas as pd

# Création d'un exemple de DataFrame
data = {
    'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
    'Âge': [25, 32, 18, 47],
    'Année de Naissance': [1998, 1991, 2005, 1976]
}
df = pd.DataFrame(data)

print("DataFrame initial:")
print(df)
print("\n")

# 1. Trier par âge décroissant
df_trié = df.sort_values(by='Âge', ascending=False)
print("DataFrame trié par âge décroissant:")
print(df_trié)
print("\n")

# 2. Supprimer la colonne 'Année de Naissance'
df_sans_année = df_trié.drop(columns='Année de Naissance')
print("Après suppression de la colonne 'Année de Naissance':")
print(df_sans_année)
print("\n")

# 3. Supprimer la première ligne (index 0)
df_final = df_sans_année.drop(index=0)
print("Résultat final après suppression de la première ligne:")
print(df_final)