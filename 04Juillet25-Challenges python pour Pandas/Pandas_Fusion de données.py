import pandas as pd
import numpy as np

# DataFrames exemple
clients = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'Nom': ['Alice', 'Bob', 'Charlie']
})

commandes = pd.DataFrame({
    'commande_id': ['A101', 'A102', 'A103'],
    'customer_id': [1, 2, 1],
    'montant': [150, 200, 300]
})

# Fusion des données
df_fusion = pd.merge(clients, commandes, on='customer_id')

print("\nDataFrame fusionné :")
print(df_fusion)