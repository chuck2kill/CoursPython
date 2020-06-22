# programme 4 page 98
"""On fait apparaitre une balle avec un bouton dessous.
Lorsque l'on clique sur le bouton, la balle avance jusqu'au bord de l'écran,
puis reviens, et ainsi de suite"""

# Import des modules
from tkinter import *

# définition des fonctions
def avance():                                           # fonction qui permet de faire avancer la balle
    global x, y, step
    if x + 20 >= 500:                                   # si on touche le bord, on inverse le sens de déplacement
        step = -10
    elif x - 20 <= 0:
        step = 10
    x = x + step
    can.coords(balle, x - 20, y - 20, x + 20, y + 20)   # on applique les nouvelles coordonnées de la balle

# ----- Programme principal -----

# création de la fenêtre
fen = Tk()
fen.title('Le jeu de la balle!!!')

# création du canevas
can = Canvas(fen, width=500, height=500, bg='blue')
can.grid(row=0, column=0)

# déclaration des variables globales
step = 10
x, y = 300, 100
# création de la balle
balle = can.create_oval(x - 20, y - 20, x + 20, y + 20, fill='red')

# initialisation des boutons
Button(fen, text='Quitter', fg='white', bg='black', command=fen.quit).grid(row=1)
Button(fen, text='Avancer', command=avance).grid(row=1, sticky=W, padx=10, pady=10)

# boucle d'événements
fen.mainloop()