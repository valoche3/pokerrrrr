import src.Color_class
from src.miseEnPlace import *
import random
import poker
import os
import sys
import pygame
from pourmel import *
from fin_de_petite_partie import *
from combinaisongagnante import détermination_du_vainqueur
from joueur2 import *

pygame.init()


def Partie_de_jeu2():
    partie = Partie2()

    dealer = None
    partie_en_cours = True

    while partie_en_cours:
        # Commence un nouvel partie de jeu
        partie.remise_à_zéro()

        if dealer == None :
            dealer = détermination_premier_dealer(partie.nombre_de_joueurs)
        else:
            dealer = détermination_dealer(dealer)
        print(f"Les mains des joueurs sont : {partie.mains}")
        #print(f"Les cartes du milieu sont : {partie.cartes_du_milieu}")
        present, partie.mises = tour_de_jeu(partie.nombre_de_joueurs, partie.mises, partie.argent, partie.mise_verif, dealer, partie.cartes_du_milieu)
        joueurs_gagnants = détermination_du_vainqueur(present, partie.cartes_du_milieu, partie.mains)
        partie.argent = mise_a_niveau_argent(joueurs_gagnants, partie.argent, partie.mises)
        print(partie.argent)
        partie_en_cours = True if input("Voulez vous continuer : oui ou non") == 'oui' else False
    print(f"Le joueur gagnant est : {gagnants_finaux(partie.argent)}")


class Partie2:
    def __init__(self):
        self.nombre_de_joueurs = récupère_le_nombre_de_joueur()
        self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs2(self.nombre_de_joueurs)
        self.mises = self.mises = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)
        self.argent = self.argent = initialisation_de_dictionnaire(self.nombre_de_joueurs, 500)
        self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)
        self.mise_verif = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)

    def remise_à_zéro(self):
        self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs2(self.nombre_de_joueurs)
        self.mises = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)
        self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)
        self.mise_verif = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)

def main2():

    while True :
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            draw_window()


            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()

            Partie_de_jeu2()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main2__" :
    main2()