from tkinter import Button
from typing import Callable 

class CustomButton:
    
    button: Button
    
    def __init__(self, frame: Frame, button_text: str, button_command: Callable[[], None]) -> None:
        self.button = Button(frame, text=button_text, command=button_command)
        self.button.pack(side="left", padx=5)