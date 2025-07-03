def horaire_sup():
    """
    Fonction qui calcule le salaire total d'un employé en tenant compte
    des heures supplémentaires (au-delà de 40h payées à 1.5x le taux normal)
    """
    # Saisie des informations utilisateur
    nom = input("Entrez votre nom : ")
    salaire_horaire = float(input("Entrez votre salaire horaire (MAD) : "))
    heures_travaillees = float(input("Entrez le nombre d'heures travaillées : "))
    
    # Calcul du salaire
    if heures_travaillees <= 40:
        # Cas sans heures supplémentaires
        salaire_total = heures_travaillees * salaire_horaire
        print(f"\nRapport de paie pour {nom}:")
        print(f"Heures travaillées : {heures_travaillees}")
        print(f"Salaire total = {salaire_total:.2f} MAD")
    else:
        # Cas avec heures supplémentaires
        heures_normales = 40
        heures_supplementaires = heures_travaillees - 40
        salaire_normal = heures_normales * salaire_horaire
        salaire_supplementaire = heures_supplementaires * (salaire_horaire * 1.5)
        salaire_total = salaire_normal + salaire_supplementaire
        
        # Affichage détaillé avec heures supplémentaires
        print(f"\nRapport de paie pour {nom}:")
        print(f"Heures normales (40h) : {salaire_normal:.2f} MAD")
        print(f"Heures supplémentaires ({heures_supplementaires}h à 1.5x) : {salaire_supplementaire:.2f} MAD")
        print(f"Salaire total = {salaire_total:.2f} MAD")
    
    return salaire_total