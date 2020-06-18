# Détection et positionnement d'un clic de souris dans une fenêtre

from tkinter import *

def cercle(x, y):
    "Fonction pour créer un cercle"
    cadre.create_oval(x - c, y - c, x + c, y + c, fill='red', outline='')

def pointeur(event):
    chaine.configure(text="Clic détecté en X =" + str(event.x) +\
                            ", Y =" + str(event.y))
    cercle(event.x, event.y)

c = 1
fen = Tk()
cadre = Canvas(fen, width=200, height=150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()

fen.mainloop()
