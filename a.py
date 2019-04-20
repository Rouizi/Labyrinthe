import pickle
import os


def labyrinthe(fichier):
    Labyrinthe = []
    with open(fichier, 'r') as une_carte:
        for line in une_carte:
            liste = line.strip()
            Labyrinthe.append(list(liste))
    return Labyrinthe

def afficher_labyrinthe(labyrinthe):
    for line in labyrinthe:
        print(''.join(line))



def choisir_direction():
    direction = input('Entrez une commande: N(Nord), S(Sud), E(Est), O(Ouest),' 
                           'Q(sauvegarder et quitter): ')
    if len(direction)>2 or direction == '' or direction == ' ' or direction == '  ':
        print("Vous n'avez pas saisi une commande valide")
        return choisir_direction()
    if len(direction) == 1:
        if not direction.isalpha():
            print("Vous n'avez pas saisi de lettre")
            return choisir_direction()
        else:
            direction = direction.upper()
            return direction
    if len(direction) == 2:
        if not direction[0].isalpha():
            print("Vous n'avez pas saisi de lettre")
            return choisir_direction()
        elif direction[1].isalpha():
            print("Vous avez saisi plusieurs lettres")
            return choisir_direction()
        else:
            direction = direction[0].upper() + direction[1]
            return direction


def position_robot(un_labyrinthe, wanted):
    for index_line, line in enumerate(un_labyrinthe):
        for index_column, column in enumerate(line):
            if column == wanted:
                l, c = index_line, index_column
    return l, c



def labyrinthe_sans_perso(un_labyrinthe, perso):
    for index_line, line in enumerate(un_labyrinthe):
        for index_column, column in enumerate(line):
            if column == perso:
                un_labyrinthe[index_line][index_column] = ' '
    return un_labyrinthe


continuer_partie = True

while continuer_partie:
    print("Labyrinthes existants :")
    nom_carte = []
    for i, nom_fichier in enumerate(os.listdir("cartes")):
        print(f"  {i + 1} - {nom_fichier}")
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte.append(chemin)
    print(nom_carte)
    choix_labyrinthe = True

    while choix_labyrinthe:
        numero = input('Entrez un numéro de labyrinthe pour commencer à jouer : ')

        try:
            numero = int(numero)
            if numero > len(nom_carte):
                print("Vous avez entrée un numéro invalide")
                continue
            elif numero <= 0:
                print("Vous avez entrée un numéro invalide")
                continue
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            continue
        carte = nom_carte[numero - 1]
        Labyrinthe = labyrinthe(carte)
        afficher_labyrinthe(labyrinthe(carte))
        deplacement = True
        while deplacement:
            direction = choisir_direction()
            perso = 'X'
            line, column = position_robot(Labyrinthe, perso)
            if len(direction) == 1:
                n = 1
            if len(direction) == 2:
                n = int(direction[1])
            if direction[0] == 'E':
                if n > len(Labyrinthe[line]) - column - 1:
                    print("Vous ne pouvez pas faire ça")
                    continue
                liste_du_parcour = []
                for i in range(n + 1):
                    liste_du_parcour.append(Labyrinthe[line][column + i])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas aller par là, il y'a un mur")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(Labyrinthe, perso)
                    Labyrinthe[line][column + n] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(Labyrinthe, perso)[line][column + n] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif direction[0] == 'O':
                if n > column:
                    print("Vous ne pouvez pas faire")
                    continue
                liste_du_parcour = []
                for i in range(n + 1):
                    liste_du_parcour.append(Labyrinthe[line][column - i])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas aller par là, il y'a un mur")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(Labyrinthe, perso)
                    Labyrinthe[line][column - n] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(Labyrinthe, perso)[line][column - n] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif direction[0] == 'N':
                if n > line:
                    print("Vous ne pouvez pas faire ça")
                    continue
                liste_du_parcour = []
                for i in range(n + 1):
                    liste_du_parcour.append(Labyrinthe[line - i][column])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas aller par là, il y'a un mur.")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(Labyrinthe, perso)
                    Labyrinthe[line - n][column] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(Labyrinthe, perso)[line - n][column] == 'U':
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif direction[0] == 'S':
                if n > len(Labyrinthe) - line - 1:
                    print("Vous ne pouvez pas faire ça")
                    continue
                liste_du_parcour = []
                for i in range(n+1):
                    liste_du_parcour.append(Labyrinthe[line + i][column])
                if 'O' in liste_du_parcour:
                    print("Vous ne pouvez pas aller par là, il y'a un mur")
                    continue
                else:
                    Labyrinthe = labyrinthe_sans_perso(Labyrinthe, perso)
                    Labyrinthe[line + n][column] = 'X'
                    afficher_labyrinthe(Labyrinthe)
                    if labyrinthe_sans_perso(Labyrinthe, perso)[line + n][column] == 'U':
                        print("BRAVO vous avez gagnez !!!")
                        deplacement = False
                        choix_labyrinthe = False
                        continuer_partie = False
            elif len(direction) == 2 and direction[0] == 'Q':
                pass
            elif len(direction) == 1 and direction == "Q":
                pass