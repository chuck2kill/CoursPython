# import de module
from turtle import *


def carre(taille, couleur, angle):
    "Fonction qui dessine un carré de taille et de couleur détérminés à partir"
    "d'un angle de départ"
    color(couleur)
    c = 0
    left(angle)
    while c < 4:                    # il faut 4 cotés
        forward(taille)
        right(90)                   # on tourne à 90°
        c = c + 1
    forward(taille)
    
def triangle(taille, couleur, angle):
    "Fonction qui permet de dessiner un triangle de taille et de couleur déterminés"
    "à partir d'un angle donné"
    color(couleur)
    c = 0
    left(angle)
    while c < 3:                    # il faut 3 cotés
        forward(taille)
        right(120)                  # on tourne à 120°
        c = c + 1
    forward(taille)

def etoile5(taille, couleur, angle):
    "Fonction qui dessine une étoile à 5 branches"
    color(couleur)
    left(angle)
    c = 0
    while c < 5:                    # 5 itérations car 6 branches
        forward(taille)
        right(144)                  # on tourne à 144°
        c = c + 1
    forward(taille)

def etoile6(taille, couleur, angle):
    "Fonction qui dessine une étoile à 6 branches"
    color(couleur)
    left(angle)
    # on utilise la première fonction triangle
    triangle(taille, couleur, angle)
    # on relève le curseur pour se déplacer où l'on veut
    up()
    right(90)
    forward(taille / 2)
    left(90)
    down()
    # on baisse le curseur et on utilise la deuxième
    # fonction triangle
    triangle(taille, couleur, 180)
    up()
    forward(-taille)
    right(90)
    forward(taille / 2)
    right(90)
