# programme 1 page 50
# sert à convertir des miles par heure en km/h et en mètres par seconde

# on demande la vitesse en mph
mph = int(input("Veuillez indiquer une vitesse en mp/h :"))

# calcul des vitesses
ms = (mph * 1609) / 3600
kmh = mph * 1.609

# affichage des résultats
print("Une vitesse de", mph, "miles par heure, correspond à", kmh, "km/h et à", ms, "mètres par seconde")
input()