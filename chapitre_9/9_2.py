# Script permettant de déterminer la phrase la plus longue
# dans un fichier texte donné

# importation de modules
import os

# on récupère le nom du fichier
fichier = input("Veuillez entrer le chemnin de votre fichier : ")

# test d'existence du fichier
try:
    f = open(fichier, 'r')
    f.close()
except:
    print("le fichier " + fichier + " n'existe pas")
    os.system("pause")
else:
    f = open(fichier, 'r', encoding="utf-8")
    texte = f.read()
    sousTexte = texte.split('.')
    i = 1
    resultat = sousTexte[0]
    while i < len(sousTexte):
        if len(sousTexte[i]) > len(resultat):
            resultat = sousTexte[i]
        i += 1
    f.close()

    print("La phrase la plus longue du fichier " + fichier + " est : " + resultat + ". Cette phrase comporte " + str(len(resultat)) + " caractères.")
    os.system("pause")