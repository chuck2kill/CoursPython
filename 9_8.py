# Script permettant d'enregistrer le nom, prénom,
# adresse, code postal, ville et n° de tel de chaque
# personne dans un fichier texte

# importations
import os

f = open('club.txt', 'a')
a = True
while a:
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    adresse = input("Entrez l'adresse : ")
    code = input("Entrez le code postal : ")
    ville = input("Entrez la ville : ")
    tel = input("Entrez le numéro de téléphone : ")
    liste = [nom, prenom, adresse, code, ville, tel]
    texte = "   ".join(liste)
    f.write(texte)

