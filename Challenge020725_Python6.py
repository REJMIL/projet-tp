# Méthode avec boucle while
chaine_originale=input("Entrez la chaine de caractère SVP: ")


def inverser_chaine_while(chaine):
    chaine_inversee = ""
    index = len(chaine) - 1
    
    while index >= 0:
        chaine_inversee += chaine[index]
        index -= 1
    
    return chaine_inversee



chaine_inversee = inverser_chaine_while(chaine_originale)
print(f"Chaîne originale: {chaine_originale}")
print(f"Chaîne inversée: {chaine_inversee}")