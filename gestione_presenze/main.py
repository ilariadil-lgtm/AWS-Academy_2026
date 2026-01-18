import os
from storage import Storage
from courses import Corsi
from student_manager import StudentManager
from attendance import AttendanceManager

def main():
    # Definiamo un unico file di database per coerenza tra tutti i moduli [cite: 13]
    DB_FILE = "presenze.json"

    # 1. Inizializzazione Storage (Modulo di Manuela)
    # Carica i dati e gestisce i casi di file mancante o corrotto [cite: 10, 11]
    store = Storage(DB_FILE)
    data = store.data 

    # 2. Inizializzazione Manager
    # Sincronizziamo il modulo corsi con il dizionario caricato dallo storage
    course_mgr = Corsi(DB_FILE)
    course_mgr.dati = data 
    
    # Il modulo Atrendance (Elisabetta) riceve il riferimento ai dati 
    attendance_mgr = AttendanceManager(data)

    while True:
        print("\n=== 🎯 SISTEMA GESTIONE PRESENZE ===")
        print("1. Crea nuovo Corso")
        print("2. Iscrivi Studente a un corso")
        print("3. Registra Presenze (Oggi)")
        print("4. Visualizza Report Visuale (Icone)")
        print("5. Esci e Salva")
        
        scelta = input("\nSeleziona un'opzione: ")

        if scelta == "1":
            nome_corso = input("Nome del nuovo corso: ")
            # Usa il metodo del file courses.py [cite: 1]
            course_mgr.aggiungi_corso(nome_corso)

        elif scelta == "2":
            corso = input("Nome del corso: ")
            if corso in data:
                nome_st = input("Nome dello studente: ")
                # Il modulo di Ilaria usa metodi statici (@staticmethod) [cite: 4, 5]
                try:
                    StudentManager.add_student(data, corso, nome_st)
                    print(f"Studente {nome_st} aggiunto.")
                    store._salva_dati_interno(data) # Salvataggio immediato [cite: 17]
                except ValueError as e:
                    print(f"Errore: {e}")
            else:
                print("Corso non esistente.")

        elif scelta == "3":
            corso = input("Nome corso: ")
            if corso in data:
                data_p = input("Data (DD-MM-YYYY): ")
                status_map = {}
                # Ciclo sugli studenti per mappare gli ID agli stati (Tua parte) [cite: 7, 12]
                for s in data[corso]['studenti']:
                    stato = input(f"Stato per {s['nome']} (Presente/Assente/Ritardo): ").capitalize()
                    if stato in ["Presente", "Assente", "Ritardo"]:
                        status_map[s['id']] = stato
                    else:
                        status_map[s['id']] = "Assente" # Default in caso di errore
                
                # Chiama la tua funzione in attendance.py [cite: 7]
                attendance_mgr.mark_attendance(corso, data_p, status_map)
                store._salva_dati_interno(data)
                print("Presenze registrate.")
            else:
                print("Corso non trovato.")

        elif scelta == "4":
            corso = input("Nome corso: ")
            data_p = input("Data (DD-MM-YYYY): ")
            # Genera il report con 🟢, 🔴, ⚠️ e ⚪ 
            print(attendance_mgr.get_visual_report(corso, data_p))

        elif scelta == "5":
            store._salva_dati_interno(data) # Salvataggio finale [cite: 13]
            print("Dati salvati. Chiusura in corso...")
            break

if __name__ == "__main__":
    main()