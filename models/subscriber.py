from abc import ABC, abstractmethod
from data.todos_list import TodoList

class Subscriber(ABC):
    
    def __init__(self):    
        TodoList().subscribe_changes(self)
    
    @abstractmethod
    def update(self, action: str, todo: dict):
        pass
    
    @abstractmethod 
    def remove(self, todo_id: int):
        pass
    
    def unsubscribe(self):
        TodoList().unsubscribe(self)
        pass