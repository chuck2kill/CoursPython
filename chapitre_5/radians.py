# programme 1 page 38
# ce programme vise à convertir en radians un angle fourni au départ en degrés, minutes, secondes

degre, minute, seconde, pi = 68, 18, 44, 3.141592653     # déclaration des variables

# conversion des minutes et secondes en degrés
fsec = seconde / 60
fminute = minute + fsec
fminute = minute / 60
fdegre = degre + fminute

# conversion des degrés en radian
rad = fdegre / (180 / pi)

# affichage de la réponse
print("Pour", degre, "°", minute, "'", seconde, "\", le radian équivaut à",rad)