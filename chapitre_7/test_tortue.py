from random import *

from dessins_tortue import *

goto(0, 0)
taille = 10
espace = 2
couleur = 'red'
angle = 0
i = 0

while i < 9:
    etoile6(taille, couleur, angle)
    up()
    forward(espace)
    down()
    carre(taille, couleur, angle)
    up()
    forward(espace)
    down()
    etoile5(taille, couleur, angle)
    up()
    forward(espace)
    down()
    triangle(taille, couleur, angle)
    up()
    forward(espace)
    down()
    i = i + 1
    left(60)
    taille = taille * 1.2
input()
