# programme 2 page 98

"""Permet de déterminer la force électrostatique de deux
objets, en fonction de leur intensité électrique et 
de leur distance"""

# importation de modules
from tkinter import *

# définiton des fonctions
def part1():
    global i
    i = 0

def part2():
    global i
    i = 1

def pointeur(event):
    can.coords(particule[i], event.x - 5, event.y -5, event.x + 5, event.y + 5)

# ---------- Programme principal ----------
fen = Tk()
fen.title("Loi de coulomb")
i = 3

# libellés
valE1 = Label(fen, text='Particule 1')
valE1.grid(row=1, column=0)
valE2 = Label(fen, text='Particule 2')
valE2.grid(row=1, column=1)

x = [100, 300]
y = [200, 200]
particule = [0]*2

# canevas
can = Canvas(fen, width=400, height=400, bg='light green')
can.grid(row=0, columnspan=3)

particule[0] = can.create_oval(x[0] - 5, y[0] - 5, x[0] + 5, y[0] + 5,
                               fill='red')
particule[1] = can.create_oval(x[1] - 5, y[1] - 5, x[1] + 5, y[1] + 5,
                               fill='blue')


Button(fen, text='Particule rouge', command=part1).grid(row=2, column=0, padx=10, pady=10, sticky=W)
Button(fen, text='Particule bleue', command=part2).grid(row=2, column=1, padx=10, pady=10, sticky=W)
Button(fen, text='Quitter', command=fen.quit).grid(row=2, column=2, sticky=E)

can.bind('<Button-1>', pointeur)

# boucle d'événements
fen.mainloop()
