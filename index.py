from tkinter import *
from bundles.window import gui
from bundles.title import WindowTitle
from bundles.input import InputTodo
from bundles.task_list import TaskList


class index():   
    def __init__(self) -> None:
        WindowTitle(gui, "Twoja lista zadań")
        InputTodo(gui)
        TaskList(gui)
        
        gui.mainloop()


index()