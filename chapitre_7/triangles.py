# programme 1 page 61
# permet d'afficher des triangles de plusieurs couleurs
# avec le module turtle

# import de module
from turtle import *
from random import *

# création de la fonction
def triangle(couleur):              # définition de la fonction avec argument
    penup()                         # on leve le curseur
    # on determine la position de départ au hasard et on place le curseur 
    # à cet endroit
    x = randrange(-200, 200)
    y = randrange(-200, 200)
    goto(x, y)
    pendown()                       # on pose le curseur pour écrire

    # boucle pour écrire le triangle
    i = 0
    while i < 3:
        color(couleur)
        forward(100)
        left(120)
        i = i + 1

# création de la liste avec les couleurs
liste = ['red', 'green', 'black', 'yellow', 'blue', 'purple', 'orange']

# boucle de création des triangles
j = 0
while j < len(liste):
    triangle(liste[j])
    j = j + 1
input()
