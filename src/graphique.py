from src.Color_class import Colors
import pygame
import sys
import os


def init_placement_joueurs(tapis_width, tapis_height):
    return [
        (tapis_width / 2, 70),
        (tapis_width / 2, tapis_height - 70),
        (tapis_width - 70, tapis_height / 3),
        (20, tapis_height / 3),
        (3 * tapis_width / 4, 70),
        (tapis_width - 50, 2 * tapis_height / 3),
        (tapis_width / 4, tapis_height - 70),
        (20, 2 * tapis_height / 3),
        (tapis_width / 4, 70),
        (3 * tapis_width / 4, tapis_height - 70)
    ]


class Graphique:
    def __init__(self, mode_graphique):
        pygame.init()
        self.mode_graphique = mode_graphique
        if mode_graphique:
            self.color = Colors()
            self.width = 1300
            self.height = 700
            self.window = pygame.display.set_mode((self.width, self.height))
            self.tapis = pygame.transform.scale(pygame.image.load(os.path.join("utile/", "Tapis.jpg")), (self.width, self.height))
            self.placement_joueurs = init_placement_joueurs(self.tapis.get_width(), self.tapis.get_height())

    def draw_window(self):
        if not self.mode_graphique:
            return

        self.window.fill(self.color.black)
        self.window.blit(self.tapis, (0, 0))
        pygame.display.update()


    def affichage_image(self, path, nom_du_fichier, x, y):
        if not self.mode_graphique:
            return

        surface = pygame.image.load(os.path.join(path, nom_du_fichier))
        carte_retournée = pygame.transform.scale(surface, (50, 80))
        self.tapis.blit(carte_retournée, (x, y))
        self.tapis.blit(carte_retournée, (x + 20, y))


    def afficher_texte_bouttons(self, fenetre, nom_boutton, positions=(0,0), couleur=(0, 0, 0, 0)):
        if not self.mode_graphique:
            return

        smallfont = pygame.font.SysFont('Corbel', 22)
        nom_boutton = smallfont.render(nom_boutton, True, couleur)
        fenetre.blit(nom_boutton, positions)


    def affichage_des_cartes_joueurs(self, mains_des_joueurs, argents_des_joueurs):
        if not self.mode_graphique:
            return

        for i in range (0, len(mains_des_joueurs)):
            self.affichage_image("utile/", "red.png", self.placement_joueurs[i][0],  self.placement_joueurs[i][1])
            self.afficher_texte_bouttons(self.tapis, f" {argents_des_joueurs['j'+ str(i)]}", (self.placement_joueurs[i][0], self.placement_joueurs[i][1] - 30), (0, 0, 0, 0))


    def retourner_cartes(self, mains_des_joueurs):
        if not self.mode_graphique:
            return

        for i in range (0, len(mains_des_joueurs)):
            print("============>", mains_des_joueurs[i])
            # self.affichage_image("utile/", f".png", self.placement_joueurs[i][0],  self.placement_joueurs[i][1])


    def vérification_quitter_window(self, event):
        if not self.mode_graphique:
            return

        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
