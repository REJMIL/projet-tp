# Création des trois dictionnaires
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# Fusion en un seul dictionnaire
resultat = {}  # Dictionnaire initial vide
resultat.update(dict1)  # Ajout des éléments du premier dictionnaire
resultat.update(dict2)  # Ajout des éléments du second
resultat.update(dict3)  # Ajout des éléments du troisième

# Affichage du résultat final
print("Dictionnaire fusionné :", resultat)