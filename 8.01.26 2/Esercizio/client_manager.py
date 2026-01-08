from storage import save_data

VALID_STATUSES = ["in_corso", "concluso", "da_fatturare"]

def validate_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            num = float(value)
            if num < 0:
                print("Il compenso non può essere negativo.")
                continue
            return num
        except ValueError:
            print("Inserisci un numero valido (es. 500 o 500.0).")

def validate_status(prompt):
    print(f" Stati validi: {', '.join(VALID_STATUSES)}")
    while True:
        value = input(prompt).strip().lower().replace(" ", "_") # allow "in corso" -> "in_corso"
        if value in VALID_STATUSES:
            return value
        print(f"Stato non valido. Scegli tra: {', '.join(VALID_STATUSES)}")

def add_client(data, filename):
    print("\n--- Aggiungi Nuovo Cliente ---")
    
    # Nome Cliente
    while True:
        nome = input("Nome Cliente: ").strip()
        if nome: break
        print("Il nome non può essere vuoto.")
        
    # Nome Progetto
    while True:
        progetto = input("Nome Progetto: ").strip()
        if progetto: break
        print("Il progetto non può essere vuoto.")
        
    # Compenso
    compenso = validate_float("Compenso (€): ")
    
    # Stato
    stato = validate_status("Stato (in_corso, concluso, da_fatturare): ")
    
    record = {
        "cliente": nome,
        "progetto": progetto,
        "compenso": compenso,
        "stato": stato
    }
    
    data.append(record)
    if save_data(filename, data):
        print("Cliente aggiunto con successo.")
        print(f"Dati salvati in {filename}.")
    else:
        print("Errore durante il salvataggio data.")

def list_clients(data):
    print("\n--- Elenco Clienti ---")
    if not data:
        print("Nessun cliente in elenco.")
        return

    print(f"{'Cliente':<20} | {'Progetto':<20} | {'Compenso':<10} | {'Stato':<15}")
    print("-" * 75)
    for row in data:
        print(f"{row['cliente']:<20} | {row['progetto']:<20} | € {row['compenso']:<8.2f} | {row['stato']:<15}")

def filter_by_client(data):
    print("\n--- Filtra per Cliente ---")
    query = input("Inserisci nome cliente (o parte): ").lower()
    filtered = [r for r in data if query in r['cliente'].lower()]
    list_clients(filtered)

def filter_by_status(data):
    print("\n--- Filtra per Stato ---")
    query = validate_status("Inserisci stato esatto: ")
    filtered = [r for r in data if r['stato'] == query]
    list_clients(filtered)

def show_summary(data):
    print("\n--- Riepilogo Economico ---")
    total_projects = len(data)
    total_earnings = sum(r['compenso'] for r in data)
    total_to_invoice = sum(r['compenso'] for r in data if r['stato'] == 'da_fatturare')
    
    print(f"Totale progetti: {total_projects}")
    print(f"Totale compensi: € {total_earnings:,.2f}")
    print(f"Totale da fatturare: € {total_to_invoice:,.2f}")
