import pandas as pd
import numpy as np

# Création d'un exemple de DataFrame avec valeurs manquantes
data = {
    'Age': [25, np.nan, 35, 28, np.nan],
    'Salaire': [3000, 3200, np.nan, 2900, 3100]
}
df = pd.DataFrame(data)

# Remplacer les NaN par la moyenne des colonnes
df_clean = df.fillna(df.mean())

print("DataFrame nettoyé :")
print(df_clean)