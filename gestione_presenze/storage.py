import json
import os
import shutil
import uuid
from typing import Dict, List, Optional, Literal
from datetime import datetime

DB_FILE = "database.json"
BACKUP_FILE = "database_backup.json"

# Tipi di stato presenza
StatoPresenza = Literal["Presente", "Assente", "Ritardo"]

class Storage:
    def __init__(self, db_file: str = DB_FILE):
        self.db_file = db_file
        self.backup_file = BACKUP_FILE
        self.data = self._carica_dati()
    
    def _carica_dati(self) -> Dict:
        """
        Carica i dati dal file JSON.
        Se non esiste o è corrotto, ritorna struttura vuota.
        
        Struttura:
        {
            "NomeCorso": {
                "studenti": [{"id": "uuid", "nome": "Mario Rossi"}],
                "registro": {"13-01-2026": {"uuid": "Presente"}}
            }
        }
        """
        # Prova a caricare il file principale
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Valida la struttura base
                    if isinstance(data, dict):
                        return data
                    else:
                        print(f"Errore: File {self.db_file} ha struttura non valida.")
            except (json.JSONDecodeError, IOError) as e:
                print(f"Errore: File {self.db_file} corrotto ({e}). Tento ripristino da backup...")
        
        # Se fallisce, prova con il backup
        if os.path.exists(self.backup_file):
            try:
                with open(self.backup_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print("✅ Dati ripristinati da backup con successo!")
                    # Ripristina il file principale
                    self._salva_dati_interno(data)
                    return data
            except (json.JSONDecodeError, IOError):
                print("❌ Anche il backup è corrotto.")
        
        # Se tutto fallisce, inizia con database vuoto
        print("ℹ️ Inizializzazione database vuoto.")
        return {}
    
    def _salva_dati_interno(self, data: Dict) -> bool:
        """Salva i dati su file JSON in modo atomico."""
        tmp_file = self.db_file + ".tmp"
        try:
            # Crea backup prima di salvare
            if os.path.exists(self.db_file):
                shutil.copy2(self.db_file, self.backup_file)
            
            # Salva su file temporaneo
            with open(tmp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Sostituzione atomica
            os.replace(tmp_file, self.db_file)
            return True
        except IOError as e:
            print(f"❌ Errore critico durante il salvataggio: {e}")
            if os.path.exists(tmp_file):
                os.remove(tmp_file)
            return False
    
    def _salva_dati(self) -> bool:
        """Salva i dati correnti."""
        return self._salva_dati_interno(self.data)
    