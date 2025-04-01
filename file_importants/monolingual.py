import fasttext
import sys

def get_word_vectors_from_file(input_file, model_file, output_file):
    # Charger le modèle préentraîné
    model = fasttext.load_model(model_file)
    
    # Ouvrir le fichier de sortie pour écrire les vecteurs
    with open(output_file, 'w') as f:
        # Ouvrir le fichier d'entrée contenant les mots
        with open(input_file, 'r') as word_file:
            for line in word_file:
                word = line.strip()  # Supprimer les espaces et sauts de ligne autour du mot
                
                # Vérifier si le mot n'est pas vide
                if word:
                    # Obtenir le vecteur pour chaque mot
                    vector = model.get_word_vector(word)
                    
                    # Écrire le mot et son vecteur dans le fichier de sortie
                    f.write(f"{word} {' '.join(map(str, vector))}\n")
    
    print(f"Les vecteurs des mots ont été sauvegardés dans {output_file}")

if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 4:
        print("Usage: python script.py <input_file> <model_file> <output_file>")
        sys.exit(1)
    
    # Les arguments sont : fichier d'entrée, modèle, fichier de sortie
    input_file = sys.argv[1]
    model_file = sys.argv[2]
    output_file = sys.argv[3]
    
    # Obtenir les vecteurs des mots à partir du fichier
    get_word_vectors_from_file(input_file, model_file, output_file)
