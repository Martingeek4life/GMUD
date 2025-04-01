import re
import argparse

def extract_vocab(input_file, output_file):
    # Lire le texte
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Extraire les mots (minuscules pour éviter doublons)
    words = re.findall(r'\b\w+\b', text.lower())

    # Vocabulaire unique
    vocabulaire = sorted(set(words))

    print(f"Nombre total de mots uniques : {len(vocabulaire)}")

    # Sauvegarder
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in vocabulaire:
            f.write(word + '\n')

    print(f"Vocabulaire sauvegardé dans '{output_file}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extraction du vocabulaire unique d'un fichier texte.")
    parser.add_argument('input_file', help="Chemin du fichier texte d'entrée")
    parser.add_argument('output_file', help="Chemin du fichier de sortie pour le vocabulaire")

    args = parser.parse_args()

    extract_vocab(args.input_file, args.output_file)

