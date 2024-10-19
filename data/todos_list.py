def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class TodoList():
    id: int = 0
    todos: list
    subscribers: list
    
    def __init__(self):
        self.id = 1
        self.todos = []
        self.subscribers = []
    
    def add_todo(self, todo: str):
        todo = {"title": todo, "id": self.id, "isDone": False}
        self.id = self.id + 1 
        self.todos.append(todo)
        for s in self.subscribers:
            s.update(todo)
        pass
    
    def remove_todo(self, todo_id: int):
        self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
        for s in self.subscribers:
            s.remove(todo_id)
        pass
    
    def subscribe_changes(self, cls):
        self.subscribers.append(cls)
        pass
    
    def unsubscribe(self, cls):
        if cls in self.subscribers:
            self.subscribers.remove(cls)    
        