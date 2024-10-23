from tkinter import Label


class WindowTitle:
    
    def __init__(self, gui: Tk, title: str) -> None:
        self.title = Label(gui, text=title, background="#5cb5ea", font=("Roboto", 16, "bold"))
        self.title.pack(side="top", pady=("20", "50"))