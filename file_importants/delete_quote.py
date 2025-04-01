import sys
import re

def remove_quotes(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                # Supprime uniquement les quotes autour des mots
                cleaned_line = re.sub(r"'([^']+)'", r'\1', line)
                outfile.write(cleaned_line)

        print(f"✅ Traitement terminé ! Fichier enregistré sous : {output_file}")

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{input_file}' n'existe pas.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Utilisation : python script.py <fichier_entrée> <fichier_sortie>")
    else:
        remove_quotes(sys.argv[1], sys.argv[2])
