# programme 6 page 98
"""On fait apparaitre une balle avec un bouton dessous.
Lorsque l'on clique sur le bouton, la balle tourne autour
d'un axe

De plus, une trace est laissée apres le 
passage de la balle"""

# Importation des modules
from tkinter import *
from math import *

# définition des fonctions
def avance():                                           # fonction qui permet de faire avancer la balle
    global x, y, r, t
    px, py = x, y
    x = cx + (r * cos(t))
    y = cy + (r * sin(t))
    t += 0.1
    can.coords(balle, x - 20, y - 20, x + 20, y + 20)   # on applique les nouvelles coordonnées de la balle
    can.create_line(px, py, x, y, fill='red')

# ----- Programme principal -----

# création de la fenêtre
fen = Tk()
fen.title('Le jeu de la balle!!!')

# création du canevas
can = Canvas(fen, width=500, height=500, bg='blue')
can.grid(row=0, column=0)

# déclaration des variables globales
x, y, r, t = 300, 200, 100, 0.
cx, cy = x, y + r
# création de la balle
balle = can.create_oval(x - 20, y - 20, x + 20, y + 20, fill='red')

# initialisation des boutons
Button(fen, text='Quitter', command=fen.quit).grid(row=1)
Button(fen, text='Avancer', command=avance).grid(row=1, sticky=W, padx=10, pady=10)

# boucle d'événements
fen.mainloop()