import os
import pickle

def labyrinthe(fichier):
    """cette fonction ouvre le fichier qui contient le labyrinthe
    et met tous les elements du labyrinthe dans une liste sous forme
    de string"""

    Labyrinthe = []
    with open(fichier, 'r') as une_carte:
        for line in une_carte:
            liste = line.strip()# on enlève les sauts de line
            Labyrinthe.append(list(liste))
    return Labyrinthe

def afficher_labyrinthe(labyrinthe):
    """cette fonction nous affiche le labyrinthe tel qu'il est fans
    les fichier .txt, elle prend en paramètre la fonction labyrinthe(fichier),
    c'est-à-dire le labyrinthe mis dans la liste Labyrinthe"""

    for line in labyrinthe:
        print(''.join(line))

def enregistrer_partie(carte):
    """Cette fonction se charge d'enregistrer le labyrinthe dans le fichier
    labyrinthe. Elle reçoit en paramètre la carte à enregistrer."""

    with open(os.getcwd() +'\\cartes\\labyrinthe', "wb") as fichier_labyrinthe:
        mon_pickler = pickle.Pickler(fichier_labyrinthe)
        mon_pickler.dump(carte)

def choisir_direction():
    """cette fonction se charge de résoudre tous les cas possible de direction"""

    direction = input('Entrez une commande: N(Nord), S(Sud), E(Est), O(Ouest),' 
                           'Q(sauvegarder et quitter): ')
    if len(direction)>2 or direction == '' or direction == ' ' or direction == '  ':
        print("Vous n'avez pas saisi une commande valide")# on peux faire par exemple n2 pour avancer de 2 cases
        return choisir_direction()                        # vers le nord mais si on fait n12 ou n 15 sa marche pas
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
    """cette fonction nous permet de savoir la position du 'X' dans la carte,
    ceci est utile pour vérifier les cases alentour du robot pour voir si
    il peux aller dans la direction entrer"""

    for index_line, line in enumerate(un_labyrinthe):
        for index_column, column in enumerate(line):
            if column == wanted:
                l, c = index_line, index_column
    return l, c

def labyrinthe_sans_perso(un_labyrinthe, perso):
    """cette fonction enlève le 'X' du labyrinthe, elle est utile pour que si le robot
    passe sur une porte (un '.' dans la carte) la porte se réaffiche si le robot se déplace"""
    for index_line, line in enumerate(un_labyrinthe):
        for index_column, column in enumerate(line):
            if column == perso:
                un_labyrinthe[index_line][index_column] = ' '
    return un_labyrinthe




