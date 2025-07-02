#Challenge  2 : Calcul de salaire avec heures supplémentaires
#Objectif :  Travailler la saisie de données utilisateur, les conversions de types, les conditions (if), et les opérations arithmétiques pour simuler un cas réel de calcul de paie.
#Travail à faire : Écris un programme qui récupère les informations suivantes depuis l’entrée utilisateur : son nom, son salaire horaire et le nombre d’heures qu’il a travaillées.
#Si le nombre d’heures travaillées dépasse 40 heures, les heures au-delà de 40 seront considérées comme des heures supplémentaires et rémunérées à 1,5 fois le salaire horaire normal.
#Le programme doit alors calculer le salaire total (salaire régulier + éventuelles heures supplémentaires).
#Enfin, affiche le nom de l’utilisateur ainsi que son salaire total calculé.

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