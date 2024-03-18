from tkinter import ttk
import tkinter as tk
import ctypes

 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

class Viewy(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Viewy')
        self.state('zoomed')
        self.config(bg='black')
        self.minsize(width=1000, height=800)

        self.mainloop()

if __name__ == "__main__":
    Viewy()