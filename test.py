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
    direction = input('entrez une direction: n(nord), s(sud)'
                              'e(est), o(ouest): ').lower()
    if not direction.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return choisir_direction()
    else:
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

def verfivier_position(un_labyrinthe, line, column, x, y):
    if un_labyrinthe[line + y][column + x] == 'O':
        print("vous ne pouvez pas aller par là")
        direction = choisir_direction()
    if un_labyrinthe[line + y][column + x] == '.':
        un_labyrinthe[line][column] = ' '
        un_labyrinthe[line + y][column + x] = 'X'
        afficher_labyrinthe(un_labyrinthe)
    if un_labyrinthe[line + y][column + x] == ' ':
        un_labyrinthe[line][column] = ' '
        un_labyrinthe[line + y][column + x] = 'X'
        afficher_labyrinthe(un_labyrinthe)


continuer_partie = True

while continuer_partie:
    print("Labyrinthes existants :")
    print("  1 - facile.\n  2 - prison.")
    choix_labyrinthe = True
    while choix_labyrinthe:
        numero = input('Entrez un numéro de labyrinthe pour commencer à jouer : ')

        try:
            numero = int(numero)
        except ValueError:
            print("vous n'avez pas saisi de nombre.")
        if numero == 1:
            Labyrinthe = labyrinthe('facile.txt')
            afficher_labyrinthe(Labyrinthe)
            deplacement = True
            while deplacement:
                direction = choisir_direction()
                perso = 'X'
                if direction == 'e':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line][column + 1] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line][column + 1] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line][column + 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column + 1] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line][column + 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column + 1] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line][column + 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                if direction == 'o':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line][column - 1] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line][column - 1] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line][column - 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column - 1] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line][column - 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column - 1] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line][column - 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                if direction == 'n':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line - 1][column] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line - 1][column] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line - 1][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line - 1][column] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line - 1][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line - 1][column] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line - 1][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                if direction == 's':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line + 1][column] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line + 1][column] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line + 1][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line + 1][column] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line + 1][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line + 1][column] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), perso)
                        Labyrinthe[line + 1][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                else:
                        print("vous n'avez pas saisi une direction valide")

        if numero == 2:
            Labyrinthe = labyrinthe('prison.txt')
            afficher_labyrinthe(Labyrinthe)
            deplacement = True
            while deplacement:
                direction = choisir_direction()
                perso = 'X'
                if direction == 'e':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line][column + 1] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line][column + 1] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line][column + 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column + 1] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line][column + 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column + 1] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line][column + 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                if direction == 'o':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line][column - 1] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line][column - 1] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line][column - 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column - 1] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line][column - 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line][column - 1] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line][column - 1] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                if direction == len(direction) * 'n':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line - len(direction)][column] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line - len(direction)][column] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line - len(direction)][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line - len(direction)][column] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line - len(direction)][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line - len(direction)][column] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line - len(direction)][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                if direction == len(direction) * 's':
                    line, column = position_robot(Labyrinthe, perso)
                    if Labyrinthe[line + 1][column] == 'O':
                        print("vous ne pouvez pas aller par là")
                        continue
                    if Labyrinthe[line + len(direction)][column] == '.':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line + len(direction)][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line + len(direction)][column] == ' ':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line + len(direction)][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                    if Labyrinthe[line + len(direction)][column] == 'U':
                        Labyrinthe = labyrinthe_sans_perso(labyrinthe('prison.txt'), perso)
                        Labyrinthe[line + len(direction)][column] = 'X'
                        afficher_labyrinthe(Labyrinthe)
                        print("BRAVO vous vaez gagnez !!!")
                        deplacement = False
                else:
                        print("vous n'avez pas saisi une direction valide")

