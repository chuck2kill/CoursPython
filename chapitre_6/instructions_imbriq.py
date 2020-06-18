# instructions composées <while> - <if> - <elif> - <else>

print('Choisissez un nombre de 1 à 3 ( ou 0 pour terminer) ', end = ' ')
ch = input()
a = int(ch)                 # conversion de la chaine entrée en entier
while a:                    # équivalent à : < while a != 0: >
    if a == 1:
        print("Vous avez choisi un :")
        print("Le premier, l'unique, l'unité...")
    elif a == 2:
        print("Vous préférez le deux :")
        print("La paire, le couple, le duo...")
    elif a == 3:
        print("Vous optez pour le plus grand des trois :")
        print("Le trio, la trinité, le triplet...")
    else:
        print("Un nombre entre UN et TROIS, s.v.p.")
    print("Choisissez un nombre de 1 à 3 ( ou 0 pour terminer )", end = ' ')
    a = int(input())
print("Vous avez entré zéro :")
print("L'exercice est donc terminé.")
input()