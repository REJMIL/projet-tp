#On considère le dictionnaire suivant dont les clés sont les noms des élèves et les valeurs des clés sont les moyennes générales obtenues en passant l’examen final.
#notes_eleves = { "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2, "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,"Saad": 11.3, "Hannae": 9.8 }
#Écrire un programme Python qui partitionne ce dictionnaire en deux sous dictionnaires :
#etudiantAdmis dont les clés sont les étudiants admis et les valeurs des clés sont les moyennes obtenues (moyenne supérieures ou égales à 10 ).
#etudiantNonAdmis dont les clés sont les étudiants non admis et les valeurs des clés sont les moyennes obtenues (moyenne inférieur ou égale à 10).  

notes_eleves = {
    "Amine": 15.5, "Yassine": 19.0, "Reda": 14.2,
    "Malak": 8.7, "Manal": 20.0, "Ahmed": 7.5,
    "Saad": 11.3, "Hannae": 9.8
}

etudiantAdmis = {}
etudiantNonAdmis = {}

for eleve, moyenne in notes_eleves.items():
    if moyenne >= 10:
        etudiantAdmis[eleve] = moyenne
    else:
        etudiantNonAdmis[eleve] = moyenne

print("etudiantAdmis =", etudiantAdmis)
print("etudiantNonAdmis =", etudiantNonAdmis)