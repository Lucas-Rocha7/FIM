import os
import hashlib
import json
from time import sleep

def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def generate_hashes(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_file_hash(file_path)
    return file_hashes

def save_hashes(file_hashes, output_file):
    with open(output_file, 'w') as f:
        jsonj.dump(file_hashes, f, indent=4)

def load_hashes(input_file):
    try:
        with open(input_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    
def check_integrity(new_hashes, old_hashes):
    changes = []
    for file_path, new_hash in new_hashes.items():
        old_hash = old_hashes.get(file_path)
        if not old_hash:
            changes.append(f"[ADICINADO] {file_path}")
        elif new_hash != old_hash:
            changes.append(f"[ALTERADO] {file_path}")
    
    for file_path in old_hashes.keys() - new_hashes.keys():
        changes.append(f"[REMOVIDO] {file_path}")

    return changes

def monitor_directory(directory, output_file, interval=60):
    print(f"Monitorando o diretorio: {directory}")
    old_hashes = load_hashes(output_file)
    while True:
        new_hashes = generate_hashes(directory)
        changes = check_integrity(new_hashes, old_hashes)

        if changes:
            print("Mundancas detectadas:")
            for change in changes:
                print(change)
        else:
            print("Nenhuma mudanca detectada.")

        save_hashes(new_hashes, output_file)
        old_hashes = new_hashes

        sleep(interval) # Pausa por um intervalo antes de verificar novamente  

        if__name__ =="__main__":
            directory_to_monitor = "./diretorio_de_teste" # Substitua pelo caminho do diretorio que voce quer monitorar
            output_file = "file_hashes.json"
            monitor_directory(directory_to_monitor, output_file, interval=60)