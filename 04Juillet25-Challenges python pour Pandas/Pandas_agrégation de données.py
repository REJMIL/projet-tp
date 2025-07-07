import pandas as pd
import numpy as np
# Création d'exemple de données de ventes
data = {
    'Region': ['Nord', 'Sud', 'Nord', 'Est', 'Sud', 'Est'],
    'Ventes': [1500, 2200, 1800, 2100, 1900, 2400]
}
df = pd.DataFrame(data)

# Calcul des ventes totales par région
ventes_par_region = df.groupby('Region')['Ventes'].sum()

print("\nVentes par région :")
print(ventes_par_region)