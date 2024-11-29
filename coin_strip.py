from random import randint
import os

os.system('cls')

lenTab = int(input("Choisissez la longeur du plateau (entre 12 et 24) "))
assert 12 <= lenTab <= 24
tab = [False]*lenTab

nbCoins = int(input("Choisissez le nombre de 'coins' (entre 3 et 6) "))
assert 3 <= nbCoins <= 6

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
    indexCoup = input("Choisissez un coup (case du plateau de jeu) : ")
    try:
        int(indexCoup)
    except:
        coupInvalide(tab, joueur)
    indexCoup = int(indexCoup)
    indexCoup -= 1
    print()
    indexCoin = None
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
    for i in range(lenTab):
        if tab[i]:
            tempTab.append(1)
        else:
            tempTab.append(0)
    print(tempTab)
    for i in range(1, lenTab + 1):
        if i < 10:
            print(f" {i} ", end="")
        else:
            print(f" {i}", end="")
    print()
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
