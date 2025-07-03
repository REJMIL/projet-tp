#Challenge 4 : Remplacement de Mots dans des Textes
#Objectif : Remplacer des mots spécifiques dans une phrase par d'autres mots.
#Travail à faire :
#Écrire un programme en Python qui demande à l'utilisateur deux nombres n1 et n2 et lui indique ensuite si le produit de ces deux nombres est positif ou négatif. On prévoit dans le programme le cas où le produit peut être nul.



# Demander à l'utilisateur de saisir deux nombres
n1 = float(input("Entrez SVP le premier nombre (n1) : "))
n2 = float(input("Entrez SVP le deuxième nombre (n2) : "))

# Calculer le produit
produit = n1 * n2

# Vérifier le signe du produit
if produit > 0:
    print(f"Le produit des 2 nombres entrés {produit} est positif")
elif produit < 0:
    print(f"Le produit des 2 nombres entrés {produit} est négatif")
else:
    print(f"Le produit est nul (égal à zéro)")