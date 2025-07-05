import os

# Spécifiez le chemin du répertoire contenant le fichier
chemin_repertoire = "/chemin/vers/le/repertoire"  # Remplacez par votre chemin
fichier_config = os.path.join(chemin_repertoire, "config.yaml")

# Vérifier l'existence du fichier
if os.path.exists(fichier_config):
    print("Le fichier config.yaml existe.")
    
    try:
        # Ouvrir et lire le fichier
        with open(fichier_config, 'r') as fichier:
            contenu = fichier.read()
            print("\nContenu du fichier :\n")
            print(contenu)
            
    except Exception as e:
        print(f"\nErreur lors de la lecture : {str(e)}")
        
else:
    print("Le fichier config.yaml n'existe pas.")