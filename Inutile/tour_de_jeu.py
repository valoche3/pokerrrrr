def détermination_premier_dealer(nombre_de_joueurs):

    dealer = randint(0, nombre_de_joueurs-1)
    print('le dealer est le joueur numéro : ', dealer)

    return(dealer)

def détermination_dealer(nombre_de_joueurs, dealer):

    dealer += 1
    print('Le nouveau dealer est le joueur numéro :', dealer)

    return(dealer)

def attribution_petite_blinde_grosse_blinde(nombre_de_joueurs, dealer, mise, argent):

    if nombre_de_joueurs > 2:

        if dealer <= nombre_de_joueurs-3:

            petite_blinde = int(input('petite blinde : ')) #fuck
            while petite_blinde > argent['j'+str(dealer+1)]:
                petite_blinde = int(input('petite blinde : ')) #fuck
            mise['j' + str(dealer+1)] = petite_blinde
            numero_petite_blinde = dealer + 1

            grosse_blinde = 2*petite_blinde
            a = False
            i = 0
            while a == False:
                if argent['j'+str(dealer+2+i)] > grosse_blinde:
                    a = True
                    mise['j'+str(dealer+2+i)] = grosse_blinde
                else:
                    i += 1
            numero_grosse_blinde = dealer + 2 + i

        elif dealer == nombre_de_joueurs - 2:

            petite_blinde = int(input('petite blinde : '))
            while petite_blinde > argent['j'+str(dealer+1)]:
                petite_blinde = int(input('petite blinde : '))
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

        else:

            petite_blinde = int(input('petite blinde : '))#fuck
            while petite_blinde > argent['j0']:
                petite_blinde = int(input('petite blinde : '))#fuck
            mise['j0'] = petite_blinde
            numero_petite_blinde = 0

            grosse_blinde = 2 * petite_blinde
            a = False
            i = 0
            while a == False:
                if argent['j'+str(i+1)] > grosse_blinde:
                    a = True
                    mise['j'+str(i+1)] = grosse_blinde
                else:
                    i += 1
            numero_grosse_blinde = i + 1

    else:
        if dealer == 0:
            petite_blinde = int(input('petite blinde : '))#fuck
            grosse_blinde = 2 * petite_blinde
            while petite_blinde > argent['j0'] and grosse_blinde > argent['j1']:
                petite_blinde = int(input('petite blinde : '))#fuck
                grosse_blinde = 2 * petite_blinde
            mise['j0'] = petite_blinde
            mise['j1'] = grosse_blinde
            numero_petite_blinde = 0
            numero_grosse_blinde = 1

        else:
            petite_blinde = int(input('petite blinde : '))
            grosse_blinde = 2 * petite_blinde
            while petite_blinde > argent['j1'] and grosse_blinde > argent['j0']:
                petite_blinde = int(input('petite blinde : '))
                grosse_blinde = 2 * petite_blinde
            mise['j1'] = petite_blinde 
            mise['j0'] = grosse_blinde
            numero_petite_blinde = 1
            numero_grosse_blinde = 0
    
    mise_minimale = petite_blinde
    
    return(petite_blinde, grosse_blinde, numero_petite_blinde, numero_grosse_blinde, mise_minimale)


def joueur_present(nombre_de_joueurs):

    present = {'j'+str(i) for i in range(nombre_de_joueurs)}

    return(present)
  
  
def premier_joueur(nombre_de_joueurs, dealer, mod = 'flop'):

    if mod == 'flop':
        if ((nombre_de_joueurs - 1) - (dealer)) < 3:
            joueur_actuel = 'j' + str((dealer + 3) % nombre_de_joueurs)
            numero_joueur_actuel = (dealer + 3) % nombre_de_joueurs 
        else:
            joueur_actuel = 'j' + str(dealer + 3)
            numero_joueur_actuel = dealer + 3
    else: 
        if dealer != 'j' + str(nombre_de_joueurs - 1):
            joueur_actuel = 'j' + str(dealer + 1)
            numero_joueur_actuel = dealer + 1
            
        else:
            joueur_actuel = 'j0'
            numero_joueur_actuel = 0
    
    print("C'est à", joueur_actuel, "de jouer")

    return(joueur_actuel, numero_joueur_actuel)
    
    
def joueur_actuel(nombre_de_joueurs, dealer):

    if joueur_actuel == 'j' + str(nombre_de_joueurs - 1):
           joueur_actuel == 'j0'
       else:
           joueur_actuel == 'j' + str(numero_joueur_actuel + 1)
    
    print("C'est à", joueur_actuel, "de jouer")
    
    return(joueur_actuel, numero_joueur_actuel)


def mise_verif(nombre_de_joueurs):

    mise_verif = initialisation_de_dictionnaire(nombre_de_joueurs, 0)

    return(mise_verif)


def avancee_tour(mise, present):

    if present != {}:
        verif = mise_verif[random.choice(present)]
        for joueur in present:
            a = mise_verif[joueur]
            if a != verif:
                tour = True
            else :
                tour = False
    else:
        tour = False

    return(tour)


def actions_possibles(joueur_actuel, present, mise_minimale):
        if joueur_actuel in present:

            print('Voici les actions que tu peux faire :')
            if argent[joueur_actuel] >= mise_minimale:
                print("s'aligner")
                print("miser jusqu'à", str(argent[joueur_actuel]))
            print('se coucher')


def action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent):

    a = input('Que veux-tu faire ? :')#fuck
    actions_possibles(joueur_actuel, present, mise_minimale)   
    while a == "s'aligner" or a == 'miser' or a == 'se coucher':
        a = input('Que veux-tu faire ? :') #fuck
    if a == "s'aligner":
        mise[joueur_actuel] += mise_minimale
        mise_verif[joueur_actuel] = mise_minimale
        mise_minimale = mise_verif[joueur_actuel] 
    elif a == "miser":
        mettre = input('Combien veux-tu miser ?', "jusqu'à", argent[joueur_actuel])#fuck
        mise[joueur_actuel] += mettre
        mise_verif[joueur_actuel] = mettre
        mise_minimale = mise_verif[joueur_actuel]
    else:
        present.pop(joueur_actuel)

    return(mise, mise_verif, mise_minimale, present)


def tour_de_jeu(nombre_de_joueurs, mise, argent):

    dealer = détermination_premier_dealer(nombre_de_joueurs)
    petite_blinde, grosse_blinde, numero_petite_blinde, numero_grosse_blinde, mise_minimale = attribution_petite_blinde_grosse_blinde(nombre_de_joueurs, dealer, mise, argent)
    present = joueur_present(nombre_de_joueurs)
    mise_verif = mise_verif(nombre_de_joueurs
    joueur_actuel = premier_joueur(nombre_de_joueurs, dealer, mod = 'flop')
    tour = avancee_tour(mise, present)
    
    while tour == True:
    
        actions_possibles(joueur_actuel, present, mise_minimale)
        mise, mise_verif, mise minimale, present = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent)
        joueur_actuel = joueur_actuel(nombre_de_joueurs, dealer)
        mise_verif = mise_verif(nombre_de_joueurs, present)
       
    while tour == True:
    
        actions_possibles(joueur_actuel, present, mise_minimale)
        mise, mise_verif, mise minimale, present = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent)
        joueur_actuel = joueur_actuel(nombre_de_joueurs, dealer, mod = 'turn')
        mise_verif = mise_verif(nombre_de_joueurs, present)
    
     while tour == True:
    
        actions_possibles(joueur_actuel, present, mise_minimale)
        mise, mise_verif, mise minimale, present = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent)
        joueur_actuel = joueur_actuel(nombre_de_joueurs, dealer, mod = 'river')
        mise_verif = mise_verif(nombre_de_joueurs, present)
    
    
   
