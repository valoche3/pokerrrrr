import pygame
import sys
import os


def init_placement_joueurs(tapis_width, tapis_height):
    return [
        (tapis_width / 2, 90),
        (tapis_width / 2, tapis_height - 90),
        (tapis_width - 70, tapis_height / 3 - 20),
        (20, tapis_height / 3 - 20),
        (3 * tapis_width / 4, 70 - 20),
        (tapis_width - 50, 2 * tapis_height / 3 - 20),
        (tapis_width / 4, tapis_height - 70 - 20),
        (20, 2 * tapis_height / 3 - 20),
        (tapis_width / 4, 70 - 20),
        (3 * tapis_width / 4, tapis_height - 70 - 20)
    ]

def init_placement_cartes_milieu(tapis_width, tapis_height):
    return [
        (tapis_width/2 - 450, tapis_height/2 - 213/2),
        (tapis_width/2 - 262.5,tapis_height/2 - 213/2),
        (tapis_width/2 -75, tapis_height/2 - 213/2),
        (tapis_width/2 + 262.5-75-32.7, tapis_height/2 - 213/2),
        (tapis_width/2 + 450-75-32.7, tapis_height/2 - 213/2)
    ]

class Graphique:
    def __init__(self, mode_graphique):
        pygame.init()
        self.mode_graphique = mode_graphique
        if mode_graphique:
            self.width = 1300
            self.height = 700
            self.window = pygame.display.set_mode((self.width, self.height))
            self.tapis = pygame.transform.scale(pygame.image.load(os.path.join("utile/", "Tapis.jpg")), (self.width, self.height))
            self.placement_joueurs = init_placement_joueurs(self.tapis.get_width(), self.tapis.get_height())
            self.placement_cartes_milieu = init_placement_cartes_milieu(self.tapis.get_width(), self.tapis.get_height())

    def draw_window(self):
        if not self.mode_graphique:
            return

        self.window.fill((0, 0, 0, 0))
        self.window.blit(self.tapis, (0, 0))
        pygame.display.update()


    def affichage_image(self, path, nom_du_fichier, x, y, mode = "cachées"):
        if not self.mode_graphique:
            return

        surface = pygame.image.load(os.path.join(path, nom_du_fichier))
        carte = pygame.transform.scale(surface, (50, 80))
        self.tapis.blit(carte, (x, y))
        if mode == "cachées" :
            self.tapis.blit(carte, (x - 20, y))


    def afficher_texte_bouttons(self, fenetre, nom_boutton, positions=(0,0), couleur=(0, 0, 0, 0)):
        if not self.mode_graphique:
            return

        smallfont = pygame.font.SysFont('Corbel', 22)
        nom_boutton = smallfont.render(nom_boutton, True, couleur)
        fenetre.blit(nom_boutton, positions)


    def affichage_des_cartes_joueurs_face_cachée(self, mains_des_joueurs, argents_des_joueurs) :
        if not self.mode_graphique:
            return

        for i in range (0, len(mains_des_joueurs)):
            self.affichage_image("utile/paquet", "red.png", self.placement_joueurs[i][0],  self.placement_joueurs[i][1])
            self.afficher_texte_bouttons(self.tapis, f" j{i} a {argents_des_joueurs['j'+ str(i)]}", (self.placement_joueurs[i][0]-10, self.placement_joueurs[i][1] - 20), (0, 0, 0, 0))
            
            
        

    def affichage_carte_joueurs_face_visible(self, main_joueurs, numero_joueur):
        if not self.mode_graphique:
            return
    
        self.affichage_image("utile/paquet", f"{main_joueurs['j' + str(numero_joueur)][0]}.png", self.placement_joueurs[numero_joueur][0], self.placement_joueurs[numero_joueur][1], mode="visible")
        self.affichage_image("utile/paquet", f"{main_joueurs['j' + str(numero_joueur)][1]}.png", self.placement_joueurs[numero_joueur][0] - 20, self.placement_joueurs[numero_joueur][1], mode="visible")

    def retourner_cartes_milieu(self, cartes_du_milieu, numero_carte_milieu):
        if not self.mode_graphique:
            return
        self.affichage_image("utile/paquet", f"{cartes_du_milieu[numero_carte_milieu]}.png", self.placement_cartes_milieu[numero_carte_milieu][0],  self.placement_cartes_milieu[numero_carte_milieu][1], mode = "visible")
        
    def cartes_joueur_cachées(self, numero_joueur_actuel, mise, petite_blinde, grosse_blinde):
        if not self.mode_graphique:
            return
        mise_tot = petite_blinde + grosse_blinde
        self.affichage_image("utile/paquet", "red.png", self.placement_joueurs[numero_joueur_actuel][0], self.placement_joueurs[numero_joueur_actuel][1], mode = "cachées")
        mise_tot + mise['j' + str(numero_joueur_actuel)]
        
    def vérification_quitter_window(self, event):
        if not self.mode_graphique:
            return

        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
