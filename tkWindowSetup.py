import tkinter
from tkinter import *
from tkinter.ttk import *

def setupWindow():
    window = Tk()
    window.title("Crisis Budget Planner")
    window.configure(bg="#EDEDF3")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    distX = (screen_width - 1280) / 2
    distY = (screen_height - 720) / 2

    window.geometry("1280x720+{}+{}".format(int(distX), int(distY)))
    window.maxsize(1280,720)
    window.minsize(1280,720)

    return window