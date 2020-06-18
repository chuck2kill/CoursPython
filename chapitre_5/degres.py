# programme 2 page 38
# ce programme servira à convertir un angle donné en radian vers 
# son équivalent en degrés, minutes, secondes

radian, pi = 1, 3.141          # déclaration des variables

# calcul du degré, on supprime le reste et on le garde pour la suite
degre = radian * (180 / pi)
reste = degre % 1
degre = degre - reste

# calcul des minutes, on garde le reste pour les secondes
minute = reste * 60
reste = minute % 1
minute = minute - reste

# calcul des secondes, et on arrondit
seconde = reste * 60
reste = seconde % 1
seconde = seconde - reste

# affichage du résultat
print("un radian de", radian, "équivaut à", degre, "°", minute, "'", seconde, "\"")