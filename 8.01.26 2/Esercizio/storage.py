import json
import os

def load_data(filename):
    """
    Loads data from a JSON file.
    Returns a list of records. If file doesn't exist or is invalid, returns an empty list.
    """
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f"Errore: Impossibile leggere il file {filename}. Si parte da un elenco vuoto.")
        return []

def save_data(filename, data):
    """
    Saves the list of data to a JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError:
        print(f"Errore: Impossibile salvare su {filename}.")
        return False
