from tkinter import *
from .task import TodoTask
from data.todos_list import TodoList

class TaskList:
    
    def __init__(self, gui: Tk):    
        TodoList().subscribe_changes(self)
        self.task_frame = Frame(gui, background="#5cb5ea")
        self.task_frame.pack(side="top", anchor="n", pady=("0", "15"), fill="x") 
        for todo in TodoList().todos:
            TodoTask(self.task_frame, todo)
            
    def update(self):
        self.clear_frame()
        for todo in TodoList().todos:
            TodoTask(self.task_frame, todo)
            
    def clear_frame(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        