# programme 4 page 38
# permet de calculer les intérêts accumulés au bout de 20 ans
# par le placement de 100 € au taux de 4.3%

taux, duree, kdepart = 4.3, 20, 100         # déclaration des variables
compteur = 1                                # création du compteur
capital = kdepart                           # variable capital qui s'incrémentera avec les intérets

# boucle pour calculer les intérêts de chaque année
while compteur <= duree:
    i = capital * (taux / 100)              # calcul de l'intérêt
    capital = capital + i                   # incrémentation du capital
    compteur = compteur + 1

# affichage du résultat
print("Au bout de 20 ans, les interets accumulés seront de",capital - kdepart, "€")