import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("eMOBILITY")
        self.window.iconbitmap('./images/CarIcon.ico')
        w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        self.window.geometry("%dx%d+0+0" % (w, h))
        self.window.config(bg='#fcfcfc')
        self.window.res
