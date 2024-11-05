import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tktooltip import ToolTip

def infoPanel (scooter):
    topScooter = Toplevel()
    topScooter.title('Electric Scooters')
    topScooter.iconbitmap('./images/CarIcon.ico')
    topScooter.geometry('600x600')
    topScooter.config(bg='pink')
    utl.center_window(topScooter,600,600)
    
    if scooter == 1:
        sc1 = utl.read_Image('./images/scooter/City.png',(200,170))
        sc1lbl = Label(topScooter,image=sc1,bd=0)
        sc1lbl.place()
