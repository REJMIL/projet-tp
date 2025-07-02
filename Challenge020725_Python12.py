# Programme de présentation avec âge futur
while True:
    # Demander le prénom (La méthode .strip() est ajoutée pour nettoyer l'entrée utilisateur en supprimant les espaces superflus au début et à la fin de la chaîne)
    prenom = input("Entrez votre prénom : ").strip()
    
    # Vérifier que le prénom n'est pas vide
    if not prenom:
        print("Erreur : Le prénom ne peut pas être vide. Veuillez réessayer.")
        continue
    
    # Demander l'âge avec validation
    age_input = input("Entrez votre âge : ").strip()
    
    # Vérifier que l'âge est numérique
    if not age_input.isdigit():
        print("Erreur : L'âge doit être un nombre entier. Veuillez réessayer.")
        continue
    
    age = int(age_input)
    
    # Vérifier que l'âge est raisonnable (0-120)
    if age < 0:
        print("Erreur : L'âge ne peut pas être négatif. Veuillez réessayer.")
    elif age > 120:
        print("Erreur : L'âge semble trop élevé. Veuillez réessayer.")
    else:
        break

# Calculer l'âge futur
age_futur = age + 1

# Afficher le message personnalisé
print(f"Bonjour {prenom}! Actuellement vous avez {age} ans.")
print(f"L'année prochaine vous aurez {age_futur} ans!")