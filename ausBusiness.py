import tkinter
import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *

def AusBusiness(window, canvas):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)
    style.configure("Main.TCheckbutton", font=lato, foreground='#020202', background='#EDEDF3')

    def AusBusExitButton():
        window.destroy()

    def AusBusNextButton():
        canvas.delete("all")
        chk1.place(x=-1000, y=-1000)
        chk2.place(x=-1000, y=-1000)
        chk3.place(x=-1000, y=-1000)
        chk4.place(x=-1000, y=-1000)
        chk5.place(x=-1000, y=-1000)
        nextBtn.place(x=-1000, y=-1000)
        x = varTrue()
        if x == True:
            canvas.create_text(640, 100, text="Your business is eligible for a tax-free A$20,000 - A$100,000\ncash boost upon lodgement of an activity statement.\n(Payments will not be made prior to 28 April 2020 but can be lodged).", justify=CENTER, fill='#020202', font=soleil)
        elif x == False:
            canvas.create_text(640, 100, text="Your business is ineligible for any COVID-19 financial aid.", justify=CENTER, fill='#020202', font=soleil)
        canvas.create_text(388, 660, text="Progress: 100%", justify=LEFT, fill='#020202', font=lato)
        canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
        canvas.create_rectangle(320, 680, 960, 695, fill='#6558F5', outline='#6558F5')
        exitBtn.place(x=560, y=575)

    def varTrue():
        if var1.get() == 1 and var2.get() == 1 and var3.get() == 1 and var4.get() == 1 and var5.get() == 1:
            return True
        else:
            return False

    canvas.create_text(640, 100, text="An Australian business? Awesome.\nPlease tick any of the boxes that you meet the criteria for.", justify=CENTER, fill='#020202', font=soleil)

    var1 = IntVar()
    chk1 = Checkbutton(canvas, text='Currently holding an ABN that was active from at latest 12 March 2020.', variable=var1, style='Main.TCheckbutton')
    chk1.place(x=250, y=200)

    var2 = IntVar()
    chk2 = Checkbutton(canvas, text='Small or medium business.', variable=var2, style='Main.TCheckbutton')
    chk2.place(x=250, y=250)

    var3 = IntVar()
    chk3 = Checkbutton(canvas, text='Annual turnover is less than A$50 million.', variable=var3, style='Main.TCheckbutton')
    chk3.place(x=250, y=300)

    var4 = IntVar()
    chk4 = Checkbutton(canvas, text='Made eligible payments that the business is required to withhold.', variable=var4, style='Main.TCheckbutton')
    chk4.place(x=250, y=350)

    var5 = IntVar()
    chk5 = Checkbutton(canvas, text='Lodged 2019 tax return before 12 March 2020 OR:\nMade GST taxable, GST-free or input-taxed sales in a previous tax period.', variable=var5, style='Main.TCheckbutton')
    chk5.place(x=250, y=400)

    nextBtn = Button(canvas, text='FINISH', style='Next.TButton', command=AusBusNextButton)
    nextBtn.place(x=715, y=575);

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=AusBusExitButton)
    exitBtn.place(x=400, y=575);

    canvas.create_text(388, 660, text="Progress: 40%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
    canvas.create_rectangle(320, 680, 576, 695, fill='#6558F5', outline='#6558F5')