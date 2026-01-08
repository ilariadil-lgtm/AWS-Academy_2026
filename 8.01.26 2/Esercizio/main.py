from storage import load_data
import client_manager

FILENAME = "clienti.json"

def main():
    print("Benvenuto in Gestione Clienti Freelance")
    data = load_data(FILENAME)
    
    while True:
        print("\n--- MENU ---")
        print("1) Aggiungi cliente/progetto")
        print("2) Mostra elenco")
        print("3) Filtra per cliente")
        print("4) Filtra per stato")
        print("5) Riepilogo")
        print("0) Esci")
        
        choice = input("Scelta: ").strip()
        
        if choice == "1":
            client_manager.add_client(data, FILENAME)
        elif choice == "2":
            client_manager.list_clients(data)
        elif choice == "3":
            client_manager.filter_by_client(data)
        elif choice == "4":
            client_manager.filter_by_status(data)
        elif choice == "5":
            client_manager.show_summary(data)
        elif choice == "0":
            print("Uscita in corso...")
            break
        else:
            print("Scelta non valida, riprova.")

if __name__ == "__main__":
    main()
