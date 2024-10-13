import os
from tkinter import *

class MainWindow:
    
    window = Tk()
    window.geometry("800x600")
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_directory, "..", "images", "icon.png")
    
    icon = PhotoImage(file=icon_path)
    
    window.iconphoto(True, icon)
    
    window.title("Lista zadań do zrobienia")
    window.config(background="#5cb5ea")
    
gui = MainWindow().window