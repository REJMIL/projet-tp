# Demander une phrase à l'utilisateur
phrase = input("Entrez une phrase et je vous donnerai le mot le plus long : ")

# Séparer la phrase en mots
mots = phrase.split()

# Trouver le mot le plus long
mot_long = ""
for mot in mots:
    if len(mot) > len(mot_long):
        mot_long = mot

# Afficher le résultat
print("Le mot le plus long est :", mot_long)