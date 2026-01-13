from project import Project


class Todolist:
    def __init__(self):
        self.projects: list[Project] = []

    def add_project(self, project: Project) -> None:
        """Add single project to a to project list"""
        if project is None:
            raise ValueError("Project should not be empty.")
        self.projects.append(project)

    def get_projects_length(self) -> int:
        """Return the number of projects inside the project list"""
        return len(self.projects)

    def get_projects(self) -> None:
        """Return the project formatted with <id - project name>"""
        for p in self.projects:
            print(f"{p.id} - {p.name}")

    def is_project_name_already_exists(self, new_name: str) -> bool:
        """Return True if project name already exists, instead return False"""
        if not new_name or not new_name.strip():
            return False

        normalized_new = new_name.strip().casefold()

        for p in self.projects:
            tmp_project_name = p.get_project_name()
            if (
                tmp_project_name
                and tmp_project_name.strip().casefold() == normalized_new
            ):
                return True

        return False

    def get_project_by_id(self, project_id: str) -> Project | None:
        if not isinstance(project_id, str):
            raise TypeError("id must be a str instance.")

        if not project_id or not project_id.strip():
            raise ValueError("Id should not be empty.")

        return next(
            (
                project
                for project in self.projects
                if project.get_project_id() == project_id
            ),
            None,
        )

    def update_project_name(self, project_id: str, new_name: str) -> None:
        """Update the project name based on his id"""

        if not isinstance(project_id, str) or not isinstance(new_name, str):
            raise TypeError("id or new_name must be a str instance.")

        if (
            not project_id
            or not project_id.strip()
            or not new_name
            or not new_name.strip()
        ):
            raise ValueError("Id or new_name should not be empty.")

        project = self.get_project_by_id(project_id)

        if project is None:
            raise ValueError(f"Project with following {project_id} does not exists.")

        project.set_project_name(new_name)

    def get_first_list_project(self) -> Project:
        if not self.projects:
            raise IndexError("No projects available.")
        return self.projects[0]