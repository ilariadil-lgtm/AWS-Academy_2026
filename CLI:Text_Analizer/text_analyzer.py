import warnings
# Suppress FutureWarning from google.generativeai
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

import argparse
import os
import sqlite3
import json
import sys
import typing
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

# Carica le variabili d'ambiente
load_dotenv()

# Configurazione
NOME_DB = "analysis_results.db"
FILE_ULTIMA_ANALISI = "latest_analysis.json"
CHIAVE_API_GEMINI = os.getenv("GEMINI_API_KEY")

class TextAnalyzer:
    def __init__(self):
        self.configura_gemini()
        self.inizializza_db()

    def configura_gemini(self):
        """Configura il client Google Gemini AI."""
        if not CHIAVE_API_GEMINI:
            # Non solleviamo un errore qui per permettere l'esecuzione di help/validazione argomenti,
            # ma lo verificheremo prima dell'analisi.
            pass
        else:
            genai.configure(api_key=CHIAVE_API_GEMINI)
            self.model = genai.GenerativeModel('gemini-2.5-flash')

    def inizializza_db(self):
        """Inizializza il database SQLite e la tabella history."""
        try:
            conn = sqlite3.connect(NOME_DB)
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME,
                    source TEXT,
                    content TEXT,
                    sentiment TEXT,
                    word_count INTEGER
                )
            ''')
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Errore durante l'inizializzazione del database: {e}", file=sys.stderr)
            sys.exit(1)

    def salva_nella_cronologia(self, fonte: str, contenuto: str, sentimento: str, conteggio_parole: int):
        """Salva i risultati dell'analisi nel database SQLite."""
        try:
            conn = sqlite3.connect(NOME_DB)
            cursor = conn.cursor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                INSERT INTO history (timestamp, source, content, sentiment, word_count)
                VALUES (?, ?, ?, ?, ?)
            ''', (timestamp, fonte, contenuto, sentimento, conteggio_parole))
            conn.commit()
            conn.close()
            print("Salvataggio nel database completato.")
        except sqlite3.Error as e:
            print(f"Errore nel salvataggio su database: {e}", file=sys.stderr)

    def salva_ultimo_json(self, dati: dict):
        """Salva l'ultima analisi in un file JSON."""
        try:
            with open(FILE_ULTIMA_ANALISI, 'w', encoding='utf-8') as f:
                json.dump(dati, f, indent=4, ensure_ascii=False)
            print(f"Salvataggio in {FILE_ULTIMA_ANALISI} completato.")
        except IOError as e:
            print(f"Errore nel salvataggio del file JSON: {e}", file=sys.stderr)

    def analizza_testo(self, testo: str) -> dict:
        """Invia il testo all'API Gemini per l'analisi."""
        if not CHIAVE_API_GEMINI:
            raise ValueError("GEMINI_API_KEY non trovata. Assicurati di aver configurato il file .env")

        print("Analisi in corso con Gemini AI...")
        
        prompt = f"""
        Analizza il seguente testo e restituisci ESCLUSIVAMENTE un oggetto JSON valido.
        Non includere blocchi di codice markdown (```json ... ```). Restituisci solo il JSON raw.
        
        Il JSON deve avere queste due chiavi:
        1. "sentiment": Classifica il testo come "Positivo", "Negativo" o "Neutro".
        2. "word_count": Conta il numero di parole nel testo.

        Testo da analizzare:
        "{testo}"
        """

        try:
            response = self.model.generate_content(prompt)
            # Pulisce la risposta se necessario (a volte i modelli aggiungono backticks nonostante le istruzioni)
            testo_risposta = response.text.strip()
            if testo_risposta.startswith("```json"):
                testo_risposta = testo_risposta[7:]
            if testo_risposta.endswith("```"):
                testo_risposta = testo_risposta[:-3]
            
            return json.loads(testo_risposta)
        except Exception as e:
            raise RuntimeError(f"Errore durante l'analisi AI: {e}")

    def esegui(self):
        parser = argparse.ArgumentParser(description="Tool CLI per l'analisi testuale con Google Gemini.")
        parser.add_argument("--text", type=str, help="Testo da analizzare (stringa).")
        parser.add_argument("--file", type=str, help="Percorso del file di testo da analizzare.")

        args = parser.parse_args()

        # Validazione: Almeno un input richiesto
        if not args.text and not args.file:
            parser.error("Devi specificare almeno un input: --text o --file")

        contenuto = ""
        fonte = ""

        try:
            if args.file:
                fonte = "File"
                print(f"Lettura del file: {args.file}...")
                with open(args.file, 'r', encoding='utf-8') as f:
                    contenuto = f.read()
            else:
                fonte = "CLI"
                contenuto = args.text

            if not contenuto.strip():
                print("Errore: Il contenuto da analizzare è vuoto.", file=sys.stderr)
                return

            # Esegui Analisi
            risultato = self.analizza_testo(contenuto)
            
            sentimento = risultato.get("sentiment", "N/D")
            conteggio_parole = risultato.get("word_count", 0)

            print("\n--- Risultati Analisi ---")
            print(f"Sentiment: {sentimento}")
            print(f"Word Count: {conteggio_parole}")
            print("-------------------------")

            # Salva risultati
            # Tronchiamo il contenuto nel DB per risparmiare spazio se necessario, ma qui salviamo i primi 500 caratteri
            self.salva_nella_cronologia(fonte, contenuto[0:500], sentimento, conteggio_parole) 
            
            record_completo = {
                "timestamp": datetime.now().isoformat(),
                "source": fonte,
                "content": contenuto,
                "sentiment": sentimento,
                "word_count": conteggio_parole
            }
            self.salva_ultimo_json(record_completo)

        except FileNotFoundError:
            print(f"Errore: File '{args.file}' non trovato.", file=sys.stderr)
        except Exception as e:
            print(f"Errore imprevisto: {e}", file=sys.stderr)


