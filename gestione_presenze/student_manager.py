import uuid

class Student:
    def __init__(self, name, student_id=None):
        if not name or not name.strip():
            raise ValueError("Il nome dello studente non può essere vuoto")
        self.name = name
        self.id = student_id if student_id else str(uuid.uuid4())

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.name
        }

    @staticmethod
    def from_dict(data):
        return Student(name=data["nome"], student_id=data["id"])

class StudentManager:
    @staticmethod
    def add_student(data, course_name, student_name):
        """
        Aggiunge un nuovo studente a un corso.
        Args:
            data (dict): La struttura dati principale.
            course_name (str): Il nome del corso.
            student_name (str): Il nome dello studente.
        Returns:
            Student: L'oggetto studente creato.
        """
        if course_name not in data:
            raise ValueError(f"Il corso '{course_name}' non esiste")
        
        student = Student(student_name)
        
        # Controlla se la lista "studenti" esiste, inizializza se non esiste
        if "studenti" not in data[course_name]:
             data[course_name]["studenti"] = []

        data[course_name]["studenti"].append(student.to_dict())
        return student

    @staticmethod
    def get_students(data, course_name):
        """
        Restituisce una lista di studenti per un dato corso.
        Args:
            data (dict): La struttura dati principale.
            course_name (str): Il nome del corso.
        Returns:
            list: Lista di oggetti Student.
        """
        if course_name not in data or "studenti" not in data[course_name]:
            return []
        
        return [Student.from_dict(s) for s in data[course_name]["studenti"]]

    @staticmethod
    def update_student(data, course_name, student_id, new_name):
        """
        Aggiorna il nome di uno studente.
        Args:
            data (dict): La struttura dati principale.
            course_name (str): Il nome del corso.
            student_id (str): L'ID dello studente da aggiornare.
            new_name (str): Il nuovo nome dello studente.
        Returns:
            bool: True se aggiornato, False se non trovato.
        """
        if course_name not in data or "studenti" not in data[course_name]:
            return False
            
        if not new_name or not new_name.strip():
             raise ValueError("Il nuovo nome dello studente non può essere vuoto")

        for s_dict in data[course_name]["studenti"]:
            if s_dict["id"] == student_id:
                s_dict["nome"] = new_name
                return True
        return False

    @staticmethod
    def delete_student(data, course_name, student_id):
        """
        Rimuove uno studente da un corso e gestisce le presenze associate.
        Args:
            data (dict): La struttura dati principale.
            course_name (str): Il nome del corso.
            student_id (str): L'ID dello studente da rimuovere.
        Returns:
            bool: True se rimosso, False se non trovato.
        """
        if course_name not in data:
            return False

        # Rimuovi dalla lista degli studenti
        students = data[course_name].get("studenti", [])
        initial_count = len(students)
        data[course_name]["studenti"] = [s for s in students if s["id"] != student_id]
        
        if len(data[course_name]["studenti"]) == initial_count:
            return False # Studente non trovato

        # Pulisci le presenze (registro)
        # Struttura: "registro": { "DATA": { "ID_STUDENTE": "STATO" } }
        registro = data[course_name].get("registro", {})
        for date, presence_dict in registro.items():
            if student_id in presence_dict:
                del presence_dict[student_id]
        
        return True
