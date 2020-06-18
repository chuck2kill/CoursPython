# programme d'affichage de damier page 86

# import de modules
from tkinter import *
from random import randrange

# ---------- Définition de fonctions ----------

def ligneDeCarre(x, y):
    "Fonction permettant d'imprimer une ligne de carrés"
    i = 0
    while i < 5:
        can.create_rectangle(x, y, x + c, y + c, fill='black')  # on imprime une case sur 2 en noir
        i, x = i + 1, x + c * 2

def damier():
    "Fonction pour remplir le damier"
    i, j = 0, 0
    # boucle sur chaque ligne, à une ligne on commence directement à gauche, et
    # à la suivante, on commence une case plus loin
    while i < 10:
        if i % 2 == 0:
            j = 0
        else:
            j = 1
        ligneDeCarre(j * c, i * c)
        i += 1

def cercle(x1, y1):
    "Fonction pour créer un cercle"
    can.create_oval(x1, y1, x1 + c, y1 + c, fill='red')

def pions():
    "Fonction pour créer un pion aléatoirement"
    x = randrange(10)
    y = randrange(10)
    cercle(x * c, y * c)

# ---------- Programme principal --------------

# variable c qui représente la taille d'un coté de carré
c = 30

fen = Tk()
can = Canvas(fen, height=300, width=300, bg='white')
can.pack(side=TOP)
b1 = Button(fen, text='Damier', command=damier)
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(fen, text='pions', command=pions)
b2.pack(side=RIGHT, padx=5, pady=5)
b3 = Button(fen, text='Quitter', command=fen.quit)
b3.pack(side=RIGHT, padx=5, pady=5)

fen.mainloop()

fen.destroy()
