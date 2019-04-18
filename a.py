def labyrinthe(fichier):
    Labyrinthe = []
    with open(fichier, 'r') as une_carte:
        for line in une_carte:
            liste = line.strip()
            Labyrinthe.append(list(liste))
    return Labyrinthe

def afficher_labyrinthe(L):
    for l in L:
        print(''.join(l))

def choisir_direction():
    direction = input('entrez une direction: n(nord), s(sud)'
                              'e(est), o(ouest): ').lower()
    if len(direction)>1 or not direction.isalpha():
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


def verifier_position(i, j, x, y):
    Labyrinthe = labyrinthe('facile.txt')
    if Labyrinthe[i + y][j + x] == 'O':
        print("vous ne pouvez pas aller par là")
    if Labyrinthe[i + y][j + x] == '.':
        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), 'X')
        Labyrinthe[i + y][j + x] = 'X'
        afficher_labyrinthe(Labyrinthe)
    if Labyrinthe[i + y][j + x] == ' ':
        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), 'X')
        Labyrinthe[i + y][j + x] = 'X'
        afficher_labyrinthe(Labyrinthe)

continuer_partie = True

while continuer_partie:
    print("Labyrinthes existants :")
    print("  1 - facile.\n  2 - prison.")

    while True:
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
                if direction == 'n':
                    line, column = position_robot(Labyrinthe, perso)
                    verifier_position(line, column, 0, -1)
                if direction == 's':
                    line, column = position_robot(Labyrinthe, perso)
                    verifier_position(line, column, 0, 1)

def verifier_position(i, j, x, y):
    Labyrinthe = labyrinthe('facile.txt')
    if Labyrinthe[i + y][j + x] == 'O':
        print("vous ne pouvez pas aller par là")
    if Labyrinthe[i + y][j + x] == '.':
        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), 'X')
        Labyrinthe[i + y][j + x] = 'X'
        afficher_labyrinthe(Labyrinthe)
    if Labyrinthe[i + y][j + x] == ' ':
        Labyrinthe = labyrinthe_sans_perso(labyrinthe('facile.txt'), 'X')
        Labyrinthe[i + y][j + x] = 'X'
        afficher_labyrinthe(Labyrinthe)



