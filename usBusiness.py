import tkinter
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def UsBusiness(window, canvas):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)
    style.configure("Main.TCheckbutton", font=lato, foreground='#020202', background='#EDEDF3')

    def UsBusExitButton():
        window.destroy()

    def UsBusNextButton():
        canvas.delete("all")
        chk1.place(x=-1000, y=-1000)
        chk2.place(x=-1000, y=-1000)
        chk3.place(x=-1000, y=-1000)
        nextBtn.place(x=-1000, y=-1000)
        amountLabel.place(x=-1000, y=-1000)
        amountEntry.place(x=-1000, y=-1000)
        isValid()
        canvas.create_text(388, 660, text="Progress: 100%", justify=LEFT, fill='#020202', font=lato)
        canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
        canvas.create_rectangle(320, 680, 960, 695, fill='#6558F5', outline='#6558F5')
        exitBtn.place(x=560, y=575)

    def showEarningsInput():
        amountLabel.place(x=150, y=350)
        amountEntry.place(x=550, y=350)

    def generatePay(pay):
        p = pay + (pay * 0.25)
        if p > 10000000:
            return 10000000
        else:
            return p

    def isValid():
        if var1.get() == 1:
            payout = generatePay(int(amountString.get()))
        if var2.get() == 1:
            payout = generatePay(int(amountString.get()))
        if var3.get() == 1:
            payout = generatePay(int(amountString.get()))
        elif var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
            payout = 0

        if payout > 0:
            canvas.create_text(640, 100, text="Your business is eligible for a loan of US${:0,.2f}.".format(payout), justify=CENTER, fill='#020202', font=soleil)
            canvas.create_text(640, 360, text='No payments have to be made on this loan for 6 months.\nIf you maintain your workforce, the government will\nmore or less forive the loan', justify=CENTER, fill='#020202', font=lato)
        else:
            canvas.create_text(640, 100, text="Your business is ineligible for any COVID-19 financial aid.", justify=CENTER, fill='#020202', font=soleil)

    canvas.create_text(640, 100, text="An American business? Awesome.\nPlease tick any of the boxes that you meet the criteria for.", justify=CENTER, fill='#020202', font=soleil)

    var1 = IntVar()
    chk1 = Checkbutton(canvas, text='A company, non-profit, veterans org. or tribal concern with 500 or less employees.', variable=var1, style='Main.TCheckbutton', command=showEarningsInput)
    chk1.place(x=150, y=200)

    var2 = IntVar()
    chk2 = Checkbutton(canvas, text='Self-employed.', variable=var2, style='Main.TCheckbutton', command=showEarningsInput)
    chk2.place(x=150, y=250)

    var3 = IntVar()
    chk3 = Checkbutton(canvas, text='Independent contractor.', variable=var3, style='Main.TCheckbutton', command=showEarningsInput)
    chk3.place(x=150, y=300)

    amountLabel = Label(canvas, text="  Past 8 weeks average prior payroll: ", font=lato, background='#EDEDF3')   
    amountString = StringVar()
    amountEntry = Entry(canvas, width=15, font=lato, textvariable=amountString)

    nextBtn = Button(canvas, text='FINISH', style='Next.TButton', command=UsBusNextButton)
    nextBtn.place(x=715, y=575);

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=UsBusExitButton)
    exitBtn.place(x=400, y=575);

    canvas.create_text(388, 660, text="Progress: 40%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
    canvas.create_rectangle(320, 680, 576, 695, fill='#6558F5', outline='#6558F5')