# programme 3 page 33
# ce programme affiche les 20 premiers terme de la table de multiplication de 7
# mais il signale également par un astérisque les multiples de 3

table, compteur = 7, 0                                   # affectation de la table de multiplication et du compteur
while compteur < 20:                                     # boucle d'affichage de la table
    compteur = compteur + 1                              # incrémentation du compteur
    resultat = table * compteur                          # calcul du résultat de la multiplication
    if resultat % 3 == 0:                                # condition, si le résultat est un multiple de 3, on affiche
        print(resultat, "*", end = " ")                  # le résultat avec une étoile, sinon, on affiche juste le résultat
    else:
        print(resultat, end = " ")                      
print("\n")                                              # on affiche la table en ligne, donc avec 'end = ""', puis à la fin
                                                         # on affiche un saut de ligne   