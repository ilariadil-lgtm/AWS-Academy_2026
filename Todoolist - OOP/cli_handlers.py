from project import Project
from task import Task
from todolist import Todolist


def get_project_list(todolist: Todolist) -> None:
    """Returns the project list"""
    print("=" * 20)
    print("Lista dei progetti:")
    print("=" * 20)

    todolist.get_projects()


def update_project_name(todolist: Todolist):
    """
    This function contains al the logic related to the update project name process
    """
    print("\n=== Aggiorna Nome Progetto ===")
    get_project_list(todolist)

    id_progetto = input("ID del progetto: ")

    if not id_progetto:
        print("Input non valido.")
        return

    while True:
        new_name = input("Nuovo nome: ")

        if not new_name:
            print("Input non valido.")
            continue

        if todolist.is_project_name_already_exists(new_name):
            print(f"Un oggetto con il nome {new_name} esiste già")
            continue

        try:
            todolist.update_project_name(id_progetto, new_name)

        except (ValueError, TypeError) as e:
            print(f"Errore: {e}")
            return

        print(f"Update eseguito con successo per l'oggetto {id_progetto}")
        break


def add_new_project(todolist: Todolist):
    """
    This functions executes the full process to add a new projects.
    If a project with the same name already exists, it doesn't add the project to the list.
    """
    print("\n=== Aggiungi Nuovo Progetto ===")
    print("=" * 30)

    project_name = input("Nome del progetto: ")

    if not project_name:
        print("Input non valido.")

    if todolist.is_project_name_already_exists(project_name):
        print(f"Un oggetto con il nome {project_name} esiste già")
        return

    try:
        new_project = Project(project_name)
        todolist.add_project(new_project)

    except (ValueError, TypeError) as e:
        print(f"Errore: {e}")
        return

    print(f"il numero di progetti è: {todolist.get_projects_length()}")


def add_new_task(todolist: Todolist):
    print("\n=== Aggiungi Nuova Task ===")
    n = todolist.get_projects_length()
    if n == 0:
        print("Non ci sono progetti.")
        return

    if n == 1:
        project = todolist.get_first_list_project()
    else:
        get_project_list(todolist)
        id_progetto = input(
            "ID progetto di destinazione: "
        ).strip()
        if not id_progetto:
            print("ID non valido.")
            return

        try:
            project = todolist.get_project_by_id(id_progetto)
        except (ValueError, TypeError) as e:
            print(f"Errore: {e}")
            return

        if project is None:
            print("Il progetto non esiste!")
            return

    task_title = input("Titolo della task: ").strip()
    if not task_title:
        print("Titolo non valido.")
        return

    try:
        new_task = Task(task_title)
    except (ValueError, TypeError) as e:
        print(f"Errore: {e}")
        return

    project.add_task(new_task)
    print("Task aggiunta con successo!")


def get_task_list(todolist: Todolist):
    n = todolist.get_projects_length()
    if n == 0:
        print("Non ci sono progetti.")
        return

    if n == 1:
        project = todolist.get_first_list_project()
    else:
        get_project_list(todolist)
        id_progetto = input("ID del progetto: ").strip()
        if not id_progetto:
            print("ID non valido.")
            return
        try:
            project = todolist.get_project_by_id(id_progetto)
        except (ValueError, TypeError) as e:
            print(f"Errore: {e}")
            return
        if project is None:
            print("Il progetto non esiste!")
            return

    print(f"Numero di task: {project.get_tasks_lenght()}")