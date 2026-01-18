class AttendanceManager:
    def __init__(self, data):
        """Inizializza il gestore con il dizionario dei dati."""
        self.data = data

    def mark_attendance(self, course_name, date, status_map):
        """
        Registra le presenze per una data specifica.
        status_map: dizionario {student_id: stato}
        Stati ammessi: 'Presente', 'Assente', 'Ritardo'
        """
        if course_name not in self.data:
            raise ValueError(f"Corso '{course_name}' non trovato.")
        
        if "registro" not in self.data[course_name]:
            self.data[course_name]["registro"] = {}
            
        # Validazione stati
        valid_states = ["Presente", "Assente", "Ritardo"]
        for s_id, state in status_map.items():
            if state not in valid_states:
                 raise ValueError(f"Stato '{state}' non valido per lo studente {s_id}.")

        self.data[course_name]["registro"][date] = status_map

    def get_visual_report(self, course_name, date):
        """
        Genera un report visuale per una data specifica.
        🟢 Presente, 🔴 Assente, ⚠️ Ritardo, ⚪ Non segnato
        """
        if course_name not in self.data:
            return f"Corso '{course_name}' non trovato."
        
        students = self.data[course_name].get("studenti", [])
        registry = self.data[course_name].get("registro", {}).get(date, {})
        
        icons = {
            "Presente": "🟢",
            "Assente": "🔴",
            "Ritardo": "⚠️"
        }
        
        report = [f"--- Report Presenze: {course_name} ({date}) ---"]
        
        if not students:
            report.append("Nessun studente iscritto.")
            return "\n".join(report)

        for student in students:
            s_id = student["id"]
            s_name = student["nome"]
            status = registry.get(s_id, "Non segnato")
            icon = icons.get(status, "⚪")
            report.append(f"{icon} {s_name} ({status})")
            
        return "\n".join(report)