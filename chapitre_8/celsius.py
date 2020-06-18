# programme 3 page 98

""" Ce programme fait apparaître une fenêtre avec 2 champs
l'un indique la température en Celsius, et l'autre en Fahrenheit.
Lorsque l'on change une température, cela change l'autre et 
vice versa"""

# importation des modules
from tkinter import *

# définitions de fonctions
def convertFa(event):
    fahrenheit.select_clear()
    f = int(celsius.get())
    f = f * 22
    fahrenheit.insert(0, f)

# ---------- Programme principal ----------
fen = Tk()
Label(fen, text='température en degrés Celsius').grid(row=0, column=0)
Label(fen, text='Température en degrés Fahrenheit').grid(row=1, column=0)
celsius = Entry(fen, fg='red')
celsius.grid(row=0, column=1)
celsius.bind("<Return>", convertFa)
fahrenheit = Entry(fen, fg='green')
fahrenheit.grid(row=1, column=1)

Button(fen, text='Quitter', command=fen.quit).grid(row=2, column=1, sticky=E)

fen.mainloop()
