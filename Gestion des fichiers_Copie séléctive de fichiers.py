import os
import shutil

def copier_fichiers(source, destination, extension):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    for fichier in os.listdir(source):
        if fichier.endswith(extension):
            src_path = os.path.join(source, fichier)
            dst_path = os.path.join(destination, fichier)
            shutil.copy(src_path, dst_path)
            print(f"Copié: {fichier}")

# Exemple d'utilisation
copier_fichiers("data_source", "data_backup", ".csv")