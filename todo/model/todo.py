# TODO: Add code here
class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed: bool = True

    def add_tag(self, tags: list[str]):
        self.tags = tags

    def __str__(self):
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos: dict[int, Todo] = {}

    def add_todo(self, title: str, description:str) -> int:
        code_id = len(self.todos) + 1
        nuevo_todo = Todo(code_id, title, description)
        self.todos[code_id] = nuevo_todo
        return code_id

    def pending_todos(self):
        return


