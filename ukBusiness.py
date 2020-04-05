import tkinter
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def UkBusiness(window, canvas):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)
    style.configure("Main.TCheckbutton", font=lato, foreground='#020202', background='#EDEDF3')

    def UkBusExitButton():
        window.destroy()

    canvas.create_text(640, 100, text="Sorry, we are unable to calculate a financial aid\nestimation for British businesses at this time.", justify=CENTER, fill='#020202', font=soleil)

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=UkBusExitButton)
    exitBtn.place(x=560, y=575);

    canvas.create_text(388, 660, text="Progress: 100%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
    canvas.create_rectangle(320, 680, 960, 695, fill='#6558F5', outline='#6558F5')