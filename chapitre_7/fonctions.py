# import de modules
from math import *

# fonction 1 page 70
# permet d'afficher un nombre n de caractères ca dans une chaine
def ligneCar(n, ca):
    i = 0
    chaine = ""
    while i < n:
        chaine = chaine + ca
        i = i + 1
    return chaine

# fonction 2 page 70
# calcule l'aire d'un cercle de rayon r
def surfCercle(r):
    return pi * r**2

# fonction 3 page 70
# calcule la multiplication de 3 arguments
def volBoite(x1=-1, x2=-1, x3=-1):
    if x1 == -1:
        return x1
    elif x2 == -1:
        return x1**3
    elif x3 == -1:
        return x1 * x1 * x2
    else:
        return x1 * x2 * x3
# fonction 4 page 70
# détermine le plus grand nombre de la liste d'arguments
def maximum(n1, n2, n3):
    x = n1
    if x < n2:
        x = n2
    if x < n3:
        x = n3
    return x

# fonction 2 page 71
def compteCar(ca, ch):
    "Fonction définissant le nombre de caractères 'ca' dans la chaine 'ch'"
    i = 0
    resultat = 0
    while i < len(ch):
        if ch[i] == ca:
            resultat = resultat + 1
        i = i + 1
    return resultat

# fonction 3 page 71
def indexMax(liste):
    "Fonction qui renvoie l'index de la valeur la plus élevée de la liste"
    i = 0
    index = 0
    chiffre = 0
    while i < len(liste):
        if chiffre < liste[i]:
            chiffre = liste[i]
            index = i
        i = i + 1
    return index

# fonction 4 page 71
def nomMois(n):
    "Fonction qui permet de retrouver le nom d'un mois grâce au numéro"
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 
            'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return mois[n - 1]

# fonction 5 page 71
def inverse(ch):
    "Fonction qui inverse l'ordre des caractères d'une chaine 'ch'"
    i = len(ch)
    chaine2 = ""
    while i > 0:
        chaine2 = chaine2 + ch[i - 1]
        i = i - 1
    return chaine2

# fonction 6 page 71
def compteMot(ph):
    """Fonction qui compte le nombre de mots dans une phrase, en considérant que les mots sont 
    séparés par des espaces"""
    mots = 0
    i = 0
    while i < len(ph):
        if ph[i] == " ":
            mots = mots + 1
        i = i + 1
    return mots + 1

def question(annonce, essais=4, please='oui ou non, s.v.p.!'):
    while essais > 0:
        reponse = input(annonce)
        if reponse in ('o', 'oui', 'O', 'Oui', 'OUI'):
            return 1
        if reponse in ('n', 'non', 'N', 'Non', 'NON'):
            return 0
        print(please)
        essais = essais - 1

def changeCar(ch, ca1, ca2, debut=0, fin=-1):
    """Fonction qui permet de remplacer 'ca1' par 'ca2', dans la chaine de 
    caractères 'ch'.
    debut et fin permettent de savoir à partir d'où commencer
    et où finir. Ces 2 arguments sont optionnels"""
    nch, i = "", 0
    if fin == -1:
        fin = len(ch)
    while i < len(ch):
        if i >= debut and ch[i] == ca1 and i <= fin:
            nch = nch + ca2
        else:
            nch = nch + ch[i]
        i = i + 1
    return nch

def eleMax(liste, debut=0, fin=-1):
    """Fonction qui donne la plus grande valeur de la liste transmise.
    Les arguments debut et fin permettent de savoir où la recherche
    doit s'effectuer"""
    i = 0
    if fin == -1:
        fin = len(liste)
    while debut < fin:
        if i < liste[debut]:
            i = liste[debut]
        debut = debut + 1
    return i

# programme main

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(eleMax(serie, fin=3, debut=1))
