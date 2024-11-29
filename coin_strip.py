from random import randint
from termcolor import colored
import os

lenTab = 0
while lenTab < 12 or lenTab > 24:
    os.system('cls')
    choix = input("Choisissez la longeur du plateau (entre 12 et 24) ")
    try:
        int(choix)
    except:
        continue
    lenTab = int(choix)
tab = [False]*lenTab

nbCoins = 0
while nbCoins < 3 or nbCoins > 6:
    os.system('cls')
    choix = input("Choisissez le nombre de 'coins' (entre 3 et 6) ")
    try:
        int(choix)
    except:
        continue
    nbCoins = int(choix)

aleatoire = None
while aleatoire == None:
    os.system('cls')
    choix = input(
        "Voulez vous que les pièces soient placées aléatoirement sur le plateau de jeu ? (o/n) ")
    if choix == "o":
        aleatoire = True
    elif choix == "n":
        aleatoire = False

if aleatoire:
    listIndex = []
    while len(listIndex) < nbCoins:
        index = randint(1, len(tab)-1)
        if not index in listIndex:
            listIndex.append(index)
    for i in range(nbCoins):
        tab[listIndex[i]] = True
else:
    for i in range(nbCoins):
        tab[-1 - i] = True

joueur = 1


def coinStrip():
    """Fonction principale qui assure l'éxécution du jeu."""
    global joueur
    turn = 1
    fini = False
    while not fini:  # game loop
        os.system('cls')
        affichage(tab, joueur, turn)
        jouerCoup(tab, joueur)
        fini = victoire(tab, joueur)
        if joueur == 1:
            joueur = 2
        else:
            joueur = 1
        turn += 1


def jouerCoup(tab, joueur):
    """Joue le coup de l'utilisateur"""
    print()
    choix = input("Choisissez un coup (case du plateau de jeu) : ")
    try:
        int(choix)
    except:
        coupInvalide(tab, joueur)
        return
    indexCoup = int(choix)
    indexCoup -= 1
    print()
    indexCoin = None
    if not 0 <= indexCoup <= lenTab:
        coupInvalide(tab, joueur)
    if tab[indexCoup]:
        coupInvalide(tab, joueur)

    for i in range(indexCoup + 1, len(tab)):
        if tab[i]:
            indexCoin = i
            break

    if indexCoin == None:
        coupInvalide(tab, joueur)

    tab[indexCoin] = False
    tab[indexCoup] = True
    # TODO: corriger un bug rare qui fait disparaitre la pièce


def coupInvalide(tab: list, joueur):
    """Fait rejouer l'utilisateur"""
    print("Coup invalide, recommencez")
    jouerCoup(tab, joueur)


def affichage(tab: list, joueur: int, turn: int):
    """Fonction qui s'occupe de l'affichage pour l'utilisateur"""
    print(f"Tour n°{turn}")
    print("Plateau de jeu actuel :")
    print()
    tempTab = []
    print("| ", end="")
    for i in range(lenTab):
        if tab[i]:
            print(colored('o', 'red'), end="")
        else:
            print("x", end="")
        print(" | ", end="")
    print()
    for i in range(1, lenTab + 1):
        if i <= 10:
            print(f"  {i} ", end="")
        else:
            print(f" {i} ", end="")
    print()
    input()
    print(f"Au tour du joueur {joueur}.")


def victoire(tab, joueur) -> bool:
    """Vérifie si le joueur gagne"""
    victoire = True
    for i in range(nbCoins):
        if not tab[i]:
            victoire = False
            break
    if victoire:
        print()
        print(f"Le joueur {joueur} a gagné !")
        return True
    return False


coinStrip()
