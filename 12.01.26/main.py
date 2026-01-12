""" 
class Formina:
    def __init__(self, nome_forma: str):
        self.forma = nome_forma (stellina, cuoricino)

    

biscotto1 = Formina("cuoricino")
biscotto2 = Formina("stellina")

print(biscotto1.forma)
print(biscotto2.forma) 
"""

class Persona:

    def __init__(self, nome: str, cognome: str = "", isEdgemonyPartecipant: bool = False):
        self.nome = nome
        self.cognome = cognome
        self.isEdgemonyPartecipant = isEdgemonyPartecipant

    def printIsEdgemonyPartecipant(self) -> None: 
        print(f"{self.nome} {self.cognome}: {self.isEdgemonyPartecipant}")


class Corso: 
    def __init__(self, nome):
        self.nome = nome
        self.partecipants = []

    def addPartecipant(self, p: Persona) -> bool:
        if p.isEdgemonyPartecipant:
            self.partecipants.append(f"{p.nome} {p.cognome}")
            return True
        
        else: 
            return False
        

    
persona1 = Persona("Claudia", "Nigro", True)
persona2 = Persona("Valeria", "Angioj", True)
persona3 = Persona("Maria", "Rossi", False)

corso1 = Corso("Edgemony")

plist = [persona1, persona2, persona3]

for p in plist:
    print(f"Prima: {corso1.partecipants}")
    print(corso1.addPartecipant(p))
    print(f"Dopo: {corso1.partecipants}")