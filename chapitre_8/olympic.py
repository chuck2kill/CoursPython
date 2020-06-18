"""Programme qui affiche les 5 anneaux olympiques"""

# importation de modules
from tkinter import *

# définition des fonctions
def cercleBleue():
    can1.create_oval(100, 100, 300, 300, width=5, outline='blue')

def cercleNoire():
    can1.create_oval(300, 100, 500, 300, width=5, outline='black')

def cercleRouge():
    can1.create_oval(500, 100, 700, 300, width=5, outline='red')

def cercleJaune():
    can1.create_oval(200, 200, 400, 400, width=5, outline='yellow')

def cercleVert():
    can1.create_oval(400, 200, 600, 400, width=5, outline='green')


# ----- Programme Principal -----

# création de la fenêtre principale
fen1 = Tk()
# création du canevas (espace de dessin)
can1 = Canvas(fen1, bg='white', height=500, width=800)
can1.pack(side=TOP)                                                 # on affiche le canevas
# création des bouttons
bouBleu = Button(fen1, text='Cercle bleu', command=cercleBleue)
bouNoire = Button(fen1, text='Cercle noir', command=cercleNoire)
bouRouge = Button(fen1, text='Cercle rouge', command=cercleRouge)
bouJaune = Button(fen1, text='Cercle jaune', command=cercleJaune)
bouVert = Button(fen1, text='Cercle vert', command=cercleVert)
bouQuit = Button(fen1, text='Quitter', command=fen1.quit)

# affichage des bouttons
bouBleu.pack(side=LEFT)
bouNoire.pack(side=LEFT)
bouRouge.pack(side=LEFT)
bouJaune.pack(side=LEFT)
bouVert.pack(side=LEFT)
bouQuit.pack(side=RIGHT)

# boucle principale pour réceptionner les événements
fen1.mainloop()

# destruction de la fenêtre
fen1.destroy()
