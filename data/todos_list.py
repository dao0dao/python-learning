def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class TodoList():
    id: int
    todos: list
    subscribers: list
    
    def __init__(self):
        self.id = 1
        self.todos = []
        self.subscribers = []
    
    def add_todo(self, todo: str):
        self.todos.append({"title": todo})
        for s in self.subscribers:
            s.update()
        pass
    
    def subscribe_changes(self, cls):
        self.subscribers.append(cls)
        pass