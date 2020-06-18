# programme 5 page 38
# programme qui sert à afficher le nombre de grains de riz total,
# si on dipose 1 grain sur la 1ere case d'un échiquier, 2 grains
# sur la 2e case, 4 grains sur la 3e case, etc...
# à faire en nombre entier et réel

# déclaration des variables
cases, c, grain, grainFloat = 64, 1, 1, 1.0

# boucle sur chaque case de l'échiquier
while c <= cases:
    grain = grain * 2               # pour chaque case, on multiplie le nombre de grains
    grainFloat = grainFloat * 2     # de riz par 2
    c = c + 1                       # on incrémente le compteur 'c'

# affichage du résultat
print("il y aura", grain, "grains de riz en entier, et", grainFloat, "grains de riz en réel sur la 64e case")