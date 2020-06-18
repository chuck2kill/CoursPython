# programme 2 page 33
# permet de convertir un nombre de secondes en années,
# mois, jours, heures, minutes et secondes

sec = 3601                                  # initialisation de la variable secondes

annees = sec // (60 * 60 * 24 * 30 * 12)    # on cherche le nombre d'années
reste = sec % (60 * 60 * 24 * 30 * 12)      # on garde le reste

mois = reste // (60 * 60 * 24 * 30)         # on cherche le nombre de mois
reste = reste % (60 * 60 * 24 * 30)         # on garde ce qui reste

jours = reste // (60 * 60 * 24)             # on cherche le nombre de jours
reste = reste % (60 * 60 * 24)              # on garde le reste pour calculer la suite

heures = reste // 3600                      # on cherche le nombre d'heures
reste = reste % 3600                        # on garde le reste pour calculer la suite

minutes = reste // 60                       # on cherche les minutes
secondes = reste % 60                       # et le reste correspond aux secondes

# on affiche le résultat avec toutes les variables créées
print("Cela représente", annees, "année(s),", mois, "mois,", jours, "jour(s)", heures, "heure(s),", minutes, "minute(s) et", secondes, "seconde(s) !")