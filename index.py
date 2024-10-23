from tkinter import *
from bundles.views.window import gui
from bundles.views.title import WindowTitle
from bundles.views.input import InputTodo
from bundles.views.task_list import TaskList


class index():   
    def __init__(self) -> None:
        WindowTitle(gui, "Twoja lista zadań")
        InputTodo(gui)
        TaskList(gui)
        
        gui.mainloop()


index()