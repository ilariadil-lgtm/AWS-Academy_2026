"""
menu
todoolist --> entità principale del programma, viene inizializzata per prima
task
project
tag
"""
import uuid

class Task:
    pass

class Tag:
    pass

class Menu:
    
    def printMenu(self) -> None:
        print(f"""
              1. Add Project
              2. Add Task
              3. Add Tag
              4. List Project
              5. List task
              6. List Tags
              7. exit
        """)

class Todoolist:
     def __init__(self):
          self.project = []
    
     def add_project(self, project: Project) -> None:
        self.project.append(project)
    
     def get_projects_lenght(self) -> int:
         return len(self.project)  
     
     def get_projects(self) -> list[Project]:
          for p in self.project:
            return f"{p.id} - {p.name}"
          
     def update_project_name(self, id: str) -> None:
        target = next((project for project in self.projects if project["id"] == id))
        target.set_prject_name ("pippo")
          
class Project:
    def __init__(self,name: str):
         self.id = str(uuid.uuid4())
         self.name = name
         self.task_list = []

    def get_tasks_lenght(self) -> int:
         return len(self.task_list)   

    def get_project_name(self) -> str:
         return self.name      
         
    def set_project_name(self, new_name: str) -> None:
         self.name = new_name

def main():
    todoolist = Todoolist()

    menu = Menu()

    while True:
         
        menu.printMenu()

        i = input("Selezione l'operazione da eseguire")
       
        match i :
            case "1":
                  print("Hai scelto aggiungi progetto")
                  print("="*20)
                  project_name = input("inserisci nome del progetto:")
                  new_project = Project(project_name)
                  todoolist.add_project(new_project)
                  print(todoolist.get_projects_lenght())
                  continue 
            case "2":
                  print("Aggiungi task")
                  continue   
            case "4":
                  id_progetto =  print("Inserisci l'id del progetto da aggiornare:")
                  print(todoolist.update_project_name(id_progetto))
            case "5":
                  print(todoolist.get_projects())
            case "7":
                break
            case _:
                print("Inserisci il valore corretto")
                continue


if __name__ == "__main__":
        main()