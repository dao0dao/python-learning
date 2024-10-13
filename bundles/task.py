from tkinter import *
from typing import Any
from .customButton import CustomButton

def action_done():
    pass
def action_edit():
    pass
def action_delete():
    pass


class TodoTask:
    
    def __init__(self, gui: Tk, task: dict[str, Any]):    
        self.task_frame = Frame(gui, background="#5cb5ea")
        self.task_frame.pack(side="top", anchor="n", pady=("0", "15"), fill="x") 

        self.task_label = Label(self.task_frame, text=task.get("title"), background="#5cb5ea", font=("Roboto", 12))
        self.task_label.pack(side="left", padx=10, expand=True)

        CustomButton(self.task_frame, button_text="Zrobione", button_command=action_done)
        CustomButton(self.task_frame, button_text="Edytuj", button_command=action_edit)
        CustomButton(self.task_frame, button_text="Usuń", button_command=action_delete)
        