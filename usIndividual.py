import tkinter
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def UsIndividual(window, canvas):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)
    style.configure("Main.TCheckbutton", font=lato, foreground='#020202', background='#EDEDF3')

    def UsIndExitButton():
        window.destroy()

    def UsIndNextButton():
        canvas.delete("all")
        chk1.place(x=-1000, y=-1000)
        chk2.place(x=-1000, y=-1000)
        chk3.place(x=-1000, y=-1000)
        chk4.place(x=-1000, y=-1000)
        chk5.place(x=-1000, y=-1000)
        nextBtn.place(x=-1000, y=-1000)
        amountLabel.place(x=-1000, y=-1000)
        childrenLabel.place(x=-1000, y=-1000)
        amountEntry.place(x=-1000, y=-1000)
        childrenEntry.place(x=-1000, y=-1000)
        checkEligibility()
        canvas.create_text(388, 660, text="Progress: 100%", justify=LEFT, fill='#020202', font=lato)
        canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
        canvas.create_rectangle(320, 680, 960, 695, fill='#6558F5', outline='#6558F5')
        exitBtn.place(x=400, y=575)

    def showEarningsInput():
        currentY = chk2.winfo_y()
        chk2.place(x=300, y=currentY+50)
        chk3.place(x=300, y=currentY+100)
        chk4.place(x=300, y=currentY+150)
        chk5.place(x=300, y=currentY+200)
        amountLabel.place(x=300, y=currentY)
        amountEntry.place(x=550, y=currentY)
    
    def showChildrenInput():
        currentY = chk3.winfo_y()
        chk3.place(x=300, y=currentY+50)
        chk4.place(x=300, y=currentY+100)
        chk5.place(x=300, y=currentY+150)
        childrenLabel.place(x=300, y=currentY)
        childrenEntry.place(x=550, y=currentY)

    def getPayout(pay):
        if pay <= 75000:
            return 1200
        elif pay > 75000:
            ret = (pay - 75000) / 100
            ret = 1200 - (ret * 5)
            if ret < 0:
                return 0
            else:
                return ret
        else:
            window.destroy()
    

    def checkEligibility():
        pay = 0
        if var1.get() == 1:
            pay += getPayout(int(amountString.get()))
        if var2.get() == 1:
            pay += int(childrenString.get()) * 500
        if var5.get() == 1:
            pay += 600
        if var4.get() == 1:
            pay = 0
        if var3.get() == 0:
            pay = 0

        if pay > 0:
            canvas.create_text(640, 100, text="You are eligible for a payout of US${:0,.2f}.".format(pay), justify=CENTER, fill='#020202', font=soleil)
        else:
            canvas.create_text(640, 100, text="You are ineligible for any COVID-19 financial aid.", justify=CENTER, fill='#020202', font=soleil)

        canvas.create_text(388, 660, text="Progress: 100%", justify=LEFT, fill='#020202', font=lato)
        canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
        canvas.create_rectangle(320, 680, 960, 695, fill='#6558F5', outline='#6558F5')
        exitBtn.place(x=400, y=575)
        

    canvas.create_text(640, 100, text="An American individual? Awesome.\nPlease check any boxes that are relevant to you.", justify=CENTER, fill='#020202', font=soleil)

    var1 = IntVar(value=0)
    chk1 = Checkbutton(canvas, text='Have you completed your 2018-2019 tax return?', variable=var1, style='Main.TCheckbutton', command=showEarningsInput)
    chk1.place(x=300, y=200)

    amountLabel = Label(canvas, text="  2018-2019 income:", font=lato, background='#EDEDF3')   
    amountString = StringVar()
    amountEntry = Entry(canvas, width=15, font=lato, textvariable=amountString)

    var2 = IntVar(value=0)
    chk2 = Checkbutton(canvas, text='Do you have children 16 or under listed as dependent on your tax return?', variable=var2, style='Main.TCheckbutton', command=showChildrenInput)
    chk2.place(x=300, y=250)

    childrenLabel = Label(canvas, text="  Number of children:", font=lato, background='#EDEDF3')   
    childrenString = StringVar()
    childrenEntry = Entry(canvas, width=15, font=lato, textvariable=childrenString)

    var3 = IntVar()
    chk3 = Checkbutton(canvas, text='Do you have a valid social security number?', variable=var3, style='Main.TCheckbutton')
    chk3.place(x=300, y=300)

    var4 = IntVar()
    chk4 = Checkbutton(canvas, text="Are you listed as dependent on your parent's tax return?", variable=var4, style='Main.TCheckbutton')
    chk4.place(x=300, y=350)

    var5 = IntVar()
    chk5 = Checkbutton(canvas, text='Are you receiving unemployment insurance?', variable=var5, style='Main.TCheckbutton')
    chk5.place(x=300, y=400)

    nextBtn = Button(canvas, text='FINISH', style='Next.TButton', command=UsIndNextButton)
    nextBtn.place(x=715, y=575);

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=UsIndExitButton)
    exitBtn.place(x=560, y=575);

    canvas.create_text(388, 660, text="Progress: 40%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
    canvas.create_rectangle(320, 680, 576, 695, fill='#6558F5', outline='#6558F5')