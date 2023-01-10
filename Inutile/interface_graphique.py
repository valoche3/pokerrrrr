
# import pygame 
# from pygame import *
# import sys 
# import os 
# from Colors_class import Colors 
# from Input_box import InputBox

# pygame.init()

# WIDTH, HEIGHT = 1000, 600
# WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 

# pygame.display.set_caption("Texas Hold'em")

# COLOR = Colors()

# def affichage_image (nom_dossier, nom_image):
#     WIN.blit(pygame.image.load(os.path.join(nom_dossier, nom_image+'.png')), (0, 0))

# TAPIS =pygame.image.load(os.path.join( 'Tapis', 'Tapis_TexasHold\'em.jpeg'))
# TAPIS = pygame.transform.scale(TAPIS, (750,450))
# WIDTH_TAPIS = TAPIS.get_width()
# HEIGHT_TAPIS = TAPIS.get_height()

# smallfont = pygame.font.SysFont('Corbel',35)
# text_bet = smallfont.render('Bet' , True , COLOR.white)
# text_fold = smallfont.render('Fold' , True , COLOR.white)
# text_Raise = smallfont.render('Raise' , True , COLOR.white)

# def afficher_texte_bouttons():
#     WIN.blit(text_bet, (50, HEIGHT-50))
#     WIN.blit(text_fold, (450, HEIGHT-50))
#     WIN.blit(text_Raise, (700, HEIGHT-50))


# def contour_boutons():
#     pygame.draw.rect(WIN,COLOR.dark_green3,[50,HEIGHT-50,140,40])
#     pygame.draw.rect(WIN, COLOR.dark_green3, [450, HEIGHT-50, 140, 40])
#     pygame.draw.rect(WIN, COLOR.dark_green3, [700, HEIGHT-50, 140, 40])


# def draw_window(event):
#     WIN.fill(COLOR.black)
#     #pygame.draw.rect(WIN, BLACK, BORDER) 
#     WIN.blit(TAPIS, (WIDTH/2 - WIDTH_TAPIS/2, HEIGHT/2 - HEIGHT_TAPIS/2))
#     affichage_image('Cards\coeurs', 'Coeur_2') 
#     # WIN.blit(BACK, (card.x + 50, card.y + 50)) 

#     if event.type == pygame.MOUSEBUTTONDOWN:
#         if pygame.mouse.get_pressed():
#             if 50 <= pygame.mouse.get_pos()[0] <= 50 +140 and HEIGHT - 50 <= pygame.mouse.get_pos()[1] <= HEIGHT - 50 + 40:
#                 affichage_image('Jetons', 'bet-img1') #comment garder le jeton affiché après avoir cliqué sur le boutton ?

#         if pygame.mouse.get_pressed():
#             if 700 <= pygame.mouse.get_pos()[0] <= 700 +140 and HEIGHT - 50 <= pygame.mouse.get_pos()[1] <= HEIGHT - 50 + 40:
#                     affichage_image('Jetons', 'bet-img1')
        
#         if pygame.mouse.get_pressed():
#             if 450 <= pygame.mouse.get_pos()[0] <= 450 +140 and HEIGHT - 50 <= pygame.mouse.get_pos()[1] <= HEIGHT - 50 + 40:
#                     affichage_image('Cards', 'red')
#                     affichage_image('Cards', 'red')

#     if 50 <= pygame.mouse.get_pos()[0] <= 50 +140 and HEIGHT - 50 <= pygame.mouse.get_pos()[1] <= HEIGHT - 50 + 40:
#         pygame.draw.rect(WIN,COLOR.light_gray1,[50,HEIGHT-50,140,40])
    
#     elif 450 <= pygame.mouse.get_pos()[0] <= 450 +140 and HEIGHT - 50 <= pygame.mouse.get_pos()[1] <= HEIGHT - 50 + 40:
#         pygame.draw.rect(WIN,COLOR.light_gray1,[450,HEIGHT-50,140,40])
    
#     elif 700 <= pygame.mouse.get_pos()[0] <= 700 +140 and HEIGHT - 50 <= pygame.mouse.get_pos()[1] <= HEIGHT - 50 + 40:
#         pygame.draw.rect(WIN,COLOR.light_gray1,[700,HEIGHT-50,140,40])

#     else:
#         contour_boutons()
    
#     afficher_texte_bouttons()
#     pygame.display.update()
    
     

# def main1():
#     card = pygame.Rect(100, 300, 60, 100)
#     clock = pygame.time.Clock()
#     input_box1 = InputBox(WIN, 100, 100, 140, 32)
#     input_box2 = InputBox(WIN, 100, 300, 140, 32)
#     input_boxes = [input_box1, input_box2]
#     run = True
    
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT : 
#                 run = False
#             for box in input_boxes:
#                 box.handle_event(event)

#         for box in input_boxes:
#             box.update()

#         draw_window(event)

#         for box in input_boxes:
#             box.draw()

#         pygame.display.flip()
#         pygame.display.update()
#         clock.tick(60)




# if __name__ == "__main__":
#     main1()
#     pygame.quit()
