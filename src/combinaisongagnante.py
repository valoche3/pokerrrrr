
from src.miseEnPlace import initalisation_de_dictionnaire
#fonction qui trie par chiffres+couleurs et par chiffres
# res=[]
# tri_chiffre=[]
# tri_chiffres_couleurs=[]
# for j in joueurs: 
#     tot = cartes + joueurs[j]
#     for k in range(0,len(paquet)):
#         if paquet[k]== tot[0] or paquet[k]== tot[1] or paquet[k]== tot[2] or paquet[k]== tot[3]or paquet[k]== tot[4]:
#             tri_chiffres_couleurs.append(paquet[k])
#     for p in tot:
#         if 'R' in p:
#             tri_chiffre.append(p)
#         if 'D' in p:
#             tri_chiffre.append(p)
#         if 'V' in p:
#             tri_chiffre.append(p)
#         if '10' in p:
#             tri_chiffre.append(p)
#         if '9' in p:
#             tri_chiffre.append(p)
#         if '8' in p:
#             tri_chiffre.append(p)
#         if '7' in p:
#             tri_chiffre.append(p)
#         if '6' in p:
#             tri_chiffre.append(p)
#         if '5' in p:
#             tri_chiffre.append(p)
#         if '4' in p:
#             tri_chiffre.append(p)
#         if '3' in p:
#             tri_chiffre.append(p)
#         if '2' in p:
#             tri_chiffre.append(p)

# #Compter le nombre de chaque couleur
# compteur_pique=0
# compteur_trèfle=0
# compteur_coeur=0
# compteur_carreau=0
# val=[0,0,0,0,0,0,0,0,0,0,0,0]
# for j in tot:
#     while 'Pi' in j:
#         compteur_pique += 1
#     while 'Tr' in j:
#         compteur_trèfle += 1
#     while 'Co' in j:
#         compteur_coeur += 1
#     while 'Ca' in j:
#         compteur_carreau +=1
# for k in tot: 
#     if 'R' in p:
#             val[0]+=1
#     if 'D' in p:
#             val[1]+=1
#     if 'V' in p:
#             val[2]+=1
#     if '10' in p:
#             val[3]+=1
#     if '9' in p:
#             val[4]+=1
#     if '8' in p:
#             val[5]+=1
#     if '7' in p:
#             val[6]+=1
#     if '6' in p:
#             val[7]+=1
#     if '5' in p:
#             val[8]+=1
#     if '4' in p:
#             val[9]+=1
#     if '3' in p:
#             val[10]+=1
#     if '2' in p:
#             val[11]+=1

# if compteur_pique >= 5 or compteur_trèfle>= 5 or compteur_carreau>=5 or compteur_coeur>= 5:
#     #le test pour quinte flush royal
#     if Piques[0,4] in tri_chiffres_couleurs or Trèfles[0,4] in tri_chiffres_couleurs or Carreaux[0,4] in tri_chiffres_couleurs or Coeurs[0,4] in tri_chiffres_couleurs:
#         test_gain[j][0]= 10
#         test_gain[j][1]=0
       

#     #faire le test pour quinte flush


# if 4 in val:
#     #on a un carré
#     test_gain[j][0]=8
#     test_gain[j][1]=val.index(4)
  
# # on compte le nombre de 3 dans val
# nb_3=0
# for a in val:
#     if a ==3:
#         nb_3+=1
# if ( 2 in val and 5 in val) or (2 in val and 3 in val) or (2 in val and 4 in val) or ( 3 in val and 4 in val) or nb_3==2:
#     #on a un full
#     test_gain[j][0]=7
#     k=0
#     for i in range (len(val)-1,0)
#         while k!=-1:
#         if val[i]==5 or val[i]==4 or val[i]==3:
#             k=-1
#             test_gain[j][1]= i

# if compteur_pique >= 5 or compteur_trèfle>= 5 or compteur_carreau>=5 or compteur_coeur>= 5:
#     #on a une couleur
#     test_gain[j][0]=6
#     for i in tri_chiffre:


# #test suite quinte

# if 3 in val or 4 in val:
#     #on a un brelan
#     test_gain[j][0]=4

# #on compte le nombre de 2 dans val
# nb_2=0
# for i in val:
#     if i==2:
#         nb_2+=1
# if nb_2>=2:
#     #on a deux paires
#     test_gain[j][0]=3

# if 2 in val :
#     #on a une paire
#     test_gain[j][0]=2

#carte la plus haute

def extracteur_de_valeur(carte):
    ref = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "As"]

    temp = carte.split("_")

    # renvoie d'abord la hauteur de la carte puis sa couleur
    return ref.index(temp[1]), temp[0]


def vérification_quinte_flush_royal(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_quinte_flush(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_carré(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_full(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_couleur(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_suite(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_brelan(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_double_paire(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_paire(main_du_joueur, cartes_du_milieu):
    return 0, 0, 0


def vérification_carte_la_plus_haute(main_du_joueur, cartes_du_milieu):
    somme = 0
    hauteur_max = 0
    for carte in main_du_joueur:
        hauteur, _ = extracteur_de_valeur(carte)
        if hauteur > hauteur_max:
            hauteur_max = hauteur
        somme += hauteur
    return 1, hauteur_max, somme


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
        vérification_carte_la_plus_haute
    ]

    données_des_joueurs = initalisation_de_dictionnaire(len(mains), 0)

    for joueur in mains:
        données_pour_un_joueur = [0, 0, 0]
        for fonction_de_vérification in vérificateur:
            données_des_joueurs[joueur] = fonction_de_vérification(mains[joueur], cartes_du_milieu)
            if not données_pour_un_joueur[0] == 0:
                break
    return données_des_joueurs


def détermination_du_vainqueur(mains, cartes_du_milieu):
    données_des_joueurs = attributeur_de_valeur_par_joueur(mains, cartes_du_milieu)
    print(données_des_joueurs)
    

    joueur_gagnant = ""
    id_combinaison_max = 0
    hauteur_max = 0
    départageur_max = 0

    for données_joueur in données_des_joueurs:
        
        if données_des_joueurs[données_joueur][0] > id_combinaison_max:
            id_combinaison_max = données_des_joueurs[données_joueur][0]
            hauteur_max = données_des_joueurs[données_joueur][1]
            départageur_max = données_des_joueurs[données_joueur][2]
            joueur_gagnant= données_joueur
       
        else:
            
            if données_des_joueurs[données_joueur][0] == id_combinaison_max and données_des_joueurs[données_joueur][1] > hauteur_max:
                hauteur_max = données_des_joueurs[données_joueur][1]
                joueur_gagnant = données_joueur
                départageur_max = données_des_joueurs[données_joueur][2]
                
            else:
                    
                if données_des_joueurs[données_joueur][1] == hauteur_max and données_des_joueurs[données_joueur][2] > départageur_max:
                        départageur_max = données_des_joueurs[données_joueur][2]
                        joueur_gagnant = données_joueur
    
    print("le joueur gagnant est ", joueur_gagnant)

            
    


        
        

