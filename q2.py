from q3 import *

def RunQ2(window, canvas, country):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)
    style.configure("Choice.TRadiobutton", font=lato, foreground='#020202', background='#EDEDF3')

    if country == 0:
        c = 'Australian'
    elif country == 1:
        c = 'British'
    elif country == 2:
        c = 'American'   

    canvas.create_text(640, 100, text="Okay great! So you're " + c + ", cool!\nNow, are you a small business, or an individual?", justify=CENTER, fill='#020202', font=soleil)

    options = ['Small Business', 'Individual']
    
    v = IntVar(value=-1)

    def activateButton():
        nextBtn.configure(state='normal')
    
    r1 = Radiobutton(canvas, text=options[0], variable=v, value=0, style='Choice.TRadiobutton', command=activateButton)
    r1.place(x=400, y=450)
    r2 = Radiobutton(canvas, text=options[1], variable=v, value=1, style='Choice.TRadiobutton', command=activateButton)
    r2.place(x=700, y=450)

    def Q2ExitButton():
        window.destroy()

    def Q2NextButton():
        canvas.delete("all")
        selectedType = v.get()
        r1.place(x=-1000, y=-1000)
        r2.place(x=-1000, y=-1000)
        nextBtn.place(x=-1000, y=-1000)
        exitBtn.place(x=-1000, y=-1000)
        RunQ3(window, canvas, country, selectedType)

    nextBtn = Button(canvas, text='NEXT', style='Next.TButton', command=Q2NextButton)
    nextBtn.configure(state='disabled')
    nextBtn.place(x=715, y=575);

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=Q2ExitButton)
    exitBtn.place(x=400, y=575);

    canvas.create_text(388, 660, text="Progress: 10%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')
    canvas.create_rectangle(320, 680, 384, 695, fill='#6558F5', outline='#6558F5')