import os
import base64

def decode_base64_files(input_dir, output_dir):
    # Assurez-vous que le répertoire de sortie existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Parcourir tous les fichiers du répertoire d'entrée
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            # Construire le chemin complet du fichier d'entrée et de sortie
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            # Lire le contenu encodé en base64
            with open(input_path, "rb") as file:
                encoded_content = file.read()
            
            try:
                # Décoder le contenu base64
                decoded_content = base64.b64decode(encoded_content)
                
                # Écrire le contenu décodé dans un nouveau fichier
                with open(output_path, "wb") as file:
                    file.write(decoded_content)
                print(f"File {filename} decoded successfully.")
            except Exception as e:
                print(f"Failed to decode {filename}: {e}")

# Chemins des dossiers d'entrée et de sortie ( \\ sur Windows)
input_directory = 'path_to_input_directory'
output_directory = 'path_to_output_directory'

# Appeler la fonction
decode_base64_files(input_directory, output_directory)

