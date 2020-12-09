# Script qui génère automatiquement un fichier texte avec les tables de multiplication
# de 2 à 30 (chacune d'entre elles contenant 20 termes)

# on commence par créer le fichier
f = open('multiplication.txt', 'w')

# variables pour effectuer les calculs
i, j = 2, 1
while i <= 30:                  # boucle sur le premier chiffre
    while j <= 20:              # boucle sur le second chiffre
        calcul = i * j
        # on écrit le résultat
        f.write(str(i) + " * " + str(j) + " = " + str(calcul) + '\n')
        j += 1                  # incrémentation
    f.write('\n')               # on saute une ligne entre chaque table
    # après chaque boucle de j, on replace j à 1 pour commencer une nouvelle table
    j = 1
    i += 1

# fermeture du fichier
f.close()
