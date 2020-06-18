# programme 2 page 97
# permet d'afficher une fenêtre avec deux cercles (2 astres)
# deux boutons sont disponibles pour choisir les astres
# et on les fait bouger en cliquant sur le canevas
# sous le canevas, on doit afficher en permanence la distance entre les 2
# astres, ainsi que la force gravitationnelle qu'ils exercent l'un
# sur l'autre. 
#
# on pensera à afficher en haut la masse de chaque astre, ainsi que
# l'échelle des distances

# importation de modules
from tkinter import *
from math import *

# déclaration des fonctions
def astro1():
    global i
    i = 0

def astro2():
    global i
    i = 1

def distance(x1, y1, x2, y2):
    "Distance séparant les points x1,y1 et x2,y2 grâce au théorèmes de pythagore"
    d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d

def forceG(m1, m2, di):
    "Force de gravitation s'exerçant entre m1 et m2 pour une distance di"
    return m1 * m2 * 6.67e-11 / di**2

def pointeur(event):
    can.coords(astre[i], event.x - 10, event.y -10, event.x + 10, event.y + 10)
    x[i] = event.x
    y[i] = event.y
    # calcul de la nouvelle interdistance
    di = distance(x[0], y[0], x[1], y[1])
    # conversion de la distance "écran" en distance "astronomique"
    diA = di * 1e9          # 1pxl = 1 million de km
    # calcul de la force de gravitation correspondante
    f = forceG(m1, m2, diA)
    # affichage des nouvelles valeurs de distance et force
    valDis.configure(text="Distance = " + str(diA) + " m")
    valFor.configure(text="Force = " + str(f) + " N")

# masse des deux astres
m1 = 6e24               # masse de la terre en kg
m2 = 6e24
astre = [0]*2           # liste servant à mémoriser les réf des dessins
x = [50., 350.]         # liste des coordonnées x de chaque astre
y = [100., 100.]        # liste des coordonnées y de chaque astre

# ----- Programme principal -----
fen = Tk()
fen.title('Gravitation universelle selon Newton')
i = 2

# Libellés
valM1 = Label(fen, text="M1 = " + str(m1) + " kg")
valM1.grid(row=1, column=0)
valM2 = Label(fen, text="M2 = " + str(m2) + " kg")
valM2.grid(row=1, column=1)
valDis = Label(fen, text="Distance")
valDis.grid(row=3, column=0)
valFor = Label(fen, text="Force")
valFor.grid(row=3, column=1)
# canevas avec le dessin des 2 astres
can = Canvas(fen, bg="light yellow", width=400, height=200)
can.grid(row=2, column=0, columnspan=2)
astre[0] = can.create_oval(x[0] - 10, y[0] - 10, x[0] + 10, y[0] + 10,
                           fill='red', width=1)
astre[1] = can.create_oval(x[1] - 10, y[1] - 10, x[1] + 10, y[1] + 10,
                           fill='blue', width=1)

# 2 groupes de 4 boutons, chacun installé dans un cadre (frame)
Button(fen, text="Astre rouge", fg='black', command=astro1).grid(row=4, column=0, sticky=W, padx=10)
Button(fen, text="Astre bleu", fg='black', command=astro2).grid(row=4, column=1, sticky=E, padx=10)

can.bind('<Button-1>', pointeur)

# démarrage du réceptionnaire d'événements
fen.mainloop()
