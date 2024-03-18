from tkinter import ttk, Tk
from tkinter import font
import ctypes
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from components.basic_components import *
from utils.parsing.vparser import VParser
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

class Viewy(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Viewy')
        self.state('zoomed')
        self.config(bg='black')
        self.minsize(width=1000, height=800)

        self.custom_font = font.Font(family='Comic Sans', size=20)
        self.main_frame = VMainFrame(master=self)
        self.config_text = VConfigText(master=self, font=self.custom_font) 
        self.config_bar = VConfig(master=self)
       
        self.update_main_frame(self.config_text.text)
        self.bind("<Key>", self.handle_input)

        self.mainloop()

    def handle_input(self, event) -> None:
        if event.keysym == 'Escape':
            self.quit()
        elif not self.config_text.text_showing:
            self.main_frame.select(event.keysym)     

    def update_main_frame(self, text: str) -> None:
        parsed_text = VParser.parse(text)

        def new_label(master, line_id, value, link):
            return VLabel(master, line_id, value, link,
                    text=f'{line_id} {value}', 
                    background='#14120a', foreground='white', 
                    font=self.custom_font,
                    )

        for key in parsed_text.keys():
            parsed_text[key] = new_label(self.main_frame.labels_frame, *parsed_text[key])

        self.main_frame.update(parsed_text) 
