# Script permettant d'enregistrer le nom, prénom,
# adresse, code postal, ville et n° de tel de chaque
# personne dans un fichier texte

# ouverture du fichier d'écriture des infos
f = open('club.txt', 'a')
# boucle perpétuelle
while 1:
    # on entre toutes les infos
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    adresse = input("Entrez l'adresse : ")
    code = input("Entrez le code postal : ")
    ville = input("Entrez la ville : ")
    tel = input("Entrez le numéro de téléphone : ")

    # on vérifie si les infos sont exactes
    verif = input("Appuyez sur entrée si les renseignements sont exacts : ")
    # on propose de continuer à entrer des informations
    continuer = input("Voulez-vous entrer d'autres infos? (o/n) ")
    # si les infos sont bonnes, on les écrit dans le fichier
    if verif == "":
        liste = [nom, prenom, adresse, code, ville, tel]
        texte = " # ".join(liste)
        f.write(texte + '\n')
    # si on ne veut pas continuer, on sort de la boucle
    if continuer == 'n' or continuer == 'N':
        break

# fermeture du fichier d'écriture
f.close()
