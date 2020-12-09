# Script qui recopie un fichier texte en triplant tous 
# les espaces entre les noms

# on demande le fichier source
fichierSource = input("Indiquez le fichier source : ")

# on test l'existence du fichier source
try:
    f = open(fichierSource, 'r')
    f.close()
except:
    print("Le fichier demandé n'existe pas !!!")
else:
    # si le fichier source existe
    fichierDest = input("Indiquez un fichier de destination : ")        # on demande un fichier de destination
    f = open(fichierSource, 'r')                                        # on l'ouvre
    texte = f.read()
    semiTexte = texte.split(" ")                                        # on coupe le texte au niveau des espaces
    i = 1
    resultat = semiTexte[0]

    # boucle pour traverser la variable semiTexte
    while i < len(semiTexte):
        resultat += "   " + semiTexte[i]                                # on ajoute les 3 espaces
        i += 1
    
    # on ouvre la destination et on écrit à l'intérieur
    fs = open(fichierDest, 'w')
    fs.write(resultat)

    # cloture des deux fichiers
    fs.close()
    f.close()