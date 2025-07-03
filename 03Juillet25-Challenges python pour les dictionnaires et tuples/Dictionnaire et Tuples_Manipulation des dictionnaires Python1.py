#Objectif : Apprendre à manipuler des dictionnaires en Python à travers plusieurs opérations clés
#Travail a faire:
#Considérons le dictionnaire suivant :
#First_dict = { "Appareil": "Laptop", "Marque": "IBM", "Carte mère": "MSI Z490", "Carte Graphique":"GeForce RTX 3070", "RAM": "16G", "Processeur": "Intel core i7-G11", "SSD": "1 To" }
#Écris un programme Python qui effectue les opérations suivantes :
#Corriger la valeur associée à la clé "RAM" pour qu’elle devienne "32G".
#Afficher successivement :
#La liste des clés du dictionnaire
#La liste des valeurs
#La liste des paires clé-valeur
#Inverser les paires "Processeur" : "Intel core i7-G11" et "Carte Graphique" : "GeForce RTX 3070"
#Ajouter la paire clé-valeur suivante : "Système d’exploitation": "Windows 10"

First_dict = { 
    "Appareil": "Laptop", 
    "Marque": "IBM", 
    "Carte mère": "MSI Z490", 
    "Carte Graphique": "GeForce RTX 3070", 
    "RAM": "16G", 
    "Processeur": "Intel core i7-G11", 
    "SSD": "1 To" 
}

# 1. Corriger la valeur de "RAM"
First_dict["RAM"] = "32G"

# 2. Afficher les listes
print("Liste des clés :", list(First_dict.keys()))
print("Liste des valeurs :", list(First_dict.values()))
print("Liste des paires clé-valeur :", list(First_dict.items()))
##print("Liste des paires clé-valeur :", [(k, First_dict[k]) for k in First_dict])

# 3. Inverser "Processeur" et "Carte Graphique"
processeur_temp = First_dict["Processeur"]
First_dict["Processeur"] = First_dict["Carte Graphique"]
First_dict["Carte Graphique"] = processeur_temp

# 4. Ajouter "Système d’exploitation"
First_dict["Système d’exploitation"] = "Windows 10"

# Résultat final
print("\nDictionnaire final :", First_dict)