import json
import os
from typing import Dict, List

class Corsi:
    def __init__(self, file_path: str = "presenze.json"):
        self.file_path = file_path
        self.dati = self._carica_dati()

    def _carica_dati(self) -> Dict:
        """Carica i dati dal file JSON se esiste, altrimenti restituisce un dizionario vuoto."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Errore nel caricamento del file {self.file_path}. Partenza con dati vuoti.")
                return {}
        return {}

    def salva(self):
        """Salva i dati correnti nel file JSON."""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.dati, f, indent=4, ensure_ascii=False)

    def aggiungi_corso(self, nome_corso: str) -> bool:
        """Aggiunge un nuovo corso. Restituisce True se aggiunto, False se già esistente o nome vuoto."""
        if not nome_corso.strip():
            print("Errore: Il nome del corso non può essere vuoto.")
            return False
        if nome_corso in self.dati:
            print(f"Errore: Il corso '{nome_corso}' esiste già.")
            return False
        self.dati[nome_corso] = {"studenti": [], "registro": {}}
        self.salva()
        print(f"Corso '{nome_corso}' aggiunto con successo.")
        return True

    def visualizza_corsi(self) -> List[str]:
        """Restituisce la lista dei nomi dei corsi."""
        return list(self.dati.keys())

    def modifica_corso(self, nome_vecchio: str, nome_nuovo: str) -> bool:
        """Modifica il nome di un corso esistente. Restituisce True se modificato."""
        if not nome_nuovo.strip():
            print("Errore: Il nuovo nome del corso non può essere vuoto.")
            return False
        if nome_vecchio not in self.dati:
            print(f"Errore: Il corso '{nome_vecchio}' non esiste.")
            return False
        if nome_nuovo in self.dati:
            print(f"Errore: Il corso '{nome_nuovo}' esiste già.")
            return False
        # Sposta i dati sotto la nuova chiave
        self.dati[nome_nuovo] = self.dati.pop(nome_vecchio)
        self.salva()
        print(f"Corso rinominato da '{nome_vecchio}' a '{nome_nuovo}'.")
        return True

    def elimina_corso(self, nome_corso: str) -> bool:
        """Elimina un corso e tutti i suoi dati. Restituisce True se eliminato."""
        if nome_corso not in self.dati:
            print(f"Errore: Il corso '{nome_corso}' non esiste.")
            return False
        del self.dati[nome_corso]
        self.salva()
        print(f"Corso '{nome_corso}' eliminato con successo.")
        
