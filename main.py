from tkWindowSetup import *
from q1 import *

window = setupWindow()

q1_canvas = Canvas(window, bg='#EDEDF3', width=1280, height=720)
q1_canvas.pack()

world_map = PIL.ImageTk.PhotoImage(PIL.Image.open('blank map.png'))

q1_canvas.create_image(640, 300, image=world_map)

RunQ1(window, q1_canvas)

window.mainloop()