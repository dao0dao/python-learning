from tkinter import *
from .task import TodoTask
from data.todos_list import TodoList
from models.subscriber import Subscriber

class TaskList(Subscriber) :
    
    def __init__(self, gui: Tk):    
        super().__init__()
        self.task_frame = Frame(gui, background="#5cb5ea")
        self.task_frame.pack(side="top", anchor="n", pady=("0", "15"), fill="x") 
        for todo in TodoList().todos:
            TodoTask(self.task_frame, todo)
            
    def update(self, todo):
        TodoTask(self.task_frame, todo)
    
        
            
    def remove(self, *args):
        pass