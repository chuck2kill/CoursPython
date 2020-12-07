from tkinter import *
from random import randrange

# === Définition de quelques gestionnaires d'événements : =======================================================

def start_it():
    "Démarrage de l'animation"
    global flag
    if flag == 0:
        flag = 1
        move()

def stop_it():
    "Arrêt de l'animation"
    global flag
    flag = 0

def new_ball():
    "Apparation d'une nouvelle balle"
    global canX, canY, cc, can, ballX, ballY, flag, balle
    ballX, ballY = randrange(0 + 20, canX - 20), randrange(0 + 20, canY - 20)
    balle = can.create_oval(ballX, ballY, ballX + cc, ballY + cc, fill='yellow')

def go_left(event =None):
    "Déplacement vers la gauche"
    global dx, dy, sens
    dx, dy = -1, 0
    sens = 0

def go_right(event =None):
    "Déplacement vers la droite"
    global dx, dy, sens
    dx, dy = 1, 0
    sens = 2

def go_up(event =None):
    "Déplacement vers le haut"
    global dx, dy, sens
    dx, dy = 0, -1
    sens = 1

def go_down(event =None):
    "Déplacement vers le bas"
    global dx, dy, sens
    dx, dy = 0, 1
    sens = 3

def move():
    "Animation du serpent par récursivité"
    global flag, serp, y, x
    # Principe du mouvement opéré : on déplace le carré de queue, dont les
    # caractéristiques sont mémorisées dans le premier élément de la liste
    # <serp>, de manière à l'amener en avant du carré de tête, dont les
    # caractéristiques sont mémorisées dans le dernier élément de la liste.
    # On définit ainsi un nouveau carré de tête pour le serpent, dont on
    # mémorise les caractéristiques en les ajoutant à la liste.
    # Il ne reste plus qu'à effacer alors le premier élément de la liste,
    # et ainsi de suite...
    c = serp[0]                 # extraction des infos concernant le carré de queue
    cq = c[0]                   # ref. de ce carré (coordonnées inutiles ici)
    l = len(serp)               # longueur actuelle du serpent (=n. de carrés)
    c = serp[l - 1]             # extraction des infos concernant le carré de tête
    xt, yt = c[1], c[2]         # coordonnées de ce carré
    # Préparation du déplacement proprement dit.
    # (cc est la taille du carré. dx & dy indiquent le sens du déplacement) :
    xq, yq = xt + dx * cc, yt + dy * cc         # coord. du nouveau carré de tête
    # Vérification : a-t-on atteint les limites du canvas ? :
    if xq < 0 or xq > canX - cc or yq < 0 or yq > canY - cc:
        flag = 0                # => arrêt de l'animation
        can.create_text(canX / 2, 20, anchor=CENTER, text="Perdu !!!",
                        fill="red", font="Arial 14 bold")
    can.coords(cq, xq, yq, xq + cc, yq + cc)    # Déplacement effectif
    serp.append([cq, xq, yq])                   # Mémorisation du nouveau carré de tête
    del(serp[0])                                # effacement (retrait de la liste)

    if (can.bbox(balle)[0] in range(serp[len(serp) - 1][1], serp[len(serp) - 1][1] + 15) or can.bbox(balle)[2] in range(serp[len(serp) - 1][1], serp[len(serp) - 1][1] + 15)) and (can.bbox(balle)[1] in range(serp[len(serp) - 1][2], serp[len(serp) - 1][2] + 15) or can.bbox(balle)[3] in range(serp[len(serp) - 1][2], serp[len(serp) - 1][2] + 15)):
            can.delete(balle)
            new_ball()
            longueur = len(serp)
            x = serp[0][1]
            y = serp[0][2]
            if sens == 0:
                x = x + cc
                carre = can.create_rectangle(x , y, x + cc, y + cc, fill="green")
                serp.insert(0, [carre, x, y])
            elif sens == 2:
                x = x - cc
                carre = can.create_rectangle(x , y, x + cc, y + cc, fill="green")
                serp.insert(0, [carre, x, y])
            elif sens == 1:
                y = y + cc
                carre = can.create_rectangle(x , y, x + cc, y + cc, fill="green")
                serp.insert(0, [carre, x, y])
            else:
                y = y - cc
                carre = can.create_rectangle(x , y, x + cc, y + cc, fill="green")
                serp.insert(0, [carre, x, y])

    # Appel récursif de la fonction par elle-même (=> boucle d'animation)
    if flag > 0:
        fen.after(100, move)
        

    # ===== Programme principal ================================================================================

# Variables globales modifiables par certaines fonctions :
flag = 0                            # commutateur pour l'animation
dx, dy = 1, 0                       # indicateurs pour le sens de déplacement
sens = 2                            # variable qui détermine le sens de déplacement

# Autres variables globales :
canX, canY = 500, 500                                                       # dimensions du canvas
x, y, cc = 100, 100, 15                                                     # coordonnées et coté du premier carré
ballX, ballY = randrange(0 + 20, canX - 20), randrange(0 + 20, canY - 20)   # coordonnées de la première balle


# Création de l'espace de jeu :
fen = Tk()
can = Canvas(fen, bg='dark grey', height=canX, width=canY)
can.pack(padx=10, pady=10)
bou1 = Button(fen, text='Start', width=10, command=start_it)
bou1.pack(side=LEFT, padx=10, pady=10)
bou2 = Button(fen, text='Stop', width=10, command=stop_it)
bou2.pack(side=LEFT, padx=10, pady=10)
bou3 = Button(fen, text='Quitter', width=10, command=fen.quit)
bou3.pack(side=RIGHT, padx=10, pady=10)

# Réation de la balle à attraper
balle = can.create_oval(ballX, ballY, ballX + cc, ballY + cc, fill='yellow')


# Association des gestionnaires d'événements aux touches fléchées du clavier :
fen.bind("<Left>", go_left)         # attention : les événements clavier
fen.bind("<Right>", go_right)       # doivent toujours être associés à la
fen.bind("<Up>", go_up)             # fenêtre principale, et non au canevas
fen.bind("<Down>", go_down)          # ou à au autre widget

# Création du serpent initial (= ligne de 5 carrés).
# on mémorisera les infos concernant les carrés créésdans une liste de listes :
serp = []                           # liste vide
# Création et mémorisation des 5 carrés : le dernier (à droite) est la tête
i = 0
while i < 5:
    carre = can.create_rectangle(x, y, x + cc, y + cc, fill="green")
    # Pour chaque carré, on mémorise une petite sous-liste contenant
    # 3 éléments : la référence du carré et ses coordonnées de base
    serp.append([carre, x, y])
    x = x + cc                      # le carré suivant sera un peu plus à droite
    i = i + 1

fen.mainloop()
    