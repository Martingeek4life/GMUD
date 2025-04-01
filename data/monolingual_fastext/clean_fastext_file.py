import os

def process_files(directory):
    output_directory = os.path.join(directory, "formatted")
    os.makedirs(output_directory, exist_ok=True)
    
    for filename in os.listdir(directory):
        input_file = os.path.join(directory, filename)
        output_file = os.path.join(output_directory, f"formatted_{filename}")
        
        if os.path.isfile(input_file):
            with open(input_file, "r") as infile, open(output_file, "w") as outfile:
                for i, line in enumerate(infile, start=1):
                    cleaned_line = line.strip().replace("[", "").replace("]", "").replace(",", "")
                    outfile.write(f"critique{i} {cleaned_line}\n")
            
            print(f"Fichier formaté enregistré sous {output_file}")

# Exemple d'utilisation
process_files("./")  # Remplace "chemin_du_repertoire" par le chemin réel
