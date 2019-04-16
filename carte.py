# -*-coding:Utf-8 -*


"""Ce module contient la classe Carte."""


class Carte:
    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, chaine):
        self.ligne_liste = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "{}".format(self.labyrinthe)

    def creer_labyrinthe_depuis_chaine(self, chaine):
        ligne_liste = chaine.split("\n")
        return ligne_liste