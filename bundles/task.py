from tkinter import *
from typing import Any
from .customButton import CustomButton
from models.subscriber import Subscriber
from data.todos_list import TodoList

class TodoTask(Subscriber):
    task: dict
    
    def __init__(self, gui: Tk, task: dict[str, Any]):    
        super().__init__()
        self.task = task
        self.task_frame = Frame(gui, background="#5cb5ea")
        self.task_frame.pack(side="top", anchor="n", pady=("0", "15"), fill="x") 

        self.task_label = Label(self.task_frame, text=self.task.get("title"), background="#5cb5ea", font=("Roboto", 12))
        self.task_label.pack(side="left", padx=10, expand=True)

        CustomButton(self.task_frame, button_text="Zrobione", button_command=self.action_done)
        CustomButton(self.task_frame, button_text="Edytuj", button_command=self.action_edit)
        CustomButton(self.task_frame, button_text="Usuń", button_command=self.action_delete)
        
    def action_done(self):
        pass
    def action_edit(self):
        pass
    def action_delete(self):
        TodoList().remove_todo(self.task['id'])
        pass
        
    def update(self, *args):
        pass
    
    def remove(self, todo_id: int):
        if todo_id == self.task['id']:
            self.unsubscribe()
            self.task_frame.destroy()
        