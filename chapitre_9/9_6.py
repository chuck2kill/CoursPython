# Script qui compare les contenus de 2 fichiers
# et qui signale la première différence rencontrée

# importation de module
import os

# il faut entrer les 2 fichiers à comparer
fichier1 = input("Entrez le chemin du premier fichier à comparer : ")
fichier2 = input("Entrez le chemin du second fichier à comparer : ")

# test d'existence des fichiers
try:
    f1 = open(fichier1, 'r')
    f2 = open(fichier2, 'r')
    f1.close()
    f2.close()
except:
    print("Vous devez entrer des chemins de fichiers valides. Recommencez s'il vous plaît.")
    os.system("pause")
else:
    f1, f2 = open(fichier1, 'r'), open(fichier2, 'r')
    texte1, texte2 = f1.read(), f2.read()
    # on determine la longueur du plus petit fichier
    longueur = len(texte2)
    if len(texte1) < len(texte2):
        longueur = len(texte1)
    i = 0

    # boucle qui va comparer chaque caractère
    while i < longueur:
        if texte1[i] != texte2[i]:
            # s'il y a une différence
            print("La première différence se situe au caractère " + str(i + 1))
            break           # on sort de la boucle
        i += 1

    # on ferme les 2 fichiers
    f1.close()
    f2.close()

    # pause
    os.system("pause")