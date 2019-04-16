# -*-coding:Utf-8 -*


"""Ce module contient la classe Labyrinthe."""

import os

os.chdir("C:/Python/Labyrinthe/roboc")

from carte import *


class Labyrinthe(Carte):
    """Classe représentant un labyrinthe."""

    def __init__(self, chaine):

        self.robot = "X"
        self.mur = "O"
        self.porte = "."
        self.sortie = "U"
        self.liste_passage = []
        self.labyrinthe = ""
        Carte.__init__(self, chaine)

    def commandes(self, commande):

        try:

            if commande.lower() == "q":

                print("Vous avez sauvegardé et quittez la partie")

            elif commande.lower() == "n":

                for indice, ligne in enumerate(self.ligne_liste):

                    ligne_affiche = " "

                    if self.robot in ligne:

                        indice -= 1

                        if indice < 0:
                            raise IndexError("")

                        if True in self.liste_passage:

                            indice += 1
                            ligne_affiche = "."
                            ligne_principale = self.ligne_liste[indice]
                            ligne_principale = list(ligne_principale)
                            ligne_indice = ligne.index(self.robot)
                            indice -= 1
                            ligne_nord = self.ligne_liste[
                                indice]  # ligne_nord est la ligne au dessus de la liste principale
                            if ligne_nord[ligne_indice] == self.mur:
                                pass
                            else:
                                indice += 1
                                if ligne_nord[ligne_indice] == self.sortie:
                                    self.liste_passage.append(self.sortie)
                                ligne_principale[
                                    ligne_indice] = ligne_affiche  # Si on se déplace à nouveau, le "." réapparait à sa position initiale
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne principale 2 est une chaîne de caractère
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On modifié directement dans notre liste de départ notre ligne principale par notre ligne principale avec un "."
                                self.liste_passage.pop(0)  # On enlève passage de la liste
                                passage_2 = 4
                                self.liste_passage.append(passage_2)
                                indice -= 1

                        ligne_nord = self.ligne_liste[
                            indice]  # ligne_nord est la ligne au dessus de la liste principale
                        ligne_indice = ligne.index(
                            self.robot)  # ligne_indice est égal à la position du robot dans la liste
                        ligne_affiche = ligne_nord[
                            ligne_indice]  # ligne_affiche pointe sur l'indice où était placé le robot une ligne plus bas

                        if ligne_affiche == self.mur:

                            print("Vous ne pouvez pas aller par là, il y a un mûr")

                        else:

                            if ligne_affiche == self.porte:
                                ligne_affiche = " "
                                passage = True
                                self.liste_passage.append(passage)

                            indice += 1

                            if not 4 in self.liste_passage:

                                ligne_principale = self.ligne_liste[indice]  # ligne_principale où est X
                                ligne_principale = list(ligne_principale)  # ligne_principale devient une liste
                                if ligne_affiche == self.sortie:
                                    ligne_principale[ligne_indice] = " "
                                    self.liste_passage.append(self.sortie)
                                else:
                                    ligne_principale[
                                        ligne_indice] = ligne_affiche  # On retire le robot de sa position initial
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne_principale_2 est la ligne principale sans le X
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On met notre ligne principale sans X dans notre liste de départ

                            else:

                                if self.sortie in self.liste_passage:
                                    self.liste_passage.clear()
                                    self.liste_passage.append(self.sortie)
                                else:
                                    self.liste_passage.pop(0)

                            indice -= 1

                            ligne_nord = list(ligne_nord)  # ligne_nord devient une liste
                            ligne_nord[
                                ligne_indice] = "X"  # On place le robot sur l'indice de la ligne nord d'où il était placé une ligne plus bas
                            ligne_nord_2 = "".join(ligne_nord)  # ligne_nord_2 est la ligne_nord avec le robot
                            self.ligne_liste[
                                indice] = ligne_nord_2  # On modifie directement dans notre liste de départ notre ligne nord par notre ligne nord avec le robot

            elif commande.lower() == "e":

                for indice, ligne in enumerate(self.ligne_liste):

                    ligne_affiche = " "

                    if self.robot in ligne:

                        if True in self.liste_passage:

                            ligne_affiche = "."
                            ligne_indice = ligne.index(
                                self.robot)  # ligne_indice est égal à la position du robot dans la liste
                            ligne_principale = self.ligne_liste[indice]  # ligne_principale où est X
                            ligne_principale = list(ligne_principale)  # ligne_principale devient une liste
                            if ligne_principale[ligne_indice + 1] == self.mur:
                                pass
                            else:
                                ligne_principale[
                                    ligne_indice] = ligne_affiche  # Si on se déplace à nouveau, le "." réapparait à sa position initiale
                                if ligne_principale[ligne_indice + 1] == self.sortie:
                                    self.liste_passage.append(self.sortie)
                                ligne_principale[
                                    ligne_indice + 1] = self.robot  # On met le robot une case à droite de sa position initiale
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne principale 2 est une chaîne de caractère
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On modifié directement dans notre liste de départ notre ligne principale par notre ligne principale avec un "."
                                self.liste_passage.pop(0)  # On enlève passage de la liste
                                passage_2 = 4
                                self.liste_passage.append(passage_2)

                        ligne_principale = self.ligne_liste[indice]  # ligne_principale où est X
                        ligne_indice = ligne.index(
                            self.robot)  # ligne_indice est égal à la position du robot dans la liste
                        ligne_affiche = ligne_principale[
                            ligne_indice + 1]  # ligne_affiche pointe un indice à droite du robot

                        if ligne_affiche == self.mur:

                            print("Vous ne pouvez pas aller par là, il y a un mûr")

                        else:

                            if ligne_affiche == self.porte:
                                ligne_affiche = " "
                                passage = True
                                self.liste_passage.append(passage)

                            if not 4 in self.liste_passage:

                                ligne_principale = list(ligne_principale)  # ligne_principale devient une liste
                                if ligne_affiche == self.sortie:
                                    ligne_principale[ligne_indice] = " "
                                    self.liste_passage.append(self.sortie)
                                else:
                                    ligne_principale[
                                        ligne_indice] = ligne_affiche  # On retire le robot de sa position initial

                                ligne_principale[
                                    ligne_indice + 1] = self.robot  # On met le robot un indice à côté d'où il était à l'origine
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne_principale_2 est la ligne principale modifié
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On met notre ligne principale modifié dans notre liste de départ

                            else:
                                if self.sortie in self.liste_passage:
                                    self.liste_passage.clear()
                                    self.liste_passage.append(self.sortie)
                                else:
                                    self.liste_passage.pop(0)

            elif commande.lower() == "s":

                for indice, ligne in enumerate(self.ligne_liste):

                    ligne_affiche = " "

                    if self.robot in ligne:

                        indice += 1

                        if True in self.liste_passage:

                            indice -= 1
                            ligne_affiche = "."
                            ligne_principale = self.ligne_liste[indice]
                            ligne_principale = list(ligne_principale)
                            ligne_indice = ligne.index(self.robot)
                            indice += 1
                            ligne_sud = self.ligne_liste[
                                indice]  # ligne_sud est la ligne en dessous de la liste principale
                            if ligne_sud[ligne_indice] == self.mur:
                                pass
                            else:
                                indice -= 1
                                if ligne_sud[ligne_indice] == self.sortie:
                                    self.liste_passage.append(self.sortie)
                                ligne_principale[
                                    ligne_indice] = ligne_affiche  # Si on se déplace à nouveau, le "." réapparait à sa position initiale
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne principale 2 est une chaîne de caractère
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On modifié directement dans notre liste de départ notre ligne principale par notre ligne principale avec un "."
                                self.liste_passage.pop(0)  # On enlève passage de la liste
                                passage_2 = 4
                                self.liste_passage.append(passage_2)
                                indice += 1

                        ligne_sud = self.ligne_liste[indice]  # ligne_sud est la ligne en dessous de la liste principale
                        ligne_indice = ligne.index(
                            self.robot)  # ligne_indice est égal à la position du robot dans la liste
                        ligne_affiche = ligne_sud[
                            ligne_indice]  # ligne_affiche pointe sur l'indice où était placé le robot une ligne plus haut

                        if ligne_affiche == self.mur:

                            print("Vous ne pouvez pas aller par là, il y a un mûr")

                        else:

                            if ligne_affiche == self.porte:
                                ligne_affiche = " "
                                passage = True
                                self.liste_passage.append(passage)

                            indice -= 1

                            if not 4 in self.liste_passage:

                                ligne_principale = self.ligne_liste[indice]  # ligne_principale où est X
                                ligne_principale = list(ligne_principale)  # ligne_principale devient une liste
                                if ligne_affiche == self.sortie:
                                    ligne_principale[ligne_indice] = " "
                                    self.liste_passage.append(self.sortie)
                                else:
                                    ligne_principale[
                                        ligne_indice] = ligne_affiche  # On retire le robot de sa position initial
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne_principale_2 est la ligne principale sans le X
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On met notre ligne principale sans X dans notre liste de départ

                            else:

                                if self.sortie in self.liste_passage:
                                    self.liste_passage.clear()
                                    self.liste_passage.append(self.sortie)
                                else:
                                    self.liste_passage.pop(0)

                            indice += 1

                            ligne_sud = list(ligne_sud)  # ligne_sud devient une liste
                            ligne_sud[
                                ligne_indice] = "X"  # On place le robot sur l'indice de la ligne sud d'où il était placé une ligne plus haut
                            ligne_sud_2 = "".join(ligne_sud)  # ligne_sud2 est la ligne_sud avec le robot
                            self.ligne_liste[
                                indice] = ligne_sud_2  # On modifie directement dans notre de départ notre ligne sud par notre ligne sud avec le robot
                            break

            elif commande.lower() == "o":

                for indice, ligne in enumerate(self.ligne_liste):

                    ligne_affiche = " "

                    if self.robot in ligne:

                        if True in self.liste_passage:

                            ligne_affiche = "."
                            ligne_indice = ligne.index(
                                self.robot)  # ligne_indice est égal à la position du robot dans la liste
                            ligne_principale = self.ligne_liste[indice]  # ligne_principale où est X
                            ligne_principale = list(ligne_principale)  # ligne_principale devient une liste
                            if ligne_principale[ligne_indice - 1] == self.mur:
                                pass
                            else:
                                if ligne_principale[ligne_indice - 1] == self.sortie:
                                    self.liste_passage.append(self.sortie)
                                ligne_principale[
                                    ligne_indice - 1] = self.robot  # On met le robot une case à gauche de sa position initiale
                                ligne_principale[
                                    ligne_indice] = ligne_affiche  # Si on se déplace à nouveau, le "." réapparait à sa position initiale
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne principale 2 est une chaîne de caractère
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On modifié directement dans notre liste de départ notre ligne principale par notre ligne principale avec un "."
                                self.liste_passage.pop(0)  # On enlève passage de la liste
                                passage_2 = 4
                                self.liste_passage.append(passage_2)

                        ligne_principale = self.ligne_liste[indice]  # ligne_principale où est X
                        ligne_indice = ligne.index(
                            self.robot)  # ligne_indice est égal à la position du robot dans la liste
                        ligne_indice -= 1
                        if ligne_indice < 0:
                            raise IndexError("")
                        ligne_affiche = ligne_principale[
                            ligne_indice]  # ligne_affiche pointe un indice à gauche du robot
                        ligne_indice += 1

                        if ligne_affiche == self.mur:

                            print("Vous ne pouvez pas aller par là, il y a un mûr")

                        else:

                            if ligne_affiche == self.porte:
                                ligne_affiche = " "
                                passage = True
                                self.liste_passage.append(passage)

                            if not 4 in self.liste_passage:

                                ligne_principale = list(ligne_principale)  # ligne_principale devient une liste
                                if ligne_affiche == self.sortie:
                                    ligne_principale[ligne_indice] = " "
                                    self.liste_passage.append(self.sortie)
                                else:
                                    ligne_principale[
                                        ligne_indice] = ligne_affiche  # On retire le robot de sa position initial

                                ligne_principale[
                                    ligne_indice - 1] = self.robot  # On met le robot un indice à côté d'où il était à l'origine
                                ligne_principale_2 = "".join(
                                    ligne_principale)  # ligne_principale_2 est la ligne principale modifié
                                self.ligne_liste[
                                    indice] = ligne_principale_2  # On met notre ligne principale modifié dans notre liste de départ

                            else:

                                if self.sortie in self.liste_passage:
                                    self.liste_passage.clear()
                                    self.liste_passage.append(self.sortie)
                                else:
                                    self.liste_passage.pop(0)

        except IndexError:

            print("Vous ne pouvez pas aller par là")

        compteur = 0
        self.labyrinthe = ""

        while compteur != len(self.ligne_liste):
            self.labyrinthe += self.ligne_liste[compteur] + "\n"
            compteur += 1

        if self.sortie in self.liste_passage:
            self.labyrinthe += "\n"
            self.labyrinthe += "\n"
            self.labyrinthe += "Félicitations ! Vous avez gagné !"