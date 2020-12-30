# script permettant de compléter la date de naissance et
# le sexe pour chaque personne créée dans l'exercice précédent

def traduire(ch):
    "convertir une ligne du fichier source en liste de données"
    dn = ""                         # chaine temporaire pour extraire les données
    tt = []                         # la liste à produire
    i = 0
    while i < len(ch):
        if ch[i] == "#":
            tt.append(dn)           # on ajoute la donnée à la liste, et
            dn = ""                 # on réinitialise la chaine temporaire
        else:
            dn = dn + ch[i]
        i += 1
    return tt

def encodage(tt):
    "renvoyer la liste tt, complétée avec la date de naissance et le sexe"
    print("*** Veuillez entrer les données (ou <Enter> pour terminer) : ")
    # Affichage des données déjà présentes dans la liste :
    i = 0
    while i < len(tt):
        print(tt[i], end = ' ')
        i += 1
    print()
    while 1:
        daNai = input("Date de naissance : ")
        sexe = input("Sexe (m ou f) : ")
        print(daNai, sexe)
        ver = input("Entrez <Enter> si c'est correct, sinon <n> ")
        if ver == "":
            break
    tt.append(daNai)
    tt.append(sexe)
    return tt
    

def enregistrer(tt):
    "enregistrer les données de la liste tt en les séparant par des <#>"
    i = 0
    while i < len(tt):
        fd.write(tt[i] + "#")
        i += 1
    fd.write("\n")                  # caractère de fin de ligne

fSource = input("Nom du fichier source : ")
fDest = input("Nom du fichier destination : ")
fs = open(fSource, 'r')
fd = open(fDest, 'w')
while 1:
    ligne = fs.readline()
    if ligne == "" or ligne == "\n":
        break
    liste = traduire(ligne)
    liste = encodage(liste)
    enregistrer(liste)

fd.close()
fs.close()