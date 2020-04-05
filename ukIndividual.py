import tkinter
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def UkIndividual(window, canvas):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)
    style.configure("Main.TCheckbutton", font=lato, foreground='#020202', background='#EDEDF3')

    def UkIndExitButton():
        window.destroy()

    def UkIndNextButton():
        canvas.delete("all")
        chk1.place(x=-1000, y=-1000)
        chk2.place(x=-1000, y=-1000)
        chk3.place(x=-1000, y=-1000)
        nextBtn.place(x=-1000, y=-1000)
        x = varTrue()
        if x == 1:
            canvas.create_text(640, 100, text="You are eligible for 80% of your salary\nup to a maximum of £625 per week.\n(Paid as a lump sum payment every 3 months).", justify=CENTER, fill='#020202', font=soleil)
        elif x == 2:
            canvas.create_text(640, 100, text="You are eligible for 80% of your average\nmonthly profits for the last three years up to a maximum of £625 per week.\n(Paid as a lump sum payment every 3 months).", justify=CENTER, fill='#020202', font=soleil)
        elif x == 3:
            canvas.create_text(640, 100, text="You are ineligible for any COVID-19 financial aid.", justify=CENTER, fill='#020202', font=soleil)
        canvas.create_text(388, 660, text="Progress: 100%", justify=LEFT, fill='#020202', font=lato)
        canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
        canvas.create_rectangle(320, 680, 960, 695, fill='#6558F5', outline='#6558F5')
        exitBtn.place(x=560, y=575)

    def varTrue():
        if var1.get() == 1 and var2.get() == 0 and var3.get() == 1:
            return 1
        elif var1.get() == 0 and var2.get() == 1 and var3.get() == 1:
            return 2
        elif var1.get() == 1 and var2.get() == 1 and var3.get() == 1:
            return 2
        else:
            return 3

    canvas.create_text(640, 100, text="A British individual? Awesome.\nPlease check any boxes that are relevant to you.", justify=CENTER, fill='#020202', font=soleil)

    var1 = IntVar()
    chk1 = Checkbutton(canvas, text='Work in the private sector full-time or part-time.', variable=var1, style='Main.TCheckbutton')
    chk1.place(x=350, y=200)

    var2 = IntVar()
    chk2 = Checkbutton(canvas, text='Self-employed and had a loss of income.', variable=var2, style='Main.TCheckbutton')
    chk2.place(x=350, y=250)

    var3 = IntVar()
    chk3 = Checkbutton(canvas, text='Pay tax through the Pay-As-You-Earn (PAYE) system.', variable=var3, style='Main.TCheckbutton')
    chk3.place(x=350, y=300)

    nextBtn = Button(canvas, text='FINISH', style='Next.TButton', command=UkIndNextButton)
    nextBtn.place(x=715, y=575);

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=UkIndExitButton)
    exitBtn.place(x=400, y=575);

    canvas.create_text(388, 660, text="Progress: 40%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
    canvas.create_rectangle(320, 680, 576, 695, fill='#6558F5', outline='#6558F5')