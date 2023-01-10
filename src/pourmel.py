from random import randint
import time
import pygame
import sys
import os

#mise_verif = dictionnaire qui renseigne la mise de chaqeu joueur sans prendre en compte la petite blinde et la grosse blinde

def détermination_premier_dealer(nombre_de_joueurs): #pour la première sous-partie
    dealer = randint(0, nombre_de_joueurs - 1)
    print('\nLe dealer est le joueur numéro : ', dealer)

    return dealer


def détermination_dealer(dealer): #pour toutes les sous-parties sauf la première
    dealer += 1
    print('\nLe nouveau dealer est le joueur numéro :', dealer, '\n', 'Le joueur qui paye la petite blinde est le joueur suivant le dealer.')

    return dealer


def attribution_petite_blinde_grosse_blinde(nombre_de_joueurs, dealer, mise, argent):

    if nombre_de_joueurs > 2:

        if dealer <= nombre_de_joueurs - 3: #si on n'a pas besoin de revenir à j0

            petite_blinde = int(input('Petite blinde : '))
            while petite_blinde > argent['j'+str(dealer+1)]:
                petite_blinde = int(input('Petite blinde : '))
            mise['j' + str(dealer+1)] = petite_blinde
            numero_petite_blinde = dealer + 1

            grosse_blinde = 2 * petite_blinde
            a = False
            i = 0
            while a == False:
                if argent['j'+str(dealer+2+i)] > grosse_blinde:
                    a = True
                    mise['j'+str(dealer+2+i)] = grosse_blinde
                else:
                    i += 1
            numero_grosse_blinde = dealer + 2 + i

        elif dealer == nombre_de_joueurs - 2: #si j0 paie la grosse blinde

            petite_blinde = int(input('Petite blinde : '))
            while petite_blinde > argent['j'+str(dealer+1)]:
                petite_blinde = int(input('Petite blinde : '))
            mise['j' + str(dealer+1)] = petite_blinde
            numero_petite_blinde = dealer + 1

            grosse_blinde = 2 * petite_blinde
            a = False
            i = 0
            while a == False:
                if argent['j'+str(i)] > grosse_blinde:
                    a = True
                    mise['j'+str(i)] = grosse_blinde
                else:
                    i += 1
            numero_grosse_blinde = i

        else: #si j0 paie la petite blinde et j1 la grosse blinde
            petite_blinde = int(input('Petite blinde : '))
            while petite_blinde > argent['j0']:
                petite_blinde = int(input('Petite blinde : '))
            mise['j0'] = petite_blinde
            numero_petite_blinde = 0

            grosse_blinde = 2 * petite_blinde
            a = False
            i = 0
            while a == False:
                if argent['j' + str(i+1)] > grosse_blinde:
                    a = True
                    mise['j' + str(i+1)] = grosse_blinde
                else:
                    i += 1
            numero_grosse_blinde = i + 1

    else: #si le nombre de joueurs est égal à 2
        if dealer == 0:
            petite_blinde = int(input('Petite blinde : '))
            grosse_blinde = 2 * petite_blinde
            while petite_blinde > argent['j0'] and grosse_blinde > argent['j1']:
                petite_blinde = int(input('Petite blinde : '))
                grosse_blinde = 2 * petite_blinde
            mise['j0'] = petite_blinde
            mise['j1'] = grosse_blinde
            numero_petite_blinde = 0
            numero_grosse_blinde = 1

        else:
            petite_blinde = int(input('Petite blinde : '))
            grosse_blinde = 2 * petite_blinde
            while petite_blinde > argent['j1'] and grosse_blinde > argent['j0']:
                petite_blinde = int(input('Petite blinde : '))
                grosse_blinde = 2 * petite_blinde
            mise['j1'] = petite_blinde
            mise['j0'] = grosse_blinde
            numero_petite_blinde = 1
            numero_grosse_blinde = 0

    return petite_blinde, grosse_blinde, numero_petite_blinde, numero_grosse_blinde, mise_minimale


def joueur_present(nombre_de_joueurs): #créer un set avec tous les joueurs en jeu et qui les enlève quand ils se couchent
    present = {'j'+str(i) for i in range(nombre_de_joueurs)}

    return present


def premier_joueur(nombre_de_joueurs, dealer, mod = 'flop'):

    if nombre_de_joueurs > 2:
        if mod == 'flop': #pour flop, c'est le troisième joueur après le dealer qui joue en premier
            if ((nombre_de_joueurs - 1) - (dealer)) < 3:
                joueur_actuel = 'j' + str((dealer + 3) % nombre_de_joueurs)
                numero_joueur_actuel = (dealer + 3) % nombre_de_joueurs
            else:
                joueur_actuel = 'j' + str(dealer + 3)
                numero_joueur_actuel = dealer + 3
        else: #pour turn et river, c'est le joueur juste après le dealer qui joue en premier
            if dealer != nombre_de_joueurs - 1:
                joueur_actuel = 'j' + str(dealer + 1)
                numero_joueur_actuel = dealer + 1

            else:
                joueur_actuel = 'j0'
                numero_joueur_actuel = 0
    else: #si le nombre de joueurs est égal à 2
        if dealer == 0:
            joueur_actuel = 'j1'
            numero_joueur_actuel = 1
        else:
            joueur_actuel = 'j0'
            numero_joueur_actuel = 0

    print("\tC'est à", joueur_actuel, "de jouer")

    return joueur_actuel, numero_joueur_actuel


def def_joueur_actuel(partie, graphique, joueur_actuel, numero_joueur_actuel, present): #pour passer au joueur suivant pendant la partie

    if joueur_actuel == 'j' + str(partie.nombre_de_joueurs - 1): #si on est au dernier joueur de la boucle
        joueur_actuel = 'j0'
        numero_joueur_actuel = 0
    else:
        joueur_actuel = 'j' + str(numero_joueur_actuel + 1)
        numero_joueur_actuel = numero_joueur_actuel + 1
    if joueur_actuel in present : #si le joueur n'est pas couché
        print("\tC'est à", joueur_actuel, "de jouer")
        graphique.retourner_cartes(partie.mains)

    return joueur_actuel, numero_joueur_actuel


def def_mise_minimale(mise_verif, grosse_blinde, mod = 'flop'):
    
    #pour vérifier si on n'est pas au début de "flop", "turn" ou "river"
    a = False
    for k in mise_verif:
        if mise_verif[k] == 0:
            a = True
        else:
            a = False
    if a == True and mod == 'flop':
        mise_minimale = grosse_blinde
    elif a == True and mod == 'turn/river':
        mise_minimale = 0
    elif a == False: #la mise minimale est la mise maximum déjà misée
        maxi = None
        for k in mise_verif:
            if maxi == None or mise_verif[k] > maxi:
                maxi = mise_verif[k]
        mise_minimale = maxi

    return mise_minimale


def avancee_tour(present, mise_verif): #vérifier que tous les joueurs ne sont pas couchés et vérifier que ceux qui ne sont pas couchés sont tous à la même mise, sinon le tour continue
    if len(present) > 1 :
        maxi = None
        for k in mise_verif:
            if (maxi == None) or mise_verif[k] > maxi:
                maxi = mise_verif[k]

        for joueur in present:
            a = mise_verif[joueur]
            if a != maxi:
                tour = True
                break
            else:
                tour = False
    else:
        tour = False

    return tour

def actions_possibles(joueur_actuel, present, mise_minimale, argent, mise, mise_verif, grosse_blinde, mod = 'flop'):
    if joueur_actuel in present:

        print('\tVoici les actions que tu peux faire : ')
        if mod == 'flop':
            if argent[joueur_actuel] >= def_mise_minimale(mise_verif, grosse_blinde, mod = 'flop'):
                print("\t\t- s'aligner - check si personne n'a misé")
                print("\t\t- miser jusqu'à", argent[joueur_actuel] - mise[joueur_actuel])
            elif argent[joueur_actuel] >= def_mise_minimale(mise_verif, grosse_blinde, mod = 'turn/river'):
                print("\t\t- s'aligner - check si personne n'a misé")
                print("\t\t- miser jusqu'à", argent[joueur_actuel] - mise[joueur_actuel])
        print('\t\t- se coucher')


def action_a_faire(partie, graphique, joueur_actuel, mise_minimale, present, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'flop'):
    if joueur_actuel in present:
        actions_possibles(joueur_actuel, present, mise_minimale, partie.argent, partie.mises, partie.mise_verif, grosse_blinde)
        a = input('\nQue veux-tu faire ? : ')
        while a != "s'aligner" and a != 'miser' and a != 'se coucher':
            a = input('\nQue veux-tu faire ? : ')
        if a == "s'aligner":
            if mod == 'flop':
                if numero_joueur_actuel == numero_petite_blinde:
                    partie.mises[joueur_actuel] = def_mise_minimale(partie.mise_verif, grosse_blinde, mod = 'flop') + petite_blinde
                elif numero_joueur_actuel == numero_grosse_blinde:
                    partie.mises[joueur_actuel] = def_mise_minimale(partie.mise_verif, grosse_blinde, mod = 'flop') + grosse_blinde
                else:
                    partie.mises[joueur_actuel] = def_mise_minimale(partie.mise_verif, grosse_blinde, mod = 'flop')
                partie.mise_verif[joueur_actuel] = def_mise_minimale(partie.mise_verif, grosse_blinde, mod = 'flop')
            else: #dans le cas de "turn" ou "river" (pas la même mise minimale)
                if numero_joueur_actuel == numero_petite_blinde:
                    partie.mises[joueur_actuel] = def_mise_minimale(partie.mise_verif, grosse_blinde, mod = 'turn/river') + petite_blinde
                elif numero_joueur_actuel == numero_grosse_blinde:
                    partie.mises[joueur_actuel] = def_mise_minimale(partie.mise_verif, grosse_blinde, mod = 'turn/river') + grosse_blinde
                else:
                    partie.mises[joueur_actuel] = def_mise_minimale(partie.mise_verif,grosse_blinde, mod = 'turn/river')
                partie.mise_verif[joueur_actuel] = def_mise_minimale(partie.mise_verif, grosse_blinde, mod = 'turn/river')
        elif a == "miser":
            print("Combien veux-tu miser ? jusqu'à ", partie.argent[joueur_actuel] - partie.mises[joueur_actuel])
            a_miser = int(input())
            while a_miser > partie.argent[joueur_actuel] - partie.mises[joueur_actuel] or a_miser < mise_minimale:
                a_miser = int(input("Vous n'avez pas assez ou vous n'avez pas miser assez, nouvelle mise : "))
            partie.mises[joueur_actuel] += a_miser
            partie.mise_verif[joueur_actuel] += a_miser
            mise_minimale = partie.mise_verif[joueur_actuel]
        else: #se coucher
            present.discard(joueur_actuel)
    joueur_actuel, numero_joueur_actuel = def_joueur_actuel(partie, graphique, joueur_actuel, numero_joueur_actuel, present)
    print(partie.mises)

    return partie, mise_minimale, present, joueur_actuel, numero_joueur_actuel


def tour_de_jeu(partie, graphique): #une sous-partie de jeu qui appelle toutes les fonctions dans l'ordre
    étape_du_tour = "flop" #puis "turn" et "river"
    control_flop = True
    control_turn = True
    control_river = True

    present = joueur_present(partie.nombre_de_joueurs)
    petite_blinde, grosse_blinde, numero_petite_blinde, numero_grosse_blinde, mise_minimale = attribution_petite_blinde_grosse_blinde(partie.nombre_de_joueurs, partie.dealer, partie.mises, partie.argent)

    while True:
        if graphique.mode_graphique:
            clock = pygame.time.Clock()
            clock.tick(60)

        for event in pygame.event.get():
            graphique.draw_window()

            if étape_du_tour == "flop":
                if control_flop:
                    print('\n\tDébut du tour de flop :')

                    joueur_actuel, numero_joueur_actuel = premier_joueur(partie.nombre_de_joueurs, partie.dealer, mod = 'flop')

                    print(f"\nLes cartes du milieu sont : {partie.cartes_du_milieu[0:3]}\n")

                    # Condition de victoire, s'il ne reste plus qu'un joueur non-couché
                    for i in range(partie.nombre_de_joueurs):
                        graphique.vérification_quitter_window(event.type)
                        if graphique.mode_graphique:
                            pygame.display.update()
                        if len(present) == 1:
                            return partie, present
                        partie, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(partie, graphique, joueur_actuel, mise_minimale, present, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'flop')
                        if not avancee_tour(present, partie.mise_verif):
                            étape_du_tour = "turn"

                    control_flop = False

                if étape_du_tour == "flop":
                    partie, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(partie, graphique, joueur_actuel, mise_minimale, present, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'flop')
                    if not avancee_tour(present, partie.mise_verif):
                        étape_du_tour = "turn"
            elif étape_du_tour == "turn":
                if control_turn:
                    print('\n\tDébut du tour de turn :')

                    print(f"\nLes cartes du milieu sont : {partie.cartes_du_milieu[0:4]}\n")

                    joueur_actuel, numero_joueur_actuel = premier_joueur(partie.nombre_de_joueurs, partie.dealer, mod = 'turn')

                    for i in range(partie.nombre_de_joueurs):
                        graphique.vérification_quitter_window(event.type)
                        if graphique.mode_graphique:
                            pygame.display.update()
                        if len(present) == 1:
                            return partie, present
                        partie, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(partie, graphique, joueur_actuel, mise_minimale, present, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')
                        if not avancee_tour(present, partie.mise_verif):
                            étape_du_tour = "river"

                    control_turn = False

                if étape_du_tour == "turn":
                    partie, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(partie, graphique, joueur_actuel, mise_minimale, present, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')
                    if not avancee_tour(present, partie.mise_verif):
                        étape_du_tour = "river"
            elif étape_du_tour == "river": # au moment du river
                if control_river:
                    print('\n\tDébut du tour de river :')

                    print(f"\nLes cartes du milieu sont : {partie.cartes_du_milieu[0:5]}\n")

                    joueur_actuel, numero_joueur_actuel = premier_joueur(partie.nombre_de_joueurs, partie.dealer, mod = 'river')

                    for i in range(partie.nombre_de_joueurs):
                        graphique.vérification_quitter_window(event.type)
                        if graphique.mode_graphique:
                            pygame.display.update()
                        if len(present) == 1:
                            return partie, present
                        partie, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(partie, graphique, joueur_actuel, mise_minimale, present, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')
                        if not avancee_tour(present, partie.mise_verif):
                            étape_du_tour = "fin"
                    control_river = False

                if étape_du_tour == "river":
                    partie, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(partie, graphique, joueur_actuel, mise_minimale, present, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')
                    if not avancee_tour(present, partie.mise_verif):
                        étape_du_tour = "fin"

            if étape_du_tour == "fin":
                return partie, present

            graphique.vérification_quitter_window(event.type)
            if graphique.mode_graphique:
                pygame.display.update()
