import sys
from src.core.repository import SheetsRepository
from src.ui import printers

def run_menu():
    repo = SheetsRepository()
    
    printers.print_welcome()
    # Pre-check connection (optional, good UX)
    # printers.console.print("[dim]Tentativo di connessione a Google Sheets...[/dim]")
    # if not repo.check_connection():
    #     printers.print_error("Impossibile connettersi a Google Sheet. Controlla l'URL in config.py")
    
    while True:
        printers.print_menu_options()
        choice = input("\n> ").strip()
        
        if choice == '1':
            _handle_check_stats(repo)
        elif choice == '2':
            _handle_msg_trainer(repo)
        elif choice == '3':
            printers.print_success("Arrivederci!")
            sys.exit(0)
        else:
            printers.print_error("Opzione non valida. Riprova.")

def _handle_check_stats(repo: SheetsRepository):
    student_id = input("Inserisci ID Studente: ").strip()
    if not student_id:
        return

    try:
        printers.console.print("[dim]Recupero dati in corso...[/dim]")
        # Force refresh or cache strategy could go here
        record = repo.get_student_stats(student_id)
        
        if record:
            printers.print_stats(record)
        else:
            printers.print_error(f"ID Studente '{student_id}' non trovato nel registro.")
            
    except Exception as e:
        printers.print_error(str(e))

def _handle_msg_trainer(repo: SheetsRepository):
    # Placeholder for integrity check
    try:
        repo.fetch_data()
        printers.print_success("Connessione stabilita. Il formato dei dati sembra valido.")
        printers.console.print(f"[dim]Colonne trovate: {repo._df.columns.tolist()}[/dim]")
    except Exception as e:
        printers.print_error(f"Verifica Integrità Fallita: {e}")
