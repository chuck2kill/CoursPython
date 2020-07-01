# programme 8.27 page 101

"""Programme simulant une balle qui tombe
et qui rebondit selon les lois de
la gravité"""

# import de modules
from tkinter import *

# définition de fonction
def move():
    "déplacement de la balle"
    global x, y, yh, v, dx, flag
    
    v += dx                     # augmentation de la vitesse v
    y += v                      # on ajoute la vitesse v au point y
    if y > 400:
        dx += .1
        y = 400
        v = -v
    
    can.coords(balle, x - 20, y - 20, x + 20, y + 20)
    if flag > 0:
        fen.after(50, move)

def start():
    "Démarrage de l'action"
    global flag
    flag += 1
    if flag == 1:
        move()

def stop():
    "Arrêt de l'action"
    global flag
    flag = 0


#========== Programme principal ==========

# création de la fenêtre
fen = Tk()
fen.title('Balle rebondissante')

# variables globales
x, y, yh, v, dx, flag = 250, 100, 100, 0, 6, 0

# création du canevas
can = Canvas(fen, width=500, height=500, bg='light blue')
canBouton = Canvas(fen)
canBouton.grid(row=0, column=1, sticky=N)
can.grid(row=0, column=0, rowspan=3)

# création des graphiques
sol = can.create_rectangle(0, 400, 500, 500, fill='light green', width=0)
soleil = can.create_oval(400, 20, 450, 70, fill='yellow', width=0)
balle = can.create_oval(x - 20, y - 20, x + 20, y + 20, fill='red', width=2)

# création des boutons
Button(fen, text='Quitter', command=fen.quit, width=10).grid(row=2, column=1, sticky=S)
Button(canBouton, text='Démarrage', command=start, width=10).grid(row=0, column=0, sticky=N)
Button(canBouton, text='Arrêt', command=stop, width=10).grid(row=1, column=0, sticky=N)

# démarrage du réceptionnaire d'événements (boucle principale) :
fen.mainloop()
