from random import randint
import random 

# trichiffres : fonction qui trie par chiffres+couleurs et par chiffres
def trichiffres(main_du_joueur, cartes_du_milieu):
    tri_chiffre = []
    ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    cartes = main_du_joueur + cartes_du_milieu

    for val in ref:
        for carte in cartes:
            if val in carte:
                tri_chiffre.append(carte)

    return tri_chiffre


def trichiffre_couleur(main_du_joueur, cartes_du_milieu):
    tri_chiffre_couleurs = []
    cartes = main_du_joueur + cartes_du_milieu
    paquet_de_jeu = Piques + Trèfles + Coeurs + Carreaux

    for k in range(0, len(paquet_de_jeu)):
        if paquet_de_jeu[k] == cartes[0] or paquet_de_jeu[k] == cartes[1] or paquet_de_jeu[k] == cartes[2] or paquet_de_jeu[k] == cartes[3] or paquet_de_jeu[k] == cartes[4]:
            tri_chiffre_couleurs.append(paquet_de_jeu[k])

    return tri_chiffre_couleurs


def compteur_par_couleur(main_du_joueur, cartes_du_milieu):
    compteur_pique = 0
    compteur_trèfle = 0
    compteur_coeur = 0
    compteur_carreau = 0
    cartes = main_du_joueur + cartes_du_milieu

    for carte in cartes:
        if "Pique" in carte:
            compteur_pique += 1
        if "Trèfle" in carte:
            compteur_trèfle += 1
        if "Coeur" in carte:
            compteur_coeur += 1
        if "Carreau" in carte:
            compteur_carreau += 1

    return compteur_pique, compteur_trèfle, compteur_coeur, compteur_carreau


def compteur_de_valeurs(main_du_joueur, cartes_du_milieu):
    cartes = main_du_joueur + cartes_du_milieu
    ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for indice in range(0, len(ref)):
        for carte in cartes:
            if ref[indice] in carte:
                val[indice] += 1
    return val


def cherche_valeur_liste(liste, valeur):
    nb = 0

    for a in liste:
        if a == valeur:
            nb += 1

    return nb


def extracteur_de_valeur(carte, mode=None):
    ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    #temp = carte.split("_")

    if mode is not None:
        return ref[carte], ((len(ref) - 1) - carte)

    temp = carte.split("_")

    # renvoie d'abord la hauteur de la carte puis sa couleur
    return ((len(ref) - 1) - ref.index(temp[1])), temp[0]


def vérification_quinte_flush_royal(main_du_joueur, cartes_du_milieu):
    tri_chiffres_couleurs = trichiffre_couleur(main_du_joueur, cartes_du_milieu)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    if Piques[0:4] in tri_chiffres_couleurs or Trèfles[0:4] in tri_chiffres_couleurs or Carreaux[0:4] in tri_chiffres_couleurs or Coeurs[0:4] in tri_chiffres_couleurs:
        return 10, 13, somme
    else:
        return 0, 0, 0


def quinte_associée(carte,mode=True):
    ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    if mode == True:
        index = ref.index(carte)
        return ref[index:(index + 5)]
    else:
        index=carte
        return ref[index:(index + 5)]


def vérification_quinte_flush(main_du_joueur, cartes_du_milieu):
    pique = []
    coeur = []
    trèfle = []
    carreau = []
    tri_chiffres_couleurs = trichiffre_couleur(main_du_joueur, cartes_du_milieu)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    for carte in tri_chiffres_couleurs:
        if "Pique" in carte:
            pique.append(carte)
        if "Trèfle" in carte:
            trèfle.append(carte)
        if "Coeur" in carte:
            coeur.append(carte)
        if "Carreau" in carte:
            carreau.append(carte)
    for liste in [pique, trèfle, coeur, carreau]:
        if len(liste) == 5:
            for k in range(0, 5):
                liste[k] = extracteur_de_valeur(liste[k])[0]
                liste[k] = extracteur_de_valeur(liste[k], True)
                if quinte_associée(carte) in liste:
                    return 9, quinte_associée(carte)[0], somme
            return 0, 0, 0
        else:
            return 0, 0, 0


def vérification_carré(main_du_joueur, cartes_du_milieu):
    compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    if 4 in compteur:
        carte_haute = int(extracteur_de_valeur(compteur.index(4), True)[1])+2
        return 8, carte_haute, somme
    else:
        return 0, 0, 0


def vérification_full(main_du_joueur, cartes_du_milieu):
    compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
    nb_3 = cherche_valeur_liste(compteur, 3)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    if (2 in compteur and 5 in compteur) or (2 in compteur and 3 in compteur) or (2 in compteur and 4 in compteur) or (3 in compteur and 4 in compteur) or nb_3 == 2:
        carte_haute = int(extracteur_de_valeur(compteur.index(3), True)[1])+2
        return 7, carte_haute, somme
    else:
        return 0, 0, 0


def vérification_couleur(main_du_joueur, cartes_du_milieu):
    pique, trèfle, coeur, carreau = compteur_par_couleur(main_du_joueur, cartes_du_milieu)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)
    tri_chiffres= trichiffres(main_du_joueur, cartes_du_milieu)
    for k in tri_chiffres:
        val, couleur = extracteur_de_valeur(k)
        if couleur == 'Pique' and pique == 5:
            carte_haute = val
            break
        if couleur == 'Trèfle' and trèfle == 5:
            carte_haute = val
            break
        if couleur == 'Coeur' and coeur == 5:
            carte_haute = val
            break
        if couleur == 'Carreau' and carreau == 5:
            carte_haute = val
            break
    if pique == 5 or trèfle == 5 or coeur == 5 or carreau == 5:
        return 6, carte_haute, somme
    else:
        return 0, 0, 0


def vérification_suite(main_du_joueur, cartes_du_milieu):
    tri_chiffres = trichiffres(main_du_joueur, cartes_du_milieu)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    for k in range(0, len(tri_chiffres)):
        tri_chiffres[k] = extracteur_de_valeur(tri_chiffres[k])[0]
        #tri_chiffres[k] = extracteur_de_valeur(tri_chiffres[k], True)
    for val in tri_chiffres[0:3]:
        if quinte_associée(val, mode=False) in tri_chiffres:
            return 5, quinte_associée(val, mode = False)[0], somme
    return 0, 0, 0


def vérification_brelan(main_du_joueur, cartes_du_milieu):
    compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    if 3 in compteur:
        carte_haute = int(extracteur_de_valeur(compteur.index(3), True)[1])+2
        return 4, carte_haute, somme
    else:
        return 0, 0, 0


def vérification_double_paire(main_du_joueur, cartes_du_milieu):
    compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
    nb_2 = cherche_valeur_liste(compteur, 2)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    if nb_2 >= 2:
        carte_haute = int(extracteur_de_valeur(compteur.index(2), True)[1])+2
        return 3, carte_haute, somme
    else:
        return 0, 0, 0


def vérification_paire(main_du_joueur, cartes_du_milieu):
    compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
    _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

    if 2 in compteur:
        carte_haute = int(extracteur_de_valeur(compteur.index(2), True)[1]) +2
        return 2, carte_haute, somme
    else:
        return 0, 0, 0


def vérification_carte_la_plus_haute(main_du_joueur, _=None):
    somme = 0
    hauteur_max = 0

    for carte in main_du_joueur:
        hauteur, _ = extracteur_de_valeur(carte)
        if hauteur > hauteur_max:
            hauteur_max = hauteur
        somme += hauteur
    return 1, hauteur_max + 2, somme


def attributeur_de_valeur_par_joueur(mains, cartes_du_milieu):
    vérificateur = [
        vérification_quinte_flush_royal,
        vérification_quinte_flush,
        vérification_carré,
        vérification_full,
        vérification_couleur,
        vérification_suite,
        vérification_brelan,
        vérification_double_paire,
        vérification_paire,
        vérification_carte_la_plus_haute]

    données_des_joueurs = initialisation_de_dictionnaire(len(mains), 0)

    for joueur in mains:
        for fonction_de_vérification in vérificateur:
            données_pour_un_joueur = fonction_de_vérification(mains[joueur], cartes_du_milieu)
            if not données_pour_un_joueur[0] == 0:
                données_des_joueurs[joueur] = données_pour_un_joueur
                break
    return données_des_joueurs


def détermination_du_vainqueur(mains, cartes_du_milieu):
    données_des_joueurs = attributeur_de_valeur_par_joueur(mains, cartes_du_milieu)
    print(données_des_joueurs)
    joueurs_gagnants = []
    joueur_gagnant = ""
    id_combinaison_max = 0
    hauteur_max = 0
    départageur_max = 0

    for id_joueur in données_des_joueurs:
        joueur = données_des_joueurs[id_joueur]

        if joueur[0] > id_combinaison_max:
            id_combinaison_max = joueur[0]
            hauteur_max = joueur[1]
            départageur_max = joueur[2]
            joueur_gagnant = id_joueur
        else:
            if joueur[0] == id_combinaison_max and joueur[1] > hauteur_max:
                hauteur_max = joueur[1]
                joueur_gagnant = id_joueur
                départageur_max = joueur[2]
                
            else:
                if (joueur[0] > id_combinaison_max or joueur[0] == id_combinaison_max) and joueur[1] == hauteur_max and joueur[2] > départageur_max:
                    départageur_max = joueur[2]
                    joueur_gagnant = id_joueur
    for id_joueur in données_des_joueurs:
        joueur = données_des_joueurs[id_joueur]
        if joueur[0] == id_combinaison_max and joueur[1] == hauteur_max and joueur[2] == départageur_max:
                    if joueur not in joueurs_gagnants:
                        joueurs_gagnants.append(id_joueur)

    print(f"le joueur gagnant est {joueur_gagnant}", joueurs_gagnants)

def mise_a_niveau_argent(joueurs_gagnants, dico_argent, argent_au_milieu): #réinitioalisation du tapis de jeu (avec gain d'argent)
    argent_gagné = argent_au_milieu / len(joueurs_gagnants)
    for joueur in joueurs_gagnants:
        dico_argent[joueur] += argent_gagné
    return dico_argent, 0

Piques = ["Pique_As", "Pique_R", "Pique_D", "Pique_V", "Pique_10", "Pique_9", "Pique_8", "Pique_7", "Pique_6", "Pique_5", "Pique_4", "Pique_3", "Pique_2"]
Trèfles = ["Trèfle_As", "Trèfle_R", "Trèfle_D", "Trèfle_V", "Trèfle_10", "Trèfle_9", "Trèfle_8", "Trèfle_7", "Trèfle_6", "Trèfle_5", "Trèfle_4", "Trèfle_3", "Trèfle_2"]
Coeurs = ["Coeur_As", "Coeur_R", "Coeur_D", "Coeur_V", "Coeur_10", "Coeur_9", "Coeur_8", "Coeur_7", "Coeur_6", "Coeur_5", "Coeur_4", "Coeur_3", "Coeur_2"]
Carreaux = ["Carreau_As", "Carreau_R", "Carreau_D", "Carreau_V", "Carreau_10", "Carreau_9", "Carreau_8", "Carreau_7", "Carreau_6", "Carreau_5", "Carreau_4", "Carreau_3", "Carreau_2"]


def récupère_le_nombre_de_joueur(): 
    nombre_de_joueurs = 0

    while True:
        nombre_de_joueurs = int(input("Combien de joueurs ? > ")) #input.box mel
        if nombre_de_joueurs <= 1 or nombre_de_joueurs > 10:
            print("Nombre de joueurs doit être compris entre 0 et 10 !") #input.box mel
        else:
            break

    return nombre_de_joueurs


def initialisation_de_dictionnaire(nombre_de_joueurs, valeur_par_défaut):
    dictionnaire = {}
    for i in range(0, nombre_de_joueurs):
        dictionnaire['j' + str(i)] = valeur_par_défaut

    return dictionnaire


def distribution_des_cartes_joueurs(nombre_de_joueurs):
    paquet_de_jeu = Piques + Trèfles + Coeurs + Carreaux
    mains = initialisation_de_dictionnaire(nombre_de_joueurs, 0)

    for i in mains:
        mains[i] = [0, 0]
        mains[i][0] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1)) #afficher les cartes face cachée, 2 par joueur
        mains[i][1] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))

    return mains, paquet_de_jeu


def distribution_cartes_du_milieu(paquet_de_jeu):
    cartes_du_milieu = [0, 0, 0, 0, 0]

    for i in range(len(cartes_du_milieu)):
        if i == 0 or i >= 3:
            paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))
        cartes_du_milieu[i] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))

    return cartes_du_milieu, paquet_de_jeu

class Partie:
    def __init__(self):
        self.nombre_de_joueurs = récupère_le_nombre_de_joueur()
        #self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs(self.nombre_de_joueurs)
        #self.mises = self.mises = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)
        self.argent = self.argent = initialisation_de_dictionnaire(self.nombre_de_joueurs, 500)
        #self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)

class sous_Partie():
    def __init__(self, nombre_de_joueurs):
        self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs(nombre_de_joueurs)
        self.mises = initialisation_de_dictionnaire(nombre_de_joueurs, 0)
        self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)
        self.mise_verif = initialisation_de_dictionnaire(nombre_de_joueurs, 0)

def détermination_premier_dealer(nombre_de_joueurs):

    dealer = randint(0, nombre_de_joueurs - 1)
    print('Le dealer est le joueur numéro : ', dealer)

    return(dealer)
    
def détermination_dealer(dealer):
    
    dealer += 1
    print('Le nouveau dealer est le joueur numéro :', dealer)
    
    return(dealer)

def attribution_petite_blinde_grosse_blinde(nombre_de_joueurs, dealer, mise, argent):

    if nombre_de_joueurs > 2:

        if dealer <= nombre_de_joueurs-3:

            petite_blinde = int(input('petite blinde : '))
            while petite_blinde > argent['j'+str(dealer+1)]:
                petite_blinde = int(input('petite blinde : '))
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

            petite_blinde = int(input('petite blinde : '))
            while petite_blinde > argent['j0']:
                petite_blinde = int(input('petite blinde : '))
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
            petite_blinde = int(input('petite blinde : '))
            grosse_blinde = 2 * petite_blinde
            while petite_blinde > argent['j0'] and grosse_blinde > argent['j1']:
                petite_blinde = int(input('petite blinde : '))
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
        if dealer != nombre_de_joueurs - 1:
            joueur_actuel = 'j' + str(dealer + 1)
            numero_joueur_actuel = dealer + 1
            
        else:
            joueur_actuel = 'j0'
            numero_joueur_actuel = 0
    
    print("C'est à", joueur_actuel, "de jouer")

    return(joueur_actuel, numero_joueur_actuel)
       
def def_joueur_actuel(nombre_de_joueurs, dealer, joueur_actuel, numero_joueur_actuel):

    if joueur_actuel == 'j' + str(nombre_de_joueurs - 1):
        joueur_actuel = 'j0'
        numero_joueur_actuel = 0 
    else:
        joueur_actuel = 'j' + str(numero_joueur_actuel + 1)
        numero_joueur_actuel = numero_joueur_actuel + 1 

    print("C'est à", joueur_actuel, "de jouer")
    
    return(joueur_actuel, numero_joueur_actuel)

#def mise_verif(nombre_de_joueurs):

    mise_verif = initialisation_de_dictionnaire(nombre_de_joueurs, 0)

    return(mise_verif)

def def_mise_minimale(mise_verif, petite_blinde, mod = 'flop'):
    a = False
    for k in mise_verif:
        if mise_verif[k] == 0:
            a = True
        else:
            a = False
    if a == True and mod == 'flop':
        mise_minimale = petite_blinde
    elif a == True and mod == 'turn/river':
        mise_minimale = 0
    else:
        maxi = None
        for k in mise_verif:
            if maxi == None or mise_verif[k] > maxi:
                maxi = mise_verif[k]
        mise_minimale = maxi
    return(mise_minimale)

def avancee_tour(mise, present, mise_verif):
    tour = True
    if present != {}:
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

    return(tour)

def actions_possibles(joueur_actuel, present, mise_minimale, argent, mise, mise_verif, petite_blinde, mod = 'flop'):

        if joueur_actuel in present:

            print('Voici les actions que tu peux faire :')
            if mod == 'flop':
                if argent[joueur_actuel] >= def_mise_minimale(mise_verif, petite_blinde, mod = 'flop'):
                    print("s'aligner")
                    print("miser jusqu'à", argent[joueur_actuel] - mise[joueur_actuel])
                elif argent[joueur_actuel] >= def_mise_minimale(mise_verif, petite_blinde, mod = 'turn/river'):
                    print("s'aligner")
                    print("miser jusqu'à", argent[joueur_actuel] - mise[joueur_actuel]) 
            print('se coucher')
            
def action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent, nombre_de_joueurs, dealer, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'flop'):

    if joueur_actuel in present:
        actions_possibles(joueur_actuel, present, mise_minimale, argent, mise, mise_verif, petite_blinde)
        a = input('Que veux-tu faire ? :')   
        while a != "s'aligner" and a != 'miser' and a != 'se coucher':
            a = input('Que veux-tu faire ? :') 
        if a == "s'aligner": 
            if mod == 'flop':
                if numero_joueur_actuel == numero_petite_blinde:
                    mise[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'flop') + petite_blinde
                elif numero_joueur_actuel == numero_grosse_blinde:
                    mise[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'flop') + grosse_blinde 
                else:
                    mise[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'flop')
                mise_verif[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'flop')
            else:
                if numero_joueur_actuel == numero_petite_blinde:
                    mise[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'turn/river') + petite_blinde
                elif numero_joueur_actuel == numero_grosse_blinde:
                    mise[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'turn/river') + grosse_blinde 
                else:
                    mise[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'turn/river')
                mise_verif[joueur_actuel] = def_mise_minimale(mise_verif, petite_blinde, mod = 'turn/river') 
        elif a == "miser":
            print("Combien veux-tu miser ? jusqu'à", argent[joueur_actuel] - mise[joueur_actuel])
            a_miser = int(input())
            while a_miser > argent[joueur_actuel] - mise[joueur_actuel]:
                a_miser = int(input("Vous navez pas assez, nouvelle mise : "))
            mise[joueur_actuel] += a_miser
            mise_verif[joueur_actuel] += a_miser
            mise_minimale = mise_verif[joueur_actuel]
        else:
            present.discard(joueur_actuel)
    joueur_actuel, numero_joueur_actuel = def_joueur_actuel(nombre_de_joueurs, dealer, joueur_actuel, numero_joueur_actuel)

    return(mise, mise_verif, mise_minimale, present, joueur_actuel, numero_joueur_actuel)


def tour_de_jeu(nombre_de_joueurs, mise, argent, mise_verif, dealer):

    present = joueur_present(nombre_de_joueurs)
    petite_blinde, grosse_blinde, numero_petite_blinde, numero_grosse_blinde, mise_minimale = attribution_petite_blinde_grosse_blinde(nombre_de_joueurs, dealer, mise, argent) 
    joueur_actuel, numero_joueur_actuel = premier_joueur(nombre_de_joueurs, dealer, mod = 'flop')
    tour = True
    print(mise_verif)

    #attention : on ne peut pas miser moins que la personne d'avant

    print('Début du tour de flop')

    for i in range(nombre_de_joueurs):

        mise, mise_verif, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent, nombre_de_joueurs, dealer, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'flop')
        print(mise_verif)
        print(joueur_actuel)
        print(present)

    tour = avancee_tour(mise, present, mise_verif)

    while tour == True:


        mise, mise_verif, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent, nombre_de_joueurs, dealer, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'flop')
        
        tour = avancee_tour(mise, present, mise_verif)

    print('Début du tour de turn')

#retourner les 3 cartes de flop (aurel et mel)
    joueur_actuel, numero_joueur_actuel = premier_joueur(nombre_de_joueurs, dealer, mod = 'turn')
    if present != {}:
        tour = True

    for i in range(nombre_de_joueurs):

        mise, mise_verif, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent, nombre_de_joueurs, dealer, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')

    tour = avancee_tour(mise, present, mise_verif)

    while tour == True:

        mise, mise_verif, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent, nombre_de_joueurs, dealer, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')
        
        tour = avancee_tour(mise, present, mise_verif) 

    print('Début du tour de river')

#retourner la carte de turn (aurel et mel)
    joueur_actuel, numero_joueur_actuel = premier_joueur(nombre_de_joueurs, dealer, mod = 'river')
 
    if present != {}:
        tour = True

    for i in range(nombre_de_joueurs):

        mise, mise_verif, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent, nombre_de_joueurs, dealer, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')
    
    tour = avancee_tour(mise, present, mise_verif)

    while tour == True:
    
        mise, mise_verif, mise_minimale, present, joueur_actuel, numero_joueur_actuel = action_a_faire(joueur_actuel, mise, mise_verif, mise_minimale, present, argent, nombre_de_joueurs, dealer, numero_joueur_actuel, numero_petite_blinde, numero_grosse_blinde, petite_blinde, grosse_blinde, mod = 'turn/river')
        
        tour = avancee_tour(mise, present, mise_verif)
    return (present)
    
#retourner la carte de river (aurel et mel)

partie = Partie()
sous_partie = sous_Partie(partie.nombre_de_joueurs)

#tour_de_jeu(partie.nombre_de_joueurs, sous_partie.mises, partie.argent, sous_partie.mise_verif)
