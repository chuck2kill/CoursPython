# programme 4 page 33
# ce programme vise à calculer les 50 premiers termes de la table de multiplication de 13
# mais il n'affiche que les chiffres qui sont des multiples de 7

table, compteur = 13, 0                 # on initialises les variables table et compteur
while compteur < 50:                    # boucle pour les 50 premiers termes
    compteur = compteur + 1             # on incrémente la variable compteur
    resultat = table * compteur         # calcul du résultat
    if resultat % 7 == 0:               # on affiche le résultat uniquement si c'est un multiple de 7
        print(resultat)