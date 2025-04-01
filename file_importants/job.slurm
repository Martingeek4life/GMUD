#!/bin/bash
#SBATCH --job-name=gmud_calcul_xnli_%j   # Nom du job
#SBATCH --output=gmud_%j.out     # Nom du fichier de sortie
#SBATCH --error=gmud_%j.err      # Nom du fichier d'erreur
#SBATCH --time=120:00:00          # Temps maximum pour le job (HH:MM:SS)
#SBATCH --mem=80G               # Mémoire totale allouée
#SBATCH --cpus-per-task=20       # Nombre de cœurs CPU
#SBATCH --gres=gpu:1             # Nombre de GPU
#SBATCH --partition=gpu

python ~/seminaire_lemans/GMUD.py --embeddings_before ../../vocab_critique_en_quote.vec  --embeddings_after ../../english_movievecs_crosslingual.vec  --distance_metric cosine --nb_neighbors 101
