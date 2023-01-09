from random import randint
from src.Color_class import Colors
import pygame
from src.miseEnPlace import *
import sys
import os


Piques = ["Pique_As", "Pique_R", "Pique_D", "Pique_V", "Pique_10", "Pique_9", "Pique_8", "Pique_7", "Pique_6", "Pique_5", "Pique_4", "Pique_3", "Pique_2"]
Trèfles = ["Trèfle_As", "Trèfle_R", "Trèfle_D", "Trèfle_V", "Trèfle_10", "Trèfle_9", "Trèfle_8", "Trèfle_7", "Trèfle_6", "Trèfle_5", "Trèfle_4", "Trèfle_3", "Trèfle_2"]
Coeurs = ["Coeur_As", "Coeur_R", "Coeur_D", "Coeur_V", "Coeur_10", "Coeur_9", "Coeur_8", "Coeur_7", "Coeur_6", "Coeur_5", "Coeur_4", "Coeur_3", "Coeur_2"]
Carreaux = ["Carreau_As", "Carreau_R", "Carreau_D", "Carreau_V", "Carreau_10", "Carreau_9", "Carreau_8", "Carreau_7", "Carreau_6", "Carreau_5", "Carreau_4", "Carreau_3", "Carreau_2"]

COLOR = Colors()

WIDTH, HEIGHT = 1300, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 

pygame.display.set_caption("Texas Hold'em")

TAPIS =pygame.image.load(os.path.join( 'Poker\Tapis', 'Tapis.jpg'))
TAPIS = pygame.transform.scale(TAPIS, (WIDTH,HEIGHT))
WIDTH_TAPIS = TAPIS.get_width()
HEIGHT_TAPIS = TAPIS.get_height()

PLACEMENT_JOUEURS = [(WIDTH_TAPIS/2, 70), 
(WIDTH_TAPIS/2, HEIGHT_TAPIS -70), 
(WIDTH_TAPIS-70, HEIGHT_TAPIS/3), 
(20, HEIGHT_TAPIS/3), 
(3* WIDTH_TAPIS / 4, 70), 
(WIDTH_TAPIS-50, 2*HEIGHT_TAPIS/3), 
(WIDTH_TAPIS/4, HEIGHT_TAPIS-70), 
(20, 2*HEIGHT_TAPIS/3), 
(WIDTH_TAPIS/4, 70), 
(3*WIDTH_TAPIS/4, HEIGHT_TAPIS-70)]

def draw_window():

    WIN.fill(COLOR.black)

    WIN.blit(TAPIS, (0, 0))

    pygame.display.update()

def affichage_image ( nom_dossier, nom_image, x, y):
    carte_retournée = pygame.image.load(os.path.join(nom_dossier, nom_image + '.png'))
    carte_retournée = pygame.transform.scale(carte_retournée, (50, 80))
    TAPIS.blit(carte_retournée, (x, y))
    TAPIS.blit(carte_retournée, (x+20, y ))

def afficher_texte_bouttons( fenetre, nom_boutton, positions=(0,0), couleur=(0, 0, 0, 0)):
    smallfont = pygame.font.SysFont('Corbel',22)
    nom_boutton=smallfont.render(nom_boutton , True , couleur)
    fenetre.blit(nom_boutton, positions)

       
def distribution_des_cartes_joueurs2(nombre_de_joueurs, dico_argent):

    paquet_de_jeu = Piques + Trèfles + Coeurs + Carreaux
    mains = initialisation_de_dictionnaire(nombre_de_joueurs, 0)

    for i in mains:
        mains[i] = [0, 0]
        mains[i][0] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))  #afficher les cartes face cachée, 2 par joueur
        mains[i][1] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))
        for i in range(nombre_de_joueurs) :
            affichage_image ( 'Poker\Cards', 'red', PLACEMENT_JOUEURS[i][0],PLACEMENT_JOUEURS[i][1] )
            afficher_texte_bouttons(TAPIS, f" {dico_argent['j'+ str(i)]}", (PLACEMENT_JOUEURS[i][0],PLACEMENT_JOUEURS[i][1] - 30), (0, 0, 0, 0))

    for i in mains:
        mains[i] = [0, 0]
        mains[i][0] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))
        mains[i][1] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))

    return mains, paquet_de_jeu


def main2():

    while True : 
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            draw_window()
            

            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        
            distribution_des_cartes_joueurs(4 )
        pygame.display.update()
        clock.tick(60)

main2()
