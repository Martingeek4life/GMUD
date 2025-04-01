import os
import re

# Fonction pour extraire les valeurs des lignes
def extract_values_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    patterns = {
        'deformation_moyenne': r"Déformation moyenne: ([\d\.]+)",
        'somme_deformations': r"Somme des Déformations: ([\d\.]+)",
        'ecart_type': r"EcartType des Déformations: ([\d\.]+)",
        'v_d': r"mean_vd: ([\d\.]+)",
        'v_c': r"mean_vc: ([\d\.]+)"
    }

    extracted_values = {}

    for key, pattern in patterns.items():
        match = re.search(pattern, ''.join(lines))
        if match:
            extracted_values[key] = float(match.group(1))
        else:
            extracted_values[key] = None

    return extracted_values

# Fonction principale pour parcourir les dossiers et extraire les données
def extract_data_from_folders(base_dir):
    results = {}

    for folder_name in os.listdir(base_dir):
        if folder_name.startswith('en-') and os.path.isdir(os.path.join(base_dir, folder_name)):
            gmud_path = os.path.join(base_dir, folder_name, 'GMUD/')
            if os.path.isdir(gmud_path):
                for sub_folder in ['101', '201', '501', '1001']:
                    sub_folder_path = os.path.join(gmud_path, sub_folder)
                    if os.path.isdir(sub_folder_path):
                        file_path = os.path.join(sub_folder_path, 'analyse_deformations.txt')
                        if os.path.isfile(file_path):
                            values = extract_values_from_file(file_path)
                            if folder_name not in results:
                                results[folder_name] = []
                            results[folder_name].append({
                                'k': sub_folder,
                                'deformation_moyenne': values['deformation_moyenne'],
                                'somme_deformations': values['somme_deformations'],
                                'ecart_type': values['ecart_type'],
                                'v_d': values['v_d'],
                                'v_c': values['v_c']
                            })

    return results

# Fonction pour générer le tableau LaTeX
def generate_latex_table(results, output_file):
    with open(output_file, 'w') as f:
        f.write(r"\begin{table}[H]" + "\n")
        f.write(r"    \centering" + "\n")
        f.write(r"    \begin{tabular}{|c|c|c|c|c|c|c|}" + "\n")
        f.write(r"        \hline" + "\n")
        f.write(r"        Plongement & Voisinage $k$ & \textbf{moyenne $\mu$} & $s$ & $\sigma$ & $V_d$ & $V_c$ \\ \hline" + "\n")

        for plongement, data in results.items():
            first_row = True
            for item in data:
                if first_row:
                    f.write(f"        {plongement} & {item['k']} & \\textbf{{{item['deformation_moyenne']:.2f}}} & {item['somme_deformations']:.2f} & {item['ecart_type']:.2f} & {item['v_d']:.2f} & {item['v_c']:.2f} \\\\\n")
                    first_row = False
                else:
                    f.write(f"        & {item['k']} & \\textbf{{{item['deformation_moyenne']:.2f}}} & {item['somme_deformations']:.2f} & {item['ecart_type']:.2f} & {item['v_d']:.2f} & {item['v_c']:.2f} \\\\\n")
            f.write(r"        \hline" + "\n")

        f.write(r"    \end{tabular}" + "\n")
        f.write(r"    \caption{Résumé des mesures pour différents voisinages $k$.}" + "\n")
        f.write(r"    \label{tab:metrics}" + "\n")
        f.write(r"\end{table}" + "\n")

# Spécifie le répertoire de base
base_directory = './'  # Remplacer par le chemin contenant les dossiers en-*

# Spécifie le fichier de sortie
output_file = 'resultats_deformations_gmud_bli_reverse.tex'

# Extraire les données
data = extract_data_from_folders(base_directory)

# Générer le fichier LaTeX
generate_latex_table(data, output_file)

print(f"Le tableau LaTeX a été généré dans le fichier {output_file}.")
