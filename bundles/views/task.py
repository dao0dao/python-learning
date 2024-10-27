from tkinter import Frame, Label, Tk, Entry
from typing import Any
from .customButton import CustomButton
from models.subscriber import Subscriber
from data.todos_list import TodoList

class TodoTask(Subscriber):
    task: dict
    
    def __init__(self, gui: Tk, task: dict[str, Any]):    
        super().__init__()
        self.task = task
        self.is_edited = False
        self.task_frame = Frame(gui, background="#5cb5ea")
        self.task_frame.pack(side="top", anchor="n", pady=("0", "15"), fill="x") 

        self.task_title_frame = Frame(self.task_frame, background="#5cb5ea")
        self.task_title_frame.pack(side="left", fill="x")         
        
        self.task_label = Label(self.task_title_frame, text=self.task.get("title"), background="#5cb5ea", font=("Roboto", 12))
        self.task_label.pack(side="left", padx=10, expand=True)
        
        self.task_entry = Entry(self.task_title_frame, font=('Roboto', 12))
        self.task_entry.pack(side="left", expand="True", padx=10)
        self.task_entry.pack_forget()

        CustomButton(self.task_frame, button_text="Zrobione", button_command=self.action_done)
        
        self.edit_frame = Frame(self.task_frame, background="#5cb5ea")
        self.edit_frame.pack(side="left", fill="none") 
        
        self.button_edit = CustomButton(self.edit_frame, button_text="Edytuj", button_command=self.action_edit)
        self.button_change = CustomButton(self.edit_frame, button_text="Zastosuj", button_command=self.action_change)
        self.button_change.pack_forget()
        
        CustomButton(self.task_frame, button_text="Usuń", button_command=self.action_delete)
        
    def action_done(self):
        pass
    
    def action_edit(self):
        self.button_edit.pack_forget()
        self.button_change.pack()
        
        self.task_label.pack_forget()
        
        self.task_entry.insert(0, self.task.get('title'))
        self.task_entry.pack()
        
        pass
    
    def action_change(self):
        self.task['title'] = self.task_entry.get()
        TodoList().edit_todo(self.task)
        
        self.button_change.pack_forget()
        self.task_entry.pack_forget()
        
        self.task_label.config(text=self.task.get("title"))
        
        self.button_edit.pack()
        self.task_label.pack()
        pass
    
    def action_delete(self):
        TodoList().remove_todo(self.task['id'])
        pass
        
    def update(self, **kwargs):
        pass
    
    def remove(self, todo_id: int):
        if todo_id == self.task['id']:
            self.unsubscribe()
            self.task_frame.destroy()
        