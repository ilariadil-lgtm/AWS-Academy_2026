import uuid
from task import Task

class Project:
    def __init__(self, name: str):
        self.id = str(uuid.uuid4()) 
        self.set_project_name(name)
        self.task_list = []

    def get_project_id(self):
        """Return the project id"""
        return self.id
    
    def get_tasks_lenght(self) -> int:
        """Return the lenght of the task list"""
        return len(self.task_list)

    def get_project_name(self) -> str:
        "Return the project name"
        return self.name

    def set_project_name(self, new_name:str) -> None:
        """Set the project name (usefull for update)"""

        if not isinstance(new_name, str) :
           raise TypeError("new_name must be a str instance.") 

        if  not new_name or not new_name.strip():
            raise ValueError("new_name should not be empty.") 

        self.name = new_name

    def add_task(self, new_task: Task) -> None:
        self.task_list.append(new_task)