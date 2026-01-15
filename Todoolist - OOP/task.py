import uuid

class Task:
    def __init__(self, title):
        self.id = str(uuid.uuid4())
        self.set_title(title) 
        self.isComplete = False
        self.taglist : list = []

"""
- la classe tag
    - id (uuid4)
    - name (str)
    -color (str)

  la classe taglibrary
    - lista di tag

    - metodi:
        - aggiungere / creare un tag
        - rimuovere / eliminare una category
        - aggiornare un tag(update che deve riflettersi su tutti i task che lo utilizzano)

    - la classe category
        - id (uuid4)
        - name (str)
        - color (str)

    - la classe categorylibrary
        - lista di category

    - metodi:
        - aggiungere / creare una category
        - rimuovere / eliminare una category
        - aggiornare una category(update che deve riflettersi su tutti i task che lo utilizzano)

    
        """

def get_id_(self):
        """Return the task id"""
        return self.id

def get_title(self) -> str:
        """Return the task title"""
        return self.title
    
def set_title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("new_title must be a str instance.") 
        
        if  not new_title or not new_title.strip():
            raise ValueError("new_title should not be empty.")

        self.title = new_title