# Programme 8.28 page 101

"""Une balle se déplace aléatoirement sur une feuille en rebondissant sur les cotés.
Le joueur doit cliquer sur la balle pour avoir un point.
Mais à chaque clic réussi, la balle accélère.

Arrêter le jeu après un certain nombre de clics et afficher le score atteint."""

# importation de modules
from tkinter import *
from random import *

# définition des fonctions
def move():
    global x, y, xMax, yMax, flag, dx, dy, v
    y += dy
    x += dx

    if y > 480:
        y = 480
        dy = randrange(-10, -1)
    elif y < 20:
        y = 20
        dy = randrange(1, 10)
    if x > 480:
        x = 480
        dx = randrange(-10, -1)
    elif x < 20:
        x = 20
        dx = randrange(1, 10)   
    
    can1.coords(balle, x - 20, y - 20, x + 20, y + 20)
    if flag == 1:
        fen.after(v, move)

def start():
    global flag
    flag += 1
    if flag == 1:
        move()

def stop():
    global flag
    flag = 0

def compte(event):
    global clic, score, v
    clic += 1
    if event.x < x + 20 and event.x > x - 20 and event.y < y + 20 and event.y > y - 20:
        score += 1
        v -= 15
    if clic >= 10:
        stop()
        scoreF = Label(fen, text='score = ' + str(score), width=50)
        scoreF.grid(row=0, column=0)

#========== Programme prinscipal ==========
fen = Tk()
fen.title('Clique la balle 1.0')

# déclaration des variables
xMax, yMax = 500, 500
x, y = xMax / 2, yMax / 2
dx, dy = randrange(1, 10), randrange(1, 10)
v = 100
flag = 0
clic, score = 0, 0

# création des canevas
can1 = Canvas(fen, width=xMax, height=yMax, bg='blue')
can1.grid(row=0, column=0, rowspan=2)
can2 = Canvas(fen)
can2.grid(row=0, column=1, sticky=N)

# Affichage de la balle
balle = can1.create_oval(x - 20, y - 20, x + 20, y + 20, fill='orange', width=1)

# création des boutons
Button(can2, text='Démarrer', command=start, width=10).grid(row=0, column=0, padx=10, pady=5)
Button(can2, text='Arrêter', command=stop, width=10).grid(row=1, column=0, padx=10, pady=5)
Button(fen, text='Quitter', command=fen.quit, width=10).grid(row=1, column=1, padx=10, pady=10, sticky=S)

can1.bind('<Button-1>', compte)
 
# démarrage du réceptionnaire d'événements (boucle principale) :
fen.mainloop()