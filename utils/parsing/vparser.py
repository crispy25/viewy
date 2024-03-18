from tkinter import ttk
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
top_parent = os.path.dirname(os.path.dirname(current))
sys.path.append(top_parent)

from utils.logging.viewy_logger import VLogger

class VParser:
    
    @staticmethod
    def parse(text: str) -> dict:
        labels = {}

        for line in text.split('\n'):
            if len(line) == 0:
                break
            try:    
                id, value, link = line.split()
                labels[id] = (id, value, link)
            except ValueError:
                VLogger.error("Incorrect config file! Format: (key name link)")
                return {}

        return labels