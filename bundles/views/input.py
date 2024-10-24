from tkinter import Frame, Tk, Entry
from .customButton import CustomButton
from data.todos_list import TodoList



class InputTodo:
    def __init__(self, gui: Tk, ) -> None:
        self.task_frame = Frame(gui, background="#5cb5ea")
        self.task_frame.pack(side="top", anchor="center", pady=("0", "15"), fill="x") 
        
        self.title = Entry(self.task_frame, font=('Roboto', 12))
        self.title.pack(side="left", expand="True" ,padx=10)
        
        CustomButton(self.task_frame, button_text="Dodaj", button_command=self.action_add)
        
    def action_add(self):
        TodoList().add_todo(self.title.get())
        self.title.delete(0, len(self.title.get()))

        