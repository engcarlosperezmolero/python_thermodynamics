"""Script for the buttons function: DT, BT, DP & BP
   (open a new window, with a new console and entries."""

from tkinter import *
import tkinter as tk
from entries import *


def randomspace(parent, vr, vc):
    return Label(parent, text="            ", bg="#404040").grid(row=vr, column=vc)


def randomlabel(parent, txtt, vr, vc, vcs, vpdy, vst):
    label_1 = Label(parent, text=txtt, bg="#404040", fg="#FFFFFF", font=("Arial", 12))
    label_1.grid(row=vr, column=vc, columnspan=vcs, pady=vpdy, sticky=vst)
    return label_1


def randombutton(parent, txtb, vr, vc, vrs, vcs, vpdy, vst, comm):
    button_1 = Button(parent, text=txtb, fg="#CCC9DC", bg="#324A5F", cursor="hand2", command=comm)
    button_1.grid(row=vr, column=vc, rowspan=vrs, columnspan=vcs, pady=vpdy, sticky=vst)
    return button_1


def randomentry(parent, vr, vc, vcs, vpdy, vst):
    entry_1 = Entry(parent)
    entry_1.grid(row=vr, column=vc, columnspan=vcs, pady=vpdy, sticky=vst)


def cuadro1(parent, r, c, rs, cs):
    label = Label(parent, font=24)
    label.config(bg="dark slate gray", fg="white", width=28, height=17, bd="2", relief="solid", justify=LEFT)
    label.grid(row=r, column=c, rowspan=rs, columnspan=cs, ipadx=0, sticky=W)
