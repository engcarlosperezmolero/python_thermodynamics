from tkinter import *
from tkinter import ttk
import pandas as pd
from buttonfx import *
from combx import *
from entries import *


# ======== Root specs ===========================

root = Tk()
root.title("Thermodynamic Properties calculation (binary system)")
root.geometry("+50+90")
root.resizable(0, 0)
root.config(bg="#000000", bd=0)


frame_1 = Frame(root, width=550, height=1300)
frame_1.config(bg="#404040")
frame_1.pack()

randomspace(frame_1, 0, 0)

randomspace(frame_1, 1, 0)
randomlabel(frame_1, "Component 1:", 1, 1, 2, 2, W)
randomspace(frame_1, 1, 3)
randomlabel(frame_1, "Component 2:", 1, 4, 2, 2, W)
randomspace(frame_1, 1, 7)

combof1(frame_1, 3, 1)
combof2(frame_1, 3, 4)

randomspace(frame_1, 4, 0)

randomlabel(frame_1, "Antoine Constants: ", 5, 1, 2, 1, W)
randomlabel(frame_1, "Antoine Constants: ", 5, 4, 2, 1, W)

cuadro(frame_1, 6, 1, 1)
cuadro(frame_1, 6, 4, 1)

randomspace(frame_1, 7, 0)

randomlabel(frame_1, "Pure Properties: ", 8, 1, 2, 1, W)
randomlabel(frame_1, "Pure Properties: ", 8, 4, 2, 1, W)

cuadro(frame_1, 9, 1, 1)
cuadro(frame_1, 9, 4, 1)


randomspace(frame_1, 10, 0)

randomlabel(frame_1, "Which property would you like to know?", 11, 1, 4, 1, W+E)

randomspace(frame_1, 12, 0)

randombutton(frame_1, "Bubble Pressure", 13, 2, 1, 2, 1, W+E, comm=(lambda root=root: Windowbulbp(root, "Temperature: ", "X1:", "Bubble Pressure")))
randombutton(frame_1, "Dew Pressure", 14, 2, 1, 2, 1, W+E, comm=(lambda root=root: Windowdewp(root, "Temperature: ", "Y1:", "Dew Pressure")))
randombutton(frame_1, "Bubble Temperature", 15, 2, 1, 2, 1, W+E, comm=(lambda root=root: Windowbulbt(root, "Pressure: ", "X1:", "Bubble Temperature")))
randombutton(frame_1, "Dew Temperature", 16, 2, 1, 2, 1, W+E, comm=(lambda root=root: Windowdewt(root, "Pressure: ", "Y1:", "Dew Temperature")))
randombutton(frame_1, "Flash calculations", 17, 2, 1, 2, 1, W+E, comm=(lambda root=root: Windowflash(root, "Temperature: ", "Pressure: ", "Z1:", "Flash Calculations")))

randomspace(frame_1, 18, 0)

root.mainloop()
