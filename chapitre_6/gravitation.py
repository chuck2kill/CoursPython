# programme 8 page 56
# script qui calcule la force de gravitation de 2 masses de
# 10 tonnes, pour des distances qui augmentent suivant une progression 
# géométrique de 2 à partir de 5 cm (0.05m)

# on demande le nombre d'iteration
nb = int(input("Combien d'itérations voulez-vous? :"))
i = 0                                                   # variable compteur
d = 0.05                                                # variable de distance
# boucle de traitement globale
while i < nb:
    g = (6.67*10**-11) * (10000 * 10000) / (d**2)       # formule de calcul de la force
    # affichage de la solution
    print("d =", d, "m :  la force vaut ", g, "N")
    # incrémentation des variables
    d = d * 2
    i = i + 1
    