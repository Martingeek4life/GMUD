import sys

def format_fastext(file_path, output_path):
    with open(file_path, 'r', encoding='utf-8') as f_in, open(output_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            parts = line.strip().split()
            if len(parts) < 301:
                continue  # Ignore malformed lines
            word = parts[0]
            vector = ' '.join(parts[1:])
            f_out.write(f"'{word}' {vector}\n")
    print(f"Fichier formaté enregistré sous : {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    format_fastext(input_file, output_file)
