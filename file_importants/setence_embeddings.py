import sys
import numpy as np

def load_word_vectors(vector_file):
    """ Charge les vecteurs des mots dans un dictionnaire """
    word_vectors = {}
    with open(vector_file, 'r', encoding='utf-8') as vf:
        for line in vf:
            parts = line.strip().split()
            if len(parts) != 301:  # Vérifier que la ligne contient bien un mot + 300 valeurs
                continue
            word = parts[0]
            vector = np.array([float(x) for x in parts[1:]], dtype=np.float32)
            word_vectors[word] = vector
    return word_vectors

def compute_sentence_vectors(sentence_file, word_vectors, output_file):
    """ Calcule le vecteur moyen de chaque phrase et écrit dans le fichier de sortie """
    with open(sentence_file, 'r', encoding='utf-8') as sf, open(output_file, 'w', encoding='utf-8') as out:
        for line in sf:
            words = line.strip().split()
            vectors = [word_vectors[word] for word in words if word in word_vectors]
            
            if vectors:
                sentence_vector = np.mean(vectors, axis=0)  # Moyenne des vecteurs
            else:
                sentence_vector = np.zeros(300, dtype=np.float32)  # Si aucun mot connu
            
            out.write(f"[{', '.join(map(str, sentence_vector))}]\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("❌ Utilisation : python script.py <phrases.txt> <vecteurs.txt> <sortie.txt>")
    else:
        word_vectors = load_word_vectors(sys.argv[2])
        compute_sentence_vectors(sys.argv[1], word_vectors, sys.argv[3])
        print(f"✅ Traitement terminé ! Résultat enregistré dans {sys.argv[3]}")
