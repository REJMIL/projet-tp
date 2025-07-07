import pandas as pd
import numpy as np

# Création d'exemple de données
data = {
    'Produit': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Region': ['Nord', 'Nord', 'Sud', 'Sud', 'Est', 'Est'],
    'Ventes': [150, 200, 300, 250, 100, 180]
}
df = pd.DataFrame(data)

# Création du tableau croisé dynamique
pivot_table = pd.pivot_table(
    df,
    values='Ventes',
    index='Produit',
    columns='Region',
    aggfunc=np.sum,
    fill_value=0
)

print("\nTableau croisé dynamique :")
print(pivot_table)