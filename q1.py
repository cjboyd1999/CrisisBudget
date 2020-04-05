from q2 import *

def RunQ1(window, canvas):
    soleil = Font(family="Soleil", size=26)
    lato = Font(family="Lato", size=18)

    style = Style()
    style.configure("Next.TButton", background='#6558F5', foreground='#020202', font=lato)
    style.configure("Exit.TButton", background='#D3455B', foreground='#020202', font=lato)

    aus_map = PIL.ImageTk.PhotoImage(PIL.Image.open('aus map.png'))
    uk_map = PIL.ImageTk.PhotoImage(PIL.Image.open('uk map.png'))
    us_map = PIL.ImageTk.PhotoImage(PIL.Image.open('us map.png'))

    def ChangeMap(event): 
        if combox.current() == 0:
            canvas.create_image(640, 300, image=aus_map)
            nextBtn.configure(state='normal')
        elif combox.current() == 1:
            canvas.create_image(640, 300, image=uk_map)
            nextBtn.configure(state='normal')
        elif combox.current() == 2:
            canvas.create_image(640, 300, image=us_map)
            nextBtn.configure(state='normal')

    canvas.create_text(640, 100, text="Hello, welcome to the Crisis Budget planner.\nGet started by selecting the country you are residing in.", justify=CENTER, fill='#020202', font=soleil)

    choices = ['Australia', 'United Kingdom', 'United States of America']
    variable = StringVar(window)
    variable.set('Australia')

    window.option_add("*TCombobox*Listbox*Font", lato)
    combox = Combobox(window, values=choices, font=lato, width=20, state='readonly')
    combox.place(x=490, y=450)

    combox.bind("<<ComboboxSelected>>", ChangeMap)

    def Q1ExitButton():
        window.destroy()

    def Q1NextButton():
        canvas.delete("all")
        combox.place(x=-1000, y=-1000)
        nextBtn.place(x=-1000, y=-1000)
        exitBtn.place(x=-1000, y=-1000)
        selectedCountry = combox.current()
        RunQ2(window, canvas, selectedCountry)

    nextBtn = Button(canvas, text='NEXT', style='Next.TButton', command=Q1NextButton)
    nextBtn.configure(state='disabled')
    nextBtn.place(x=715, y=575);

    exitBtn = Button(canvas, text='EXIT', style='Exit.TButton', command=Q1ExitButton)
    exitBtn.place(x=400, y=575);

    canvas.create_text(388, 660, text="Progress: 0%", justify=LEFT, fill='#020202', font=lato)
    canvas.create_rectangle(320, 680, 960, 695, fill='#90929C', outline='#90929C')