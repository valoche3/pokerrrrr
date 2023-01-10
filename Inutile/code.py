# from random import randint


# Piques = ["Pique_As", "Pique_R", "Pique_D", "Pique_V", "Pique_10", "Pique_9", "Pique_8", "Pique_7", "Pique_6", "Pique_5", "Pique_4", "Pique_3", "Pique_2"]
# Trèfles = ["Trèfle_As", "Trèfle_R", "Trèfle_D", "Trèfle_V", "Trèfle_10", "Trèfle_9", "Trèfle_8", "Trèfle_7", "Trèfle_6", "Trèfle_5", "Trèfle_4", "Trèfle_3", "Trèfle_2"]
# Coeurs = ["Coeur_As", "Coeur_R", "Coeur_D", "Coeur_V", "Coeur_10", "Coeur_9", "Coeur_8", "Coeur_7", "Coeur_6", "Coeur_5", "Coeur_4", "Coeur_3", "Coeur_2"]
# Carreaux = ["Carreau_As", "Carreau_R", "Carreau_D", "Carreau_V", "Carreau_10", "Carreau_9", "Carreau_8", "Carreau_7", "Carreau_6", "Carreau_5", "Carreau_4", "Carreau_3", "Carreau_2"]


# def récupère_le_nombre_de_joueur():
#     nombre_de_joueurs = 0

#     while True:
#         nombre_de_joueurs = int(input("Combien de joueurs ? > "))
#         if nombre_de_joueurs <= 1 or nombre_de_joueurs > 10:
#             print("Nombre de joueurs doit être compris entre 0 et 10 !")
#         else:
#             break

#     return nombre_de_joueurs


# def initialisation_de_dictionnaire(nombre_de_joueurs, valeur_par_défaut):
#     dictionnaire = {}
#     for i in range(0, nombre_de_joueurs):
#         dictionnaire['j' + str(i)] = valeur_par_défaut

#     return dictionnaire


# def distribution_des_cartes_joueurs(nombre_de_joueurs):
#     paquet_de_jeu = Piques + Trèfles + Coeurs + Carreaux
#     mains = initialisation_de_dictionnaire(nombre_de_joueurs, 0)

#     for i in mains:
#         mains[i] = [0, 0]
#         mains[i][0] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))
#         mains[i][1] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))

#     return mains, paquet_de_jeu


# def distribution_cartes_du_milieu(paquet_de_jeu):
#     cartes_du_milieu = [0, 0, 0, 0, 0]

#     for i in range(len(cartes_du_milieu)):
#         if i == 0 or i >= 3:
#             paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))
#         cartes_du_milieu[i] = paquet_de_jeu.pop(randint(0, len(paquet_de_jeu) - 1))

#     return cartes_du_milieu, paquet_de_jeu


# class Partie:
#     def __init__(self):
#         self.nombre_de_joueurs = récupère_le_nombre_de_joueur()
#         #self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs(self.nombre_de_joueurs)
#         #self.mises = self.mises = initialisation_de_dictionnaire(self.nombre_de_joueurs, 0)
#         self.argent = self.argent = initialisation_de_dictionnaire(self.nombre_de_joueurs, 500)
#         #self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)
# class sous_Partie():
#     def __init__(self, nombre_de_joueurs):
#         self.mains, self.paquet_de_jeu = distribution_des_cartes_joueurs(nombre_de_joueurs)
#         self.mises = self.mises = initialisation_de_dictionnaire(nombre_de_joueurs, 0)
#         self.cartes_du_milieu, self.paquet_de_jeu = distribution_cartes_du_milieu(self.paquet_de_jeu)


# from src.miseEnPlace import initialisation_de_dictionnaire

# Piques = ["Pique_As", "Pique_R", "Pique_D", "Pique_V", "Pique_10", "Pique_9", "Pique_8", "Pique_7", "Pique_6", "Pique_5", "Pique_4", "Pique_3", "Pique_2"]
# Trèfles = ["Trèfle_As", "Trèfle_R", "Trèfle_D", "Trèfle_V", "Trèfle_10", "Trèfle_9", "Trèfle_8", "Trèfle_7", "Trèfle_6", "Trèfle_5", "Trèfle_4", "Trèfle_3", "Trèfle_2"]
# Coeurs = ["Coeur_As", "Coeur_R", "Coeur_D", "Coeur_V", "Coeur_10", "Coeur_9", "Coeur_8", "Coeur_7", "Coeur_6", "Coeur_5", "Coeur_4", "Coeur_3", "Coeur_2"]
# Carreaux = ["Carreau_As", "Carreau_R", "Carreau_D", "Carreau_V", "Carreau_10", "Carreau_9", "Carreau_8", "Carreau_7", "Carreau_6", "Carreau_5", "Carreau_4", "Carreau_3", "Carreau_2"]


# # trichiffres : fonction qui trie par chiffres+couleurs et par chiffres
# def trichiffres(main_du_joueur, cartes_du_milieu):
#     tri_chiffre = []
#     ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#     cartes = main_du_joueur + cartes_du_milieu

#     for val in ref:
#         for carte in cartes:
#             if val in carte:
#                 tri_chiffre.append(carte)

#     return tri_chiffre


# def trichiffre_couleur(main_du_joueur, cartes_du_milieu):
#     tri_chiffre_couleurs = []
#     cartes = main_du_joueur + cartes_du_milieu
#     paquet_de_jeu = Piques + Trèfles + Coeurs + Carreaux

#     for k in range(0, len(paquet_de_jeu)):
#         if paquet_de_jeu[k] == cartes[0] or paquet_de_jeu[k] == cartes[1] or paquet_de_jeu[k] == cartes[2] or paquet_de_jeu[k] == cartes[3] or paquet_de_jeu[k] == cartes[4]:
#             tri_chiffre_couleurs.append(paquet_de_jeu[k])

#     return tri_chiffre_couleurs


# def compteur_par_couleur(main_du_joueur, cartes_du_milieu):
#     compteur_pique = 0
#     compteur_trèfle = 0
#     compteur_coeur = 0
#     compteur_carreau = 0
#     cartes = main_du_joueur + cartes_du_milieu

#     for carte in cartes:
#         if "Pique" in carte:
#             compteur_pique += 1
#         if "Trèfle" in carte:
#             compteur_trèfle += 1
#         if "Coeur" in carte:
#             compteur_coeur += 1
#         if "Carreau" in carte:
#             compteur_carreau += 1

#     return compteur_pique, compteur_trèfle, compteur_coeur, compteur_carreau


# def compteur_de_valeurs(main_du_joueur, cartes_du_milieu):
#     cartes = main_du_joueur + cartes_du_milieu
#     ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#     val = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#     for indice in range(0, len(ref)):
#         for carte in cartes:
#             if ref[indice] in carte:
#                 val[indice] += 1
#     return val


# def cherche_valeur_liste(liste, valeur):
#     nb = 0

#     for a in liste:
#         if a == valeur:
#             nb += 1

#     return nb


# def extracteur_de_valeur(carte, mode=None):
#     ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#     #temp = carte.split("_")

#     if mode is not None:
#         return ref[carte], ((len(ref) - 1) - carte)

#     temp = carte.split("_")

#     # renvoie d'abord la hauteur de la carte puis sa couleur
#     return ((len(ref) - 1) - ref.index(temp[1])), temp[0]


# def vérification_quinte_flush_royal(main_du_joueur, cartes_du_milieu):
#     tri_chiffres_couleurs = trichiffre_couleur(main_du_joueur, cartes_du_milieu)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     if Piques[0:4] in tri_chiffres_couleurs or Trèfles[0:4] in tri_chiffres_couleurs or Carreaux[0:4] in tri_chiffres_couleurs or Coeurs[0:4] in tri_chiffres_couleurs:
#         return 10, 13, somme
#     else:
#         return 0, 0, 0


# def quinte_associée(carte,mode=True):
#     ref = ["As", "R", "D", "V", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#     if mode == True:
#         index = ref.index(carte)
#         return ref[index:(index + 5)]
#     else:
#         index=carte
#         return ref[index:(index + 5)]


# def vérification_quinte_flush(main_du_joueur, cartes_du_milieu):
#     pique = []
#     coeur = []
#     trèfle = []
#     carreau = []
#     tri_chiffres_couleurs = trichiffre_couleur(main_du_joueur, cartes_du_milieu)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     for carte in tri_chiffres_couleurs:
#         if "Pique" in carte:
#             pique.append(carte)
#         if "Trèfle" in carte:
#             trèfle.append(carte)
#         if "Coeur" in carte:
#             coeur.append(carte)
#         if "Carreau" in carte:
#             carreau.append(carte)
#     for liste in [pique, trèfle, coeur, carreau]:
#         if len(liste) == 5:
#             for k in range(0, 5):
#                 liste[k] = extracteur_de_valeur(liste[k])[0]
#                 liste[k] = extracteur_de_valeur(liste[k], True)
#                 if quinte_associée(carte) in liste:
#                     return 9, quinte_associée(carte)[0], somme
#             return 0, 0, 0
#         else:
#             return 0, 0, 0


# def vérification_carré(main_du_joueur, cartes_du_milieu):
#     compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     if 4 in compteur:
#         carte_haute = int(extracteur_de_valeur(compteur.index(4), True)[1])+2
#         return 8, carte_haute, somme
#     else:
#         return 0, 0, 0


# def vérification_full(main_du_joueur, cartes_du_milieu):
#     compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
#     nb_3 = cherche_valeur_liste(compteur, 3)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     if (2 in compteur and 5 in compteur) or (2 in compteur and 3 in compteur) or (2 in compteur and 4 in compteur) or (3 in compteur and 4 in compteur) or nb_3 == 2:
#         carte_haute = int(extracteur_de_valeur(compteur.index(3), True)[1])+2
#         return 7, carte_haute, somme
#     else:
#         return 0, 0, 0


# def vérification_couleur(main_du_joueur, cartes_du_milieu):
#     pique, trèfle, coeur, carreau = compteur_par_couleur(main_du_joueur, cartes_du_milieu)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)
#     tri_chiffres= trichiffres(main_du_joueur, cartes_du_milieu)
#     for k in tri_chiffres:
#         val, couleur = extracteur_de_valeur(k)
#         if couleur == 'Pique' and pique == 5:
#             carte_haute = val
#             break
#         if couleur == 'Trèfle' and trèfle == 5:
#             carte_haute = val
#             break
#         if couleur == 'Coeur' and coeur == 5:
#             carte_haute = val
#             break
#         if couleur == 'Carreau' and carreau == 5:
#             carte_haute = val
#             break
#     if pique == 5 or trèfle == 5 or coeur == 5 or carreau == 5:
#         return 6, carte_haute, somme
#     else:
#         return 0, 0, 0


# def vérification_suite(main_du_joueur, cartes_du_milieu):
#     tri_chiffres = trichiffres(main_du_joueur, cartes_du_milieu)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     for k in range(0, len(tri_chiffres)):
#         tri_chiffres[k] = extracteur_de_valeur(tri_chiffres[k])[0]
#         #tri_chiffres[k] = extracteur_de_valeur(tri_chiffres[k], True)
#     for val in tri_chiffres[0:3]:
#         if quinte_associée(val, mode=False) in tri_chiffres:
#             return 5, quinte_associée(val, mode = False)[0], somme
#     return 0, 0, 0


# def vérification_brelan(main_du_joueur, cartes_du_milieu):
#     compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     if 3 in compteur:
#         carte_haute = int(extracteur_de_valeur(compteur.index(3), True)[1])+2
#         return 4, carte_haute, somme
#     else:
#         return 0, 0, 0


# def vérification_double_paire(main_du_joueur, cartes_du_milieu):
#     compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
#     nb_2 = cherche_valeur_liste(compteur, 2)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     if nb_2 >= 2:
#         carte_haute = int(extracteur_de_valeur(compteur.index(2), True)[1])+2
#         return 3, carte_haute, somme
#     else:
#         return 0, 0, 0


# def vérification_paire(main_du_joueur, cartes_du_milieu):
#     compteur = compteur_de_valeurs(main_du_joueur, cartes_du_milieu)
#     _, _, somme = vérification_carte_la_plus_haute(main_du_joueur)

#     if 2 in compteur:
#         carte_haute = int(extracteur_de_valeur(compteur.index(2), True)[1]) +2
#         return 2, carte_haute, somme
#     else:
#         return 0, 0, 0


# def vérification_carte_la_plus_haute(main_du_joueur, _=None):
#     somme = 0
#     hauteur_max = 0

#     for carte in main_du_joueur:
#         hauteur, _ = extracteur_de_valeur(carte)
#         if hauteur > hauteur_max:
#             hauteur_max = hauteur
#         somme += hauteur
#     return 1, hauteur_max + 2, somme


# def attributeur_de_valeur_par_joueur(mains, cartes_du_milieu):
#     vérificateur = [
#         vérification_quinte_flush_royal,
#         vérification_quinte_flush,
#         vérification_carré,
#         vérification_full,
#         vérification_couleur,
#         vérification_suite,
#         vérification_brelan,
#         vérification_double_paire,
#         vérification_paire,
#         vérification_carte_la_plus_haute]

#     données_des_joueurs = initialisation_de_dictionnaire(len(mains), 0)

#     for joueur in mains:
#         for fonction_de_vérification in vérificateur:
#             données_pour_un_joueur = fonction_de_vérification(mains[joueur], cartes_du_milieu)
#             if not données_pour_un_joueur[0] == 0:
#                 données_des_joueurs[joueur] = données_pour_un_joueur
#                 break
#     return données_des_joueurs


# def détermination_du_vainqueur(mains, cartes_du_milieu):
#     données_des_joueurs = attributeur_de_valeur_par_joueur(mains, cartes_du_milieu)
#     print(données_des_joueurs)
#     joueurs_gagnants = []
#     joueur_gagnant = ""
#     id_combinaison_max = 0
#     hauteur_max = 0
#     départageur_max = 0

#     for id_joueur in données_des_joueurs:
#         joueur = données_des_joueurs[id_joueur]

#         if joueur[0] > id_combinaison_max:
#             id_combinaison_max = joueur[0]
#             hauteur_max = joueur[1]
#             départageur_max = joueur[2]
#             joueur_gagnant = id_joueur
#         else:
#             if joueur[0] == id_combinaison_max and joueur[1] > hauteur_max:
#                 hauteur_max = joueur[1]
#                 joueur_gagnant = id_joueur
#                 départageur_max = joueur[2]
                
#             else:
#                 if (joueur[0] > id_combinaison_max or joueur[0] == id_combinaison_max) and joueur[1] == hauteur_max and joueur[2] > départageur_max:
#                     départageur_max = joueur[2]
#                     joueur_gagnant = id_joueur
#     for id_joueur in données_des_joueurs:
#         joueur = données_des_joueurs[id_joueur]
#         if joueur[0] == id_combinaison_max and joueur[1] == hauteur_max and joueur[2] == départageur_max:
#                     if joueur not in joueurs_gagnants:
#                         joueurs_gagnants.append(id_joueur)

#     print(f"le joueur gagnant est {joueur_gagnant}", joueurs_gagnants)


# from src.miseEnPlace import distribution_des_cartes_joueurs 

# def mise_a_niveau_argent(joueurs_gagnants, dico_argent, argent_au_milieu):
#     argent_gagné = argent_au_milieu / len(joueurs_gagnants)
#     for joueur in joueurs_gagnants:
#         dico_argent[joueur] += argent_gagné
#     return dico_argent, 0
