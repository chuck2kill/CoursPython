# Script qui recopie les données chiffrées
# d'un fichier texte, vers un autre fichier
# texte, mais arrondi

# importation de modules
import os

# on demande d'entrer le chemin du fichier source
fichierSource = input("Entrez le chemin du fichier source : ")

# test d'existence du fichier
try:
    fs = open(fichierSource, 'r')
    fs.close()
except:
    print("Veuillez entrer un chemin de fichier valide !")
    os.system("pause")
else:
    fichierDestination = input("Veuillez entrer le chemin du fichier destination : ")
    fd = open(fichierDestination, 'w')
    fs = open(fichierSource, 'r')
    # lecture du fichier source
    chiffres = fs.read()
    # on sépare tous les chiffres et on les place dans une liste
    chiffreListe = chiffres.split("\n")
    i = 0
    while i < len(chiffreListe):            # pour chaque objet de la liste
        # on transforme en float, on arrondi, puis on reconverti en string
        chiffreListe[i] = str(round(float(chiffreListe[i])))
        i += 1
    
    # on utilise join pour créer une seule variable string, avec le retour chariot
    # comme séparateur
    texte = "\n".join(chiffreListe)
    fd.write(texte)

    # fermeture des fichiers
    fd.close()
    fs.close()
