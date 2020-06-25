# programme 8 page 98
"""Ce programme va afficher un canevas avec des rectangles jaunes
représentant un passage pour piéton, sur une route.

Le passage sera bordé de 4 points rouges ou vert.

Un bouton présent permettra d'inverser les couleurs des points
qui représentent des feux tricolores"""

# importation des modules
from tkinter import *

# définition des fonctions
def switch():
    global x, y
    # on échange les emplacements des coordonnées rouge et vert
    x = [x[1], x[0], x[3], x[2]]
    y = [y[1], y[0], y[3], y[2]]
    # on applique les changements
    can.coords(feu1, x[0] - 15, y[0] - 15, x[0] + 15, y[0] + 15)
    can.coords(feu2, x[1] - 10, y[1] - 10, x[1] + 10, y[1] + 10)
    can.coords(feu3, x[2] - 15, y[2] - 15, x[2] + 15, y[2] + 15)
    can.coords(feu4, x[3] - 10, y[3] - 10, x[3] + 10, y[3] + 10)

# ---------- Programme Principal ----------

# création de la fenêtre
fen = Tk()
fen.title('Passage piéton')

# déclaration de variables
px, py = 110, 125
x = [80, 420,420, 80 ]          # listes avec les coordonnées
y = [105, 105, 395, 395]        # des feux tricolores

# création du canevas et des graphiques
can = Canvas(fen, width=500, height=500, bg='white')
can.grid(row=0, column=0, columnspan=2)
route = can.create_rectangle(100, 0, 400, 500, fill='grey')
while px < 400:
    can.create_rectangle(px, py, px+40, py+250, fill='yellow')
    px += 60
feu1 = can.create_oval(x[0] - 15, y[0] - 15, x[0] + 15, y[0] + 15, fill='red')
feu2 = can.create_oval(x[1] - 10, y[1] - 10, x[1] + 10, y[1] + 10, fill='green')
feu3 = can.create_oval(x[2] - 15, y[2] - 15, x[2] + 15, y[2] + 15, fill='red')
feu4 = can.create_oval(x[3] - 10, y[3] - 10, x[3] + 10, y[3] + 10, fill='green')

# création des boutons
Button(fen, text='Switcher les feux', command=switch).grid(row=1, column=0, padx=10, pady=10, sticky=W)
Button(fen, text='Quitter', command=fen.quit).grid(row=1, column=1, padx=10, pady=10, sticky=E)

# boucle d'événements
fen.mainloop()
