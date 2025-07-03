# Liste originale des notes
notes = [12, 4, 14, 11, 18, 13, 7, 10, 5, 9, 15, 8, 14, 16]

# 1. Calculer la moyenne
somme_notes = sum(notes)      # Additionne toutes les notes
nb_notes = len(notes)         # Compte le nombre de notes
moyenne = somme_notes / nb_notes  # Calcule la moyenne

# 2. Créer une liste vide pour les notes supérieures
notes_sup = []

# 3. Parcourir chaque note et comparer à la moyenne
for note in notes:             # Pour chaque note dans la liste
    if note > moyenne:         # Si la note est strictement supérieure à la moyenne
        notes_sup.append(note) # Ajouter à la nouvelle liste

# 4. Afficher les résultats
print("Moyenne:", moyenne)
print("Notes supérieures à la moyenne:", notes_sup)