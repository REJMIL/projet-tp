#Challenge 3 :  Gestion des erreurs utilisateur
#Objectif : Introduire les blocs try / except afin de rendre le programme plus robuste face aux erreurs de saisie (par exemple, texte au lieu de nombres).
#Travail à faire :
#Réécris ton programme de calcul de salaire en utilisant try et except afin que le programme gère proprement les entrées non numériques en affichant un message d’erreur puis en quittant le programme.


try:
    # Saisie des informations utilisateur
    nom = input("Entrez votre nom : ")
    salaire_horaire = float(input("Entrez votre salaire horaire (MAD) : "))
    heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
    
    # Calcul du salaire
    if heures_travaillees <= 40:
        # Cas sans heures supplémentaires
        salaire_total = heures_travaillees * salaire_horaire
    else:
        # Cas avec heures supplémentaires
        heures_normales = 40
        heures_supplementaires = heures_travaillees - 40
        salaire_normal = heures_normales * salaire_horaire
        salaire_supplementaire = heures_supplementaires * (salaire_horaire * 1.5)
        salaire_total = salaire_normal + salaire_supplementaire
    
    # Affichage du résultat
    print(f"\nRapport de paie pour {nom}:")
    print(f"Salaire total = {salaire_total:.2f} MAD")

except ValueError:
    print("Erreur : Veuillez entrer des valeurs numériques valides pour le salaire et les heures.")
    print("Programme terminé.")