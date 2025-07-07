import pandas as pd
import numpy as np

# Création d'un exemple de données financières
data = {
    'Transaction_ID': [101, 102, 103, 104],
    'Montant': [1200, 800, 1500, 950]
}
df = pd.DataFrame(data)

# Filtrer les transactions > 1000
df_filtre = df[df['Montant'] > 1000]

print("\nTransactions > 1000 :")
print(df_filtre)