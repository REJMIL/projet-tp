# Classe de base pour toutes les personnes de l'école
class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    
    # Méthode commune à redéfinir
    def afficher_infos(self):
        return "Information de base"

# Étudiant : une personne avec des notes
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
        self.notes = []  # Liste vide pour les notes
    
    def ajouter_note(self, note):
        """Ajoute une note entre 0 et 20"""
        if note < 0 or note > 20:
            print("Erreur : La note doit être entre 0 et 20")
        else:
            self.notes.append(note)
    
    def moyenne(self):
        """Calcule la moyenne des notes"""
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)
    
    def afficher_infos(self):
        """Affiche les informations de l'étudiant"""
        return (f"Étudiant: {self.prenom} {self.nom}, "
                f"Matricule: {self.matricule}, "
                f"Âge: {self.age}, "
                f"Moyenne: {self.moyenne():.1f}/20")

# Enseignant : une personne avec un salaire
class Enseignant(Personne):
    def __init__(self, nom, prenom, age, specialite, salaire):
        super().__init__(nom, prenom, age)
        self.specialite = specialite
        self.salaire = salaire  # Utilise le setter
    
    @property
    def salaire(self):
        """Récupère le salaire"""
        return self._salaire
    
    @salaire.setter
    def salaire(self, valeur):
        """Modifie le salaire avec validation"""
        if valeur < 15000:
            print("Erreur : Salaire minimum 15000 MAD")
            self._salaire = 15000  # Valeur par défaut
        else:
            self._salaire = valeur
    
    def afficher_infos(self):
        """Affiche les informations de l'enseignant"""
        return (f"Enseignant: {self.prenom} {self.nom}, "
                f"Spécialité: {self.specialite}, "
                f"Âge: {self.age}, "
                f"Salaire: {self.salaire}MAD")

# Système principal de gestion de l'école
class Ecole:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []
        self.enseignants = []
    
    def ajouter_etudiant(self, nouvel_etudiant):
        """Ajoute un étudiant à l'école"""
        self.etudiants.append(nouvel_etudiant)
    
    def ajouter_enseignant(self, nouvel_enseignant):
        """Ajoute un enseignant à l'école"""
        self.enseignants.append(nouvel_enseignant)
    
    def afficher_tous(self):
        """Affiche tous les membres de l'école"""
        print(f"\n--- MEMBRES DE {self.nom.upper()} ---")
        for etudiant in self.etudiants:
            print("• " + etudiant.afficher_infos())
        for enseignant in self.enseignants:
            print("• " + enseignant.afficher_infos())

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'étudiants
    etudiant1 = Etudiant("Dupont", "Jean", 18, "ETU001")
    etudiant1.ajouter_note(14)
    etudiant1.ajouter_note(16)
    
    etudiant2 = Etudiant("Martin", "Sophie", 19, "ETU002")
    etudiant2.ajouter_note(12)
    etudiant2.ajouter_note(18)
    
    # Création d'enseignants
    prof_maths = Enseignant("Dubois", "Pierre", 45, "Mathématiques", 3000)
    prof_physique = Enseignant("Leroy", "Marie", 38, "Physique", 2800)
    
    # Modification de salaire
    prof_physique.salaire = 2900  # Valide
    prof_maths.salaire = 1200     # Invalide → déclenche l'erreur
    
    # Création de l'école
    mon_ecole = Ecole("École Simplifiée")
    
    # Ajout des membres
    mon_ecole.ajouter_etudiant(etudiant1)
    mon_ecole.ajouter_etudiant(etudiant2)
    mon_ecole.ajouter_enseignant(prof_maths)
    mon_ecole.ajouter_enseignant(prof_physique)
    
    # Affichage final
    mon_ecole.afficher_tous()