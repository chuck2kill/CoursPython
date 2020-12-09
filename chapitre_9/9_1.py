# Script permettant de créer et de relire un fichier texte
# le programme doit d'abord demander d'entrer le nom du fichier
# Ensuite, il propose au choix d'enregistrer du nouveau texte ou
# d'afficher le contenu

import os

# On demande le chemin du fichier
fichier = input("Entrez le chemin de votre fichier:\n")

# Test sur l'existence du fichier
try:
    f = open(fichier, 'r')              # test si on peut lire le fichier (donc existe-t-il)
    f.close()                           # fermeture du fichier
except:
    print("Ce fichier n'éxiste pas")    # s'il n'existe pas, on affiche un message
    os.system("pause")
else:                                   # s'il existe, on demande si on veut lire ou écrire
    action = input("Voulez vous écrire à la suite, ou simplement lire? écrire(E)/lire(L) :  ")
    if action == "E" or action == "e":  # si on écrit
        f = open(fichier, 'a')          # on ouvre en mode append(ajout écriture)
        phrase = input("Entrez votre phrase:\n")
        f.write(phrase + '\n')          
        while phrase != "":             # tant qu'on écrit quelque chose, on peut continuer à écrire de nouvelles lignes
            phrase = input()
            f.write(phrase + '\n')
        f.close()                       # fermeture du fichier
        os.system("pause")
    elif action == "L" or action == "l":# si on veut lire
        f = open(fichier, 'r')          # on ouvre le fichier en lecture
        while 1:                        # boucle pour lire par blocs de 50 caractères
            txt = f.read(50)
            if txt == "":               # s'il n'y a plus rien à lire, 
                break                   # on sort de la boucle
            print(txt)                  # affichage du text
        f.close()                       # fermeture du fichier
        os.system("pause")
    