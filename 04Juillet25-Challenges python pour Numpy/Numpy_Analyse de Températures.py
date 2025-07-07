import numpy as np

# 1. Création du tableau de températures
temperatures = np.array([17.5, 22.3, 19.8, 25.1, 16.7, 23.4, 21.0])

# 2. Calculs statistiques
moyenne = np.mean(temperatures)
mediane = np.median(temperatures)
ecart_type = np.std(temperatures)

# 3. Affichage des résultats
print("Tableau de températures :", temperatures)
print(f"Température moyenne : {moyenne:.2f}°C")
print(f"Médiane des températures : {mediane:.2f}°C")
print(f"Écart-type : {ecart_type:.2f}°C")