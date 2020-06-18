# programme 5 page 56
# l'utilisateur entre une note sur un total
# et grace à un système prédéfini, on lui
# donne une lettre correspondante

# on demande la note à l'utilisateur
print("Veuillez entrer votre note et la base de notation séparés par une virgule")
note = list(eval(input()))

# calcul du pourcentage
pourcent = (int(note[0]) / int(note[1])) * 100

# affichage de la vrai note avec des conditions
if pourcent >= 80:
    print("Votre note est A")
elif pourcent >= 60:
    print("Votre note est B")
elif pourcent >= 50:
    print("Votre note est C")
elif pourcent >= 40:
    print("Votre note est D")
else:
    print("Votre note est E")