from tkinter import *
from .task import TodoTask
from data.todos_list import TodoList

class TaskList:
    
    def __init__(self, gui: Tk):    
        self.task_frame = Frame(gui, background="#5cb5ea")
        self.task_frame.pack(side="top", anchor="n", pady=("0", "15"), fill="x") 
        for todo in TodoList().todos:
            TodoTask(self.task_frame, todo)