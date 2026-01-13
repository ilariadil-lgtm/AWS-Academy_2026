from todolist import Todolist
from menu import Menu
from cli_handlers import get_project_list, get_task_list, update_project_name, add_new_project, add_new_task


def main():
    todolist = Todolist()

    menu = Menu()

    while True: 

        menu.printMenu()

        i = input("Seleziona l'operazione da eseguire: ")

        match i:
            case "1": add_new_project(todolist)
            case "2": add_new_task(todolist)
            case "3": print("\n=== Aggiungi Tag ===") 
            case "4": get_project_list(todolist)
            case "5": get_task_list(todolist)
            case "6": print("\n=== Visualizza Tag ===")
            case "7": update_project_name(todolist)
            case "8": break
            case _: print("Input non valido.")


if __name__ == "__main__":
    main()