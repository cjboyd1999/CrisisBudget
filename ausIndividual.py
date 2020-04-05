import tkinter
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def AusIndividual(window, canvas):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)
    style.configure("Main.TCheckbutton", font=lato, foreground='#020202', background='#EDEDF3')

    def AusIndExitButton():
        window.destroy()

    def AusIndNextButton():
        canvas.delete("all")
        chk1.place(x=-1000, y=-1000)
        chk2.place(x=-1000, y=-1000)
        chk3.place(x=-1000, y=-1000)
        chk4.place(x=-1000, y=-1000)
        chk5.place(x=-1000, y=-1000)
        chk6.place(x=-1000, y=-1000)
        chk7.place(x=-1000, y=-1000)
        nextBtn.place(x=-1000, y=-1000)
        x = varTrue()
        if x == True:
            canvas.create_text(640, 100, text="You are eligible for A$275 per week\n(paid $550/fortnight for the next 6 months).", justify=CENTER, fill='#020202', font=soleil)
        elif x == False:
            canvas.create_text(640, 100, text="You are ineligible for any COVID-19 financial aid.", justify=CENTER, fill='#020202', font=soleil)
        canvas.create_text(388, 660, text="Progress: 100%", justify=LEFT, fill='#020202', font=lato)
        canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
        canvas.create_rectangle(320, 680, 960, 695, fill='#6558F5', outline='#6558F5')
        exitBtn.place(x=560, y=575)

    def varTrue():
        if var1.get() == 1:
            return True
        elif var2.get() == 1:
            return True
        elif var3.get() == 1:
            return True
        elif var4.get() == 1:
            return True
        elif var5.get() == 1:
            return True
        elif var6.get() == 1:
            return True
        elif var7.get() == 1:
            return True
        else:
            return False

    canvas.create_text(640, 100, text="An Australian individual? Awesome.\nPlease tick any of the boxes if you are receiving any of\ntheir corresponding packages.", justify=CENTER, fill='#020202', font=soleil)

    var1 = IntVar()
    chk1 = Checkbutton(canvas, text='Jobseeker Payment', variable=var1, style='Main.TCheckbutton')
    chk1.place(x=520, y=200)

    var2 = IntVar()
    chk2 = Checkbutton(canvas, text='Youth Allowance', variable=var2, style='Main.TCheckbutton')
    chk2.place(x=520, y=250)

    var3 = IntVar()
    chk3 = Checkbutton(canvas, text='Parent Payment', variable=var3, style='Main.TCheckbutton')
    chk3.place(x=520, y=300)

    var4 = IntVar()
    chk4 = Checkbutton(canvas, text='Austudy', variable=var4, style='Main.TCheckbutton')
    chk4.place(x=520, y=350)

    var5 = IntVar()
    chk5 = Checkbutton(canvas, text='ABSTUDY', variable=var5, style='Main.TCheckbutton')
    chk5.place(x=520, y=400)

    var6 = IntVar()
    chk6 = Checkbutton(canvas, text='Farm Household Allowance', variable=var6, style='Main.TCheckbutton')
    chk6.place(x=520, y=450)

    var7 = IntVar()
    chk7 = Checkbutton(canvas, text='Special Benefits', variable=var7, style='Main.TCheckbutton')
    chk7.place(x=520, y=500)

    nextBtn = Button(canvas, text='FINISH', style='Next.TButton', command=AusIndNextButton)
    nextBtn.place(x=715, y=575);

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=AusIndExitButton)
    exitBtn.place(x=400, y=575);

    canvas.create_text(388, 660, text="Progress: 40%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
    canvas.create_rectangle(320, 680, 576, 695, fill='#6558F5', outline='#6558F5')