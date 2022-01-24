#!/usr/bin/python3
import random
import sys
import time
#import pygame
#from pygame.locals import *

'''
#Initialisation de la bibliothèque Pygame
pygame.init()

#Création de la fenêtre
fenetre = pygame.display.set_mode((1500, 780),RESIZABLE)

#Chargement et collage du fond

fond = pygame.image.load("img/background.jpg").convert()

fenetre.blit(fond, (0,0))


#Rafraîchissement de l'écran

pygame.display.flip()
'''
def game_Rules():
    global GOLD,MAX_JOUEUR
    print("Les Règles du Monopoly !")
    print("\n\n\033[36mLE JEU EN BREF :\033[0m\n")
    print("\tMonopoly est le jeu où l'on achète, loue et vend des propriétés de façon à accroître ses richesses - le joueur le plus riche étant le vainqueur.\n\tEn partant de la case départ, déplacez votre pion sur le plateau de jeu suivant votre résultat au lancer de dés.\n\tQuand vous arrivez sur une case qui n'appartient encore à personne, vous pouvez l'acheter à la banque.\n\tSi vos décidez de ne pas l'acheter, la propriété sera proposée aux enchères et reviendra au plus offrant.\n\tLes joueurs qui sont propriétaires perçoivent des loyers de la part des adversaires s'arrêtant sur leur terrain.\n\tLa construction des maisons et hôtels augmente considérablement le loyer que vous pouvez percevoir pour vos propriétés ; aussi, il est conseillé de construire dans un maximum de sites.\n\tSi vous avez besoin davantage d'argent, la banque peut vous en prêter par la biais d'hypothèque sur vos propriétés.\n\tVous devez toujours vous plier aux instructions données par les cartes caisse de communauté et chance.\n\tParfois, vous serez envoyé en prison.\n")
    print("\n\033[36mBUT DU JEU :\033[0m\n\n\tÊtre le seul joueur à ne pas être en faillite.\n")
    print("\n\033[36mDEROULEMENT :\033[0m\n")
    print("\tDans ce Monopoly Digital, le banquier a une portée monétaire illimitée. Elle ne peut pas faire faillite et elle ne contracte aucune dette retardataire.")
    print("\tLes joueurs choisiront leur pseudonyme ou leur prénom pour les identifier.\n\tPour des questions pratiques, veuillez définir des pseudonymes différents les uns des autres.")
    print("\tLes joueurs démarrent le jeu avec une solde de",GOLD,"pièces d'or.")
    print("\tIl ne peut y avoir que",MAX_JOUEUR,"joueurs maximum. Et un minimum de 2 joueurs.")
    print("\tDe plus la banque verse des salaires ou des primes, prête de l'argent sur les propriétés hypothéquées et encaisse l'argent des taxes, des amendes, des prêts et intérêts.\n\tDans le cas d'une vente aux enchères, c'est le banquier qui dirige la vente.")
    print("\tLe premier joueur à commencer la partie est préselectionné aléatoirement de manière indépendante par la machine.")
    print("\n\033[36mUNE PARTIE DE MONOPOLY :\033[0m\n")
    print("\tQuand c'est votre tour, lancez les deux dés et avancez d'autant de cases que le nombre de points indiqués sur les dés.\n\tLa case où vous vous arrêterez determinera ce que vous avez à faire. Deux pions ou plus peuvent d'arrêter sur la même case en même temps. Suivant la case où vous vous arrêter, vous pouvez :")
    print("\n\t\t> Acheter une propriété\n\t\t> Payer un loyer au propriétaire\n\t\t> Payer des taxes\n\t\t> Tirer une carte chance et caisse de communauté\n\t\t> Aller en prison\n\t\t> Vous reposer sur le parc gratuit\n\t\t> Toucher votre salaire de 20 000 pièces d'or.")
    print("\n\033[36mDOUBLE :\033[0m\n")
    print("\n\tSi vous faites un double, effectuez les opérations habituelles sur la case où vous vous arrêtez, puis relancez les dés.\n\tSi vous faites trois doubles à la suite, rendez-vous imméditement en prison.")
    print("\n\033[36mCASE DEPART :\033[0m\n")
    print("\n\tChaque fois que vous passez sur la case Départ, vous recevez 20 000 pièces d'or de la banque.\n\tIl est possible de percevoir deux salaires pendant le même tour si, par exemple,\n\tvous tirez une cartes chance ou caisse de communauté juste après être passé par la case départ, et que cette carte vous indique 'Avancez jusqu'à la case départ'\n\tVous obtenez un salaire double lorsque vous êtes sur la case départ.")
    print("\n\033[36mACHAT DE PROPRIETES :\033[0m\n")
    print("\n\tSi vous vous arrêtez sur une propriété qui n'appartient pas déjà à un autre joueur, vous pouvez l'acheter.\n\tSi vous décidez de l'acheter, payez à la banque le prix indiqué sur la case.\n\tVous recevrez en échange, comme preuve de cette acquisition, une carte de propriété que vous devez garder face visible devant vous.\n\tSi vous décidez de ne pas l'acheter, le banquier doit immédiatement ouvrir une vente aux enchères,en commençant à n'importe quel prix fixé par un joueur désireux d'acheter.\n\tLa propriété revient au plus offrant. Même si vous avez refusé de l'acheter au prix initial, vous pouvez participer à la vente aux enchères.")
    print("\n\033[36mÊTRE PROPRIETAIRE :\033[0m\n")
    print("\tLe fait d'être propriétaire vous permet de percevoir un loyer de la part de tous les locataires qui s'arrêtent sur vos terrains.\n\tVous pouvez construire sur n'importe quelle propriété à partir du moment où vous possédez tous les terrains de la même couleur que celle-ci, \033[33mc'est-à-dire dès que vous en avez le monopole.\033[0m")
    print("\n\033[36mARRÊT SUR UNE PROPRIETE DEJA ACHETEE :\033[0m\n")
    print("\tSi vous vous arrêtez sur une propriété qui a été achetée par un autre joueur, il peut vous réclamer un loyer.\n\tLe joueur qui est propriétaire de cette case doit vous réclamer le loyer avant que le deuxième joueur après vous ait lancé les dés.\n\tLe montant du loyer est indiqué sur la carte de propriété et varie selon le nombre de bâtiments qu'elle comporte.\n\tSi toutes les propriétés d'un même groupe (terrains de même couleur) appartiennent au même joueur, le loyer est doublé pour chaque propriété de ce groupe où il n'y a pas encore de construction.\n\tToutefois, un propriétaire qui possède tout un groupe ne peut pas recevoir ce double loyer si une des propriétés est hypothéquée.\n\tSur les terrains où des maisons et des hôtels ont été construits, le loyer à payer est indiqué sur la carte de propriété correspondante.\n\tAucun loyer ne sera dû pour une propriété hypothéquée.")
    print("\n\033[36mARRÊT SUR UN SERVICE PUBLIC :\033[0m\n")
    print("\tSi vous vous arrêtez sur un service public, vous pouvez l'acquérir s'il n'a pas encore été acheté.\n\tComme pour les autres propriétés, payez la somme dûe à la banque.\n\tS'il appartient déjà à un autre joueur, ce joueur peut vous demander de lui payer un loyer suivant le nombre de points obtenus aux dés.\n\tSi le propriétaire a seulement un des deux services publics, le loyer sera le total de vos dés multiplié par 400.\n\tMais si le propriétaire a les deux en sa possession, vous devez payer 1000 fois le total des dés.\n\tSi vous êtes 'envoyé' sur cette case à cause d'une carte chance ou caisse de communauté, vous devez relancer les dés pour déterminer le montant à payer.")
    print("\n\033[36mARRÊT SUR UNE GARE :\033[0m\n")
    print("\tSi vous êtes le premier à vous arrêter sur une gare, vous avez la possibilité de l'acheter.\n\tSinon, elle sera mise en vente par le banquier dans une vente aux enchères à laquelle vous pourrez participer.\n\tSi la gare appartient déjà à un autre joueur, vous devez payer le montant indiqué sur la carte de propriété.\n\tCe montant variera suivant le nombre de gares détenues par ce joueur.")


def init():
    global NB_player,player1,player2,player3,or1,or2,or3,position1,position2,position3,GOLD,player1_en_Prison,player2_en_Prison,player3_en_Prison,MAISON_QTY,HOTEL_QTY
    global lancer,double1,double2,double3,terrain,propriete1,propriete2,propriete3,allpropriete,tentative1,tentative2,tentative3,PRIX_PRISON
    global prison_Joker1,prison_Joker2,prison_Joker3,DEPART,value_Terrain,double1_statut,double2_statut,double3_statut,impots_Terrain,player1_NB_Gare,player2_NB_Gare
    global player3_NB_Gare,version,value_Propriete1,value_Propriete2,value_Propriete3,player1_Faillite,player2_Faillite,player3_Faillite,MAX_JOUEUR,couleurs
    global marron_P1,marron_P2,marron_P3,rose_P1,rose_P2,rose_P3,violet_P1,violet_P2,violet_P3,orange_P1,orange_P2,orange_P3,rouge_P1,rouge_P2,rouge_P3,jaune_P1,jaune_P2,jaune_P3,vert_P1,vert_P2,vert_P3,bleu_P1,bleu_P2,bleu_P3
    global build_marron_P1,build_marron_P2,build_marron_P3,build_rose_P1,build_rose_P2,build_rose_P3,build_violet_P1,build_violet_P2,build_violet_P3,build_orange_P1,build_orange_P2,build_orange_P3,build_rouge_P1,build_rouge_P2,build_rouge_P3,build_jaune_P1,build_jaune_P2,build_jaune_P3,build_vert_P1,build_vert_P2,build_vert_P3,build_bleu_P1,build_bleu_P2,build_bleu_P3
    global maison_belleville,maison_lecourbe,maison_vaugirard,maison_courcelles,maison_republique,maison_vilette,maison_neuilly,maison_paradis,maison_mozart,maison_stmichel,maison_pigalle,maison_matignon,maison_malesherbes,maison_henri_martin,maison_sthonore,maison_bourse,maison_fayette,maison_breteuil,maison_foch,maison_capucines,maison_elysees,maison_paix,maison_marron,maison_rose,maison_violet,maison_orange,maison_rouge,maison_jaune,maison_vert,maison_bleu,hotel_belleville,hotel_lecourbe,hotel_vaugirard,hotel_courcelles,hotel_republique,hotel_vilette,hotel_neuilly,hotel_paradis,hotel_mozart,hotel_stmichel,hotel_pigalle,hotel_matignon,hotel_malesherbes,hotel_henri_martin,hotel_sthonore,hotel_bourse,hotel_fayette,hotel_breteuil,hotel_foch,hotel_capucines,hotel_elysees,hotel_paix


    version = "2.9.0"
    NB_player = 0
    MAX_JOUEUR = 3
    player1 = 'Noname'
    player2 = 'Noname'
    player3 = 'Noname'
    player1_Faillite = False
    player2_Faillite = False
    player3_Faillite = False
    GOLD = 150000           # MONTANT GOLD par défaut
    or1 = GOLD
    or2 = GOLD
    or3 = GOLD
    PRIX_PRISON = 5000
    ''' STATUT : INIT : Joueur en prison. '''
    player1_en_Prison = False
    player2_en_Prison = False
    player3_en_Prison = False
    #________________________________________
    ''' STATUT : INIT : joueur ne dispose pas de carte Joker pour la prison. '''
    prison_Joker1 = False
    prison_Joker2 = False
    prison_Joker3 = False
    #___________________________________________________________________________
    position1 = 0
    position2 = 0
    position3 = 0
    MAISON_QTY = 32         # Nombre de maisons pouvant être construite sur le plateau
    HOTEL_QTY = 12          # Nombre d'hotels pouvant être construit sur le plateau
    DEPART = 20000          # Montant attribué à chaque tour au Départ, *2 si on stationne dessus
    lancer = 0
    de1= 0
    de2 = 0
    double1 = 0
    double2 = 0
    double3 = 0
    double1_statut = False
    double2_statut = False
    double3_statut = False
    tentative1 = 3
    tentative2 = 3
    tentative3 = 3
    ''' Initialisation : les joueurs disposent d'aucune carte au début du jeu. '''
    propriete1 = ['Boulevard de Belleville','Rue Lecourbe','Compagnie d\'Electricité','Avenue de Neuilly','Rue du Paradis','Gare de Lyon','Avenue Mozart']
    propriete2 = []
    propriete3 = []
    #_____________________________________________________________________________
    value_Propriete1 = [1200,2000,3000,4000,6000,8000]
    value_Propriete2 = []
    value_Propriete3 = []
    #_____________________________________________________________________________
    allpropriete = ['Boulevard de Belleville','Rue Lecourbe','Compagnie d\'Electricité','Avenue de Neuilly','Rue du Paradis','Gare de Lyon','Avenue Mozart']       # Liste des propriétés déjà acquises par un joueur quelconque
    player1_NB_Gare = 0
    player2_NB_Gare = 0
    player3_NB_Gare = 0
    #_____________________________________________________________________________
    #_____________________________________________________________________________
    marron_P1 = 2
    marron_P2 = 0
    marron_P3 = 0
    rose_P1 = 0
    rose_P2 = 0
    rose_P3 = 0
    violet_P1 = 0
    violet_P2 = 0
    violet_P3 = 0
    orange_P1 = 0
    orange_P2 = 0
    orange_P3 = 0
    rouge_P1 = 0
    rouge_P2 = 0
    rouge_P3 = 0
    jaune_P1 = 0
    jaune_P2 = 0
    jaune_P3 = 0
    vert_P1 = 0
    vert_P2 = 0
    vert_P3 = 0
    bleu_P1 = 0
    bleu_P2 = 0
    bleu_P3 = 0

    #_____________________________________________________________________________
    #_____________________________________________________________________________

    build_marron_P1 = True
    build_marron_P2 = False
    build_marron_P3 = False
    build_rose_P1 = False
    build_rose_P2 = False
    build_rose_P3 = False
    build_violet_P1 = False
    build_violet_P2 = False
    build_violet_P3 = False
    build_orange_P1 = True
    build_orange_P2 = False
    build_orange_P3 = False
    build_rouge_P1 = False
    build_rouge_P2 = False
    build_rouge_P3 = False
    build_jaune_P1 = False
    build_jaune_P2 = False
    build_jaune_P3 = False
    build_vert_P1 = True
    build_vert_P2 = False
    build_vert_P3 = False
    build_bleu_P1 = True
    build_bleu_P2 = False
    build_bleu_P3 = False

    #_____________________________________________________________________________
    #_____________________________________________________________________________
    ''' Lorsque la variable maison_* est égale à 4, l'utilisateur construit un hotel '''
    maison_belleville = 0
    maison_lecourbe = 0
    maison_vaugirard = 0
    maison_courcelles = 0
    maison_republique = 0
    maison_vilette = 0
    maison_neuilly = 0
    maison_paradis = 0
    maison_mozart = 0
    maison_stmichel = 0
    maison_pigalle = 0
    maison_matignon = 0
    maison_malesherbes = 0
    maison_henri_martin = 0
    maison_sthonore = 0
    maison_bourse = 0
    maison_fayette = 0
    maison_breteuil = 0
    maison_foch = 0
    maison_capucines = 0
    maison_elysees = 0
    maison_paix = 0
    maison_marron = [maison_belleville,maison_lecourbe]
    maison_rose = [maison_vaugirard,maison_courcelles,maison_republique]
    maison_violet = [maison_vilette,maison_neuilly,maison_paradis]
    maison_orange = [maison_mozart,maison_stmichel,maison_pigalle]
    maison_rouge = [maison_matignon,maison_malesherbes,maison_henri_martin]
    maison_jaune = [maison_sthonore,maison_bourse,maison_fayette]
    maison_vert = [maison_breteuil,maison_foch,maison_capucines]
    maison_bleu = [maison_elysees,maison_paix]
    #_____________________________________________________________________________
    #_____________________________________________________________________________
    hotel_belleville = False
    hotel_lecourbe = False
    hotel_vaugirard = False
    hotel_courcelles = False
    hotel_republique = False
    hotel_vilette = False
    hotel_neuilly = False
    hotel_paradis = False
    hotel_mozart = False
    hotel_stmichel = False
    hotel_pigalle = False
    hotel_matignon = False
    hotel_malesherbes = False
    hotel_henri_martin = False
    hotel_sthonore = False
    hotel_bourse = False
    hotel_fayette = False
    hotel_breteuil = False
    hotel_foch = False
    hotel_capucines = False
    hotel_elysees = False
    hotel_paix = False

    #_____________________________________________________________________________
    #_____________________________________________________________________________
    impots_Terrain = [0,200,0,400,0,2500,600,0,600,800,0,1000,0,1000,1200,2500,1400,0,1400,1600,0,1800,0,1800,2000,2500,2200,2200,0,2400,0,2600,2600,0,2800,2500,0,3500,0,5000]
    value_Terrain = [0,6000,0,6000,0,20000,10000,0,10000,12000,0,14000,15000,14000,16000,20000,18000,0,18000,20000,0,22000,0,22000,24000,20000,26000,26000,15000,28000,0,30000,30000,0,32000,20000,0,35000,0,40000]
    # Ci-dessous : définition du plateau utilisé dans ce Monopoly  // Il est possible de changer les noms et les personnalisés du moment que l'ordre respect le plateau original.
    terrain = ['Départ','Boulevard de Belleville','Caisse de communauté','Rue Lecourbe','Impôt sur le revenu','Gare Montparnasse','Rue de Vaugirard','Chance','Rue de Courcelles','Avenue de la République','Prison','Boulevard de la Vilette','Compagnie d\'Electricité','Avenue de Neuilly','Rue du Paradis','Gare de Lyon','Avenue Mozart','Caisse de Communauté','Boulevard St Michel','Place Pigalle','Parc Gratuit','Avenue Matignon','Chance','Boulevard Malesherbes','Avenue Henri-Martin','Gare du Nord','Faubourg Saint-Honoré','Place de la Bourse','Compagnie des Eaux','Rue La Fayette','ALLEZ EN PRISON','Avenue de Breteuil','Avenue Foch','Caisse de communauté','Boulevard des Capucines','Gare Saint-Lazare','Chance','Champs-Elysées','Taxe de Luxe','Rue de la Paix']
    couleurs = ['None','Marron','None','Marron','None','None','Rose','None','Rose','Rose','None','Violet','None','Violet','Violet','None','Orange','None','Orange','Orange','None','Rouge','None','Rouge','Rouge','None','Jaune','Jaune','None','Jaune','None','Vert','Vert','None','Vert','None','None','Bleu','None','Bleu']



def replay():
    global rand,NB_player
    if rand==1:
        rand+=1
    elif rand==2:
        if NB_player==3:
            rand+=1
        else:
            rand=1
    elif rand==3:
        rand=1
    launch()

def check_Proprietes():
    global allpropriete
    terrain_Start = ['Boulevard de Belleville','Rue Lecourbe','Gare Montparnasse','Rue de Vaugirard','Rue de Courcelles','Avenue de la République','Boulevard de la Vilette','Compagnie d\'Electricité','Avenue de Neuilly','Rue du Paradis','Gare de Lyon','Avenue Mozart','Boulevard St Michel','Place Pigalle','Avenue Matignon','Boulevard Malesherbes','Avenue Henri-Martin','Gare du Nord','Faubourg Saint-Honoré','Place de la Bourse','Compagnie des Eaux','Rue La Fayette','Avenue de Breteuil','Avenue Foch','Boulevard des Capucines','Gare Saint-Lazare','Champs-Elysées','Rue de la Paix']
    calcul = list(set(terrain_Start)-set(allpropriete))
    for i in calcul:
        print("\t#\033[36m",i,"\033[0m")
    if len(calcul) > 0:
        print("\n\t\033[36mIl reste\033[32m",len(calcul),"propriétés\033[36m disponibles à l'achat.\033[0m")
    else:
        print("\n\t\033[31mIl ne reste aucune propriété disponible à l'achat.\033[0m")

def construction(player):
    global player1,player2,player3,position1,position2,position3,terrain,NB_player,allpropriete,player1_en_Prison,player2_en_Prison,player3_en_Prison
    global player1_NB_Gare,player2_NB_Gare,player3_NB_Gare,player1_Faillite,player2_Faillite,player3_Faillite,NB_player_alt,couleurs,MAISON_QTY,HOTEL_QTY
    global marron_P1,marron_P2,marron_P3,rose_P1,rose_P2,rose_P3,violet_P1,violet_P2,violet_P3,orange_P1,orange_P2,orange_P3,rouge_P1,rouge_P2,rouge_P3,jaune_P1,jaune_P2,jaune_P3,vert_P1,vert_P2,vert_P3,bleu_P1,bleu_P2,bleu_P3
    global build_marron_P1,build_marron_P2,build_marron_P3,build_rose_P1,build_rose_P2,build_rose_P3,build_violet_P1,build_violet_P2,build_violet_P3,build_orange_P1,build_orange_P2,build_orange_P3,build_rouge_P1,build_rouge_P2,build_rouge_P3,build_jaune_P1,build_jaune_P2,build_jaune_P3,build_vert_P1,build_vert_P2,build_vert_P3,build_bleu_P1,build_bleu_P2,build_bleu_P3
    global maison_belleville,maison_lecourbe,maison_vaugirard,maison_courcelles,maison_republique,maison_vilette,maison_neuilly,maison_paradis,maison_mozart,maison_stmichel,maison_pigalle,maison_matignon,maison_malesherbes,maison_henri_martin,maison_sthonore,maison_bourse,maison_fayette,maison_breteuil,maison_foch,maison_capucines,maison_elysees,maison_paix,maison_marron,maison_rose,maison_violet,maison_orange,maison_rouge,maison_jaune,maison_vert,maison_bleu,hotel_belleville,hotel_lecourbe,hotel_vaugirard,hotel_courcelles,hotel_republique,hotel_vilette,hotel_neuilly,hotel_paradis,hotel_mozart,hotel_stmichel,hotel_pigalle,hotel_matignon,hotel_malesherbes,hotel_henri_martin,hotel_sthonore,hotel_bourse,hotel_fayette,hotel_breteuil,hotel_foch,hotel_capucines,hotel_elysees,hotel_paix


    if player == 1:
        if not player1_Faillite:
            liste_Build = []
            liste_Maison = []
            if build_marron_P1:
                print("\033[32mVous pouvez construire sur les propriétés Marrons.\033[0m")
                liste_Build.append("Marron")
            if build_rose_P1:
                print("\033[32mVous pouvez construire sur les propriétés Roses.\033[0m")
                liste_Build.append("Rose")
            if build_violet_P1:
                print("\033[32mVous pouvez construire sur les propriétés Violettes.\033[0m")
                liste_Build.append("Violet")
            if build_orange_P1:
                print("\033[32mVous pouvez construire sur les propriétés Oranges.\033[0m")
                liste_Build.append("Orange")
            if build_rouge_P1:
                print("\033[32mVous pouvez construire sur les propriétés Rouges.\033[0m")
                liste_Build.append("Rouge")
            if build_jaune_P1:
                print("\033[32mVous pouvez construire sur les propriétés Jaunes .\033[0m")
                liste_Build.append("Jaune")
            if build_vert_P1:
                print("\033[32mVous pouvez construire sur les propriétés Vertes .\033[0m")
                liste_Build.append("Vert")
            if build_bleu_P1:
                print("\033[32mVous pouvez construire sur les propriétés Bleues.\033[0m")
                liste_Build.append("Bleu")
            build_Select = ''
            build_Check = 0
            build_Continue = True
            while build_Continue != False:
                cpt = 1
                cpt_Liste = []
                property_Liste = []
                posTemp = 0
                print("\n\nVous souhaitez construire des Maisons dans vos propriétés, bienvenue dans le menu construction Monopoly !")
                print("Regardez auparavant que vous possédez bien des 'familles' de même couleurs complètes. (cf. ci-dessus en vert)")
                print("\n\t>> Il reste",MAISON_QTY,"maisons disponibles à la construction.")
                print("\n\t>> Il reste",HOTEL_QTY,"hôtels disponibles à la construction.")
                print("\n")
                print("Vos choix :")
                print(liste_Build)
                while build_Select not in liste_Build:
                    build_Select = input("Votre choix (écrire le nom de couleur exactement comme dans la liste citée ci-dessus) : ")
                    if build_Select not in liste_Build:
                        print("Attention : veuillez écrire correctement la couleur (Majuscule comprise)")
                if build_Select in liste_Build:
                    print("Vous avez choisi de construire sur une propriété de couleur",build_Select)
                    print("Voici une liste des propriétés de cette famille de couleur :")

                    for i in couleurs:
                        if i == build_Select:
                            print(cpt,">>",terrain[posTemp])
                            property_Liste.append(terrain[posTemp])
                            cpt_Liste.append(cpt)
                            cpt += 1
                        posTemp += 1
                    #print(property_Liste)
                    print("Voici les propriétés de cette famille, vous allez maintenant construire sur chacune d'entre elle.")
                    '''
                    while build_Check not in cpt_Liste:
                        build_Check = int(input("Entrer la valeur de la carte où vous souhaitez construire une Maison : "))
                        if build_Check not in cpt_Liste:
                            print("Attention : cette entrée est incorrecte ! Veuillez insérer le numéro devant la propriété listée ci-dessus !")
                    if build_Check in cpt_Liste:
                        print("Vous avez sélectionné la carte :",property_Liste[build_Check-1])
                        # TEST IMPORTANT MAISON UNIFORMEMENT REPARTIE A FAIRE !
                        print("Vous avez construit une maison sur cette propriété ! Félicitation.")
                        MAISON_QTY -= 1
                        print("Il reste",MAISON_QTY,"maisons disponibles.")
                    '''
                    if build_Select == "Marron":
                        maison_belleville += 1
                        maison_lecourbe += 1

                build_Select = ''
                build_Check = 0
                choix_Continuer = ''
                while choix_Continuer != 'oui' and choix_Continuer != 'non':
                    choix_Continuer = input("\n\nVoulez-vous arrêter de construire ? 'oui' ou 'non' : ")
                    if choix_Continuer == 'oui':
                        build_Continue = False
                    else:
                        build_Continue = True
        else:
            print(player1,"vous êtes en faillite, impossible de construire.")
'''
        cpt = 0
        posTemp = 0
        for i in couleurs:
            if i == "Marron":
                cpt += 1
                print(cpt,">>",terrain[posTemp])
            posTemp += 1
'''

def constat():
    global player1,player2,player3,double1,double2,double3,position1,position2,position3,terrain,NB_player,allpropriete,player1_en_Prison,player2_en_Prison,player3_en_Prison
    global player1_NB_Gare,player2_NB_Gare,player3_NB_Gare,player1_Faillite,player2_Faillite,player3_Faillite,NB_player_alt,rand
    if not player1_Faillite:
        print("\033[36m")
        print(player1,'\033[0mse trouve à\033[33m',terrain[position1],'\033[0met possède :\n',propriete1,"\nIl dispose de ",or1,"pièces d'or.")
        if player1_NB_Gare > 0:
            print("\033[32mLe joueur possède,",player1_NB_Gare,"gare(s).\033[0m")
        if player1_en_Prison:
            print("\033[31mLe joueur est en prison !\033[0m")
    else:
        print("\033[36m",player1,"\033[35ma fait faillite.\033[0m")
    print("______________________________________________________________________________")
    if not player2_Faillite:
        print("\033[36m")
        print(player2,'\033[0mse trouve à\033[33m',terrain[position2],'\033[0met possède :\n',propriete2,"\nIl dispose de ",or2,"pièces d'or.")
        if player2_NB_Gare > 0:
            print("\033[32mLe joueur possède,",player2_NB_Gare,"gare(s).\033[0m")
        if player2_en_Prison:
            print("\033[31mLe joueur est en prison !\033[0m")
    else:
        print("\033[36m",player2,"\033[35ma fait faillite.\033[0m")
    if NB_player==3:
        print("______________________________________________________________________________")
        if not player3_Faillite:
            print("\033[36m")
            print(player3,'\033[0mse trouve à\033[33m',terrain[position3],'\033[0met possède :\n',propriete3,"\nIl dispose de ",or3,"pièces d'or.")
            if player3_NB_Gare > 0:
                print("\033[32mLe joueur possède,",player3_NB_Gare,"gare(s).\033[0m")
            if player3_en_Prison:
                print("\033[31mLe joueur est en prison !\033[0m")
        else:
            print("\033[36m",player3,"\033[35ma fait faillite.\033[0m")
    print("______________________________________________________________________________")
    print("\nPropriétés déjà acquises :\n",allpropriete)

    if NB_player_alt == 1:
        winner = ''
        if not player1_Faillite:
            winner = player1
            print("\033[32mFélicitation\033[36m",player1,"\033[0m!\n\033[32mVous avez remporté la partie et êtes devenu le nouveau \033[33mPicsou\033[0m \033[32m!\033[0m")
        elif not player2_Faillite:
            winner = player2
            print("\033[32mFélicitation\033[36m",player2,"\033[0m!\n\033[32mVous avez remporté la partie et êtes devenu le nouveau \033[33mPicsou\033[0m \033[32m!\033[0m")
        elif not player1_Faillite:
            winner = player3
            print("\033[32mFélicitation\033[36m",player3,"\033[0m!\n\033[32mVous avez remporté la partie et êtes devenu le nouveau \033[33mPicsou\033[0m \033[32m!\033[0m")
        menu = ''
        while menu != 'T':
            print("La partie est terminée !")
            print(winner,"a remporté la partie et est l'actuel Picsou !")
            print("\nQue voulez-vous faire à présent ? Rejouer une partie ?")
            print("\t0. Récapitulatif des règles")
            print("\t1. Montrer le constat final")
            print("\t2. Combien de propriétés restées t-il en jeu ?")
            print("\t3. Crédits (développeurs du jeu)")
            print("\t4. Rejouer une partie !")
            print("\tT. Quitter le jeu")
            menu = input("\n\n\033[35mSélectionner l'action à effectuer : \033[0m")
            if menu == '0':
                game_Rules()
            elif menu == '1':
                constat()
            elif menu == '2':
                check_Proprietes()
            elif menu == '3':
                print("\033[32mCe Monopoly a été programmé par \033[36mValentin MICHEL\033[32m,\nEtudiant de DUT Informatique.")
                print("\033[31mDéveloppeurs :\033[36m\nValentin MICHEL\033[0m")
                print("\033[31mDesigner :\033[36m\nListe incomplète\033[0m")
                print("\033[31mContributeurs :\033[36m\nFabien GENOUD\033[0m")
            elif menu == '4':
                play()
            elif menu == 'T':
                print("Vous allez quitter le jeu.")
                print("Fermeture du processus ...")
                time.sleep(3)
                print("A bientôt !")
                sys.exit(0)
            else:
                print("Entrée incorrecte : veuillez sélectionner le caractère présent devant le titre de chaque sélection du menu.")


    '''
    TEST TEMPORAIRE

    pos = 0
    pos += position1
    print("Position joueur 1 : ",pos)
    '''
    ''' # ANCIEN MENU-PAUSE STEP BY STEP
    try:
        input("\033[35mAppuyer sur une touche quelconque pour passer au tour suivant ...\033[0m\n")
    except SyntaxError:
        pass
    replay()
    '''
    menu = ''
    currentPlayer = ''
    if rand == 1:
        currentPlayer = player1
    elif rand == 2:
        currentPlayer = player2
    elif rand == 3:
        currentPlayer = player3

    while menu != 'T':
        print("\033[32m\n\n\tMENU DU MONOPOLY\033[0m")
        print("0. Règles du jeu")
        print("1. Passer au tour suivant")
        print("2. Informations sur les joueurs présents dans la partie")
        print("3. Faire abandonner un joueur")
        print("4. Afficher les propriétés encore disponible à l'achat")
        print("5. Construire")
        print("T. Quitter la partie")
        print("\nJoueur actuel :\033[36m",currentPlayer,"\033[0m")
        menu = input("\n\n\033[35mSélectionner l'action à effectuer : \033[0m")
        if menu == '0':
            game_Rules()
        elif menu == '1':
            replay()
        elif menu == '2':
            constat()
        elif menu == '3':
            selection = 0
            if NB_player_alt > 1:
                if not player1_Faillite:
                    print("\033[36mJoueur 1 :",player1)
                if not player2_Faillite:
                    print("Joueur 2 :",player2)
                if NB_player == 3:
                    if not player3_Faillite:
                        print("Joueur 3 :",player3,"\033[0m")
                while selection != 1 and selection != 2 and selection != 3:
                    selection = int(input("Choisir le joueur qui doit être éliminé de la partie : "))
                if selection == 1:
                    player1_Faillite = True
                    NB_player_alt -= 1
                elif selection == 2:
                    player2_Faillite = True
                    NB_player_alt -= 1
                elif selection == 3:
                    player3_Faillite = True
                    NB_player_alt -= 1
                print("Vous avez retiré le joueur n°",selection)
                constat()
            else:
                print("Il ne reste qu'un seul joueur, vous ne pouvez pas abandonner : vous avez gagné la partie.")
        elif menu == '4':
            check_Proprietes()
        elif menu == '5':
            construction(rand)
        elif menu == 'T':
            print("Vous allez quitter le jeu.")
            print("Fermeture du processus ...")
            time.sleep(3)
            print("A bientôt !")
            sys.exit(0)
        else:
            print("Entrée incorrecte : veuillez sélectionner le caractère présent devant le titre de chaque sélection du menu.")


#def transfert():  A CODER pour les transferts (échange de carte / monétaire)

def check_Faillite():
    global or1,or2,or3,player1,player2,player3,rand,value_Propriete1,value_Propriete2,value_Propriete3,propriete1,propriete2,propriete3,NB_player_alt,player1_Faillite,player2_Faillite,player3_Faillite
    if not player1_Faillite:
        if rand == 1:
            if or1 < 0:
                print("\033[31mVous êtes dans le rouge !\033[0m")
                print("Vous êtes à",or1,"pièces d'or de dettes !")
                if len(propriete1) > 0:
                    total = 0
                    for i in value_Propriete1:
                        total += i
                    print("\033[33mValeur total d'hypothèque :",total/2,"pièces d'or.\033[0m")
                    if total/2 >= abs(or1):
                        print("\033[33mVous pouvez hypothéquer vos propriétés pour une valeur de moitié leur prix d'achat.\033[0m\nVoici une liste ordonnée :")
                        compt = 0
                        stock = []
                        for i in propriete1:
                            stock.append(compt)
                            print(compt,"=",i,"\t(",value_Propriete1[compt]/2,"pièces d'or)")
                            compt += 1
                        id_Prop = -1
                        while id_Prop not in stock:
                            id_Prop = int(input("Veuillez sélectionner l'\033[33midentifiant d'une carte pour l'hypothéquer\033[0m : "))
                        print("Vous avez hypothéqué\033[33m",propriete1[id_Prop],"\033[0m")
                        gain = value_Propriete1[id_Prop] / 2
                        del propriete1[id_Prop]
                        del value_Propriete1[id_Prop]
                        or1 += gain
                        print("Vous avez reçu",gain,"pièces d'or.")
                        check_Faillite()
                    else:
                        print("\033[36m")
                        print(player1,"\033[31mVOUS ÊTES EN FAILLITE !\033[0m\nVous avez été \033[31méliminé de la partie\033[0m.")
                        NB_player_alt -= 1
                        player1_Faillite = True
                #Faire des elif avec les maisons et hotel également, et un menu sélectionnant si le joueur souhaite d'abord revendre des maisons ou hypothéqué.
                else:
                    print("\033[36m")
                    print(player1,"\033[31mVOUS ÊTES EN FAILLITE !\033[0m\nVous avez été \033[31méliminé de la partie\033[0m.")
                    NB_player_alt -= 1
                    player1_Faillite = True
    if not player2_Faillite:
        if rand == 2:
            if or2 < 0:
                print("\033[31mVous êtes dans le rouge !\033[0m")
                print("Vous êtes à",or2,"pièces d'or de dettes !")
                if len(propriete2) > 0:
                    total = 0
                    for i in value_Propriete2:
                        total += i
                    print("\033[33mValeur total d'hypothèque :",total/2,"pièces d'or.\033[0m")
                    if total/2 >= abs(or2):
                        print("\033[33mVous pouvez hypothéquer vos propriétés pour une valeur de moitié leur prix d'achat.\033[0m\nVoici une liste ordonnée :")
                        compt = 0
                        stock = []
                        for i in propriete1:
                            stock.append(compt)
                            print(compt,"=",i,"\t(",value_Propriete2[compt]/2,"pièces d'or)")
                            compt += 1
                        id_Prop = -1
                        while id_Prop not in stock:
                            id_Prop = int(input("Veuillez sélectionner l'\033[33midentifiant d'une carte pour l'hypothéquer\033[0m : "))
                        print("Vous avez hypothéqué\033[33m",propriete2[id_Prop],"\033[0m")
                        gain = value_Propriete2[id_Prop] / 2
                        del propriete2[id_Prop]
                        del value_Propriete2[id_Prop]
                        or2 += gain
                        print("Vous avez reçu",gain,"pièces d'or.")
                        check_Faillite()
                    else:
                        print("\033[36m")
                        print(player1,"\033[31mVOUS ÊTES EN FAILLITE !\033[0m\nVous avez été \033[31méliminé de la partie\033[0m.")
                        NB_player_alt -= 1
                        player2_Faillite = True
                #Faire des elif avec les maisons et hotel également, et un menu sélectionnant si le joueur souhaite d'abord revendre des maisons ou hypothéqué.
                else:
                    print("\033[36m")
                    print(player2,"\033[31mVOUS ÊTES EN FAILLITE !\033[0m\nVous avez été \033[31méliminé de la partie\033[0m.")
                    NB_player_alt -= 1
                    player2_Faillite = True

    if not player3_Faillite:
        if rand == 3:
            if or3 < 0:
                print("\033[31mVous êtes dans le rouge !\033[0m")
                print("Vous êtes à",or3,"pièces d'or de dettes !")
                if len(propriete3) > 0:
                    total = 0
                    for i in value_Propriete3:
                        total += i
                    print("\033[33mValeur total d'hypothèque :",total/2,"pièces d'or.\033[0m")
                    if total/2 >= abs(or3):
                        print("\033[33mVous pouvez hypothéquer vos propriétés pour une valeur de moitié leur prix d'achat.\033[0m\nVoici une liste ordonnée :")
                        compt = 0
                        stock = []
                        for i in propriete3:
                            stock.append(compt)
                            print(compt,"=",i,"\t(",value_Propriete3[compt]/2,"pièces d'or)")
                            compt += 1
                        id_Prop = -1
                        while id_Prop not in stock:
                            id_Prop = int(input("Veuillez sélectionner l'\033[33midentifiant d'une carte pour l'hypothéquer\033[0m : "))
                        print("Vous avez hypothéqué\033[33m",propriete3[id_Prop],"\033[0m")
                        gain = value_Propriete3[id_Prop] / 2
                        del propriete3[id_Prop]
                        del value_Propriete3[id_Prop]
                        or3 += gain
                        print("Vous avez reçu",gain,"pièces d'or.")
                        check_Faillite()
                    else:
                        print("\033[36m")
                        print(player3,"\033[31mVOUS ÊTES EN FAILLITE !\033[0m\nVous avez été \033[31méliminé de la partie\033[0m.")
                        NB_player_alt -= 1
                        player3_Faillite = True
                #Faire des elif avec les maisons et hotel également, et un menu sélectionnant si le joueur souhaite d'abord revendre des maisons ou hypothéqué.
                else:
                    print("\033[36m")
                    print(player3,"\033[31mVOUS ÊTES EN FAILLITE !\033[0m\nVous avez été \033[31méliminé de la partie\033[0m.")
                    NB_player_alt -= 1
                    player3_Faillite = True

def encheres(position,prix_Init):
    global or1,or2,or3,player1,player2,player3,rand,value_Propriete1,value_Propriete2,value_Propriete3,propriete1,propriete2,propriete3,NB_player_alt
    global player1_Faillite,player2_Faillite,player3_Faillite,terrain,GOLD
    propositions = [-1,-1,-1]
    tour = 0
    print("\n\n\nBienvenue aux enchères !\n")
    print("Les enchères concernent la propriété",terrain[position],"ayant pour valeur marchande initiale",prix_Init,"pièces d'or.")
    print("Tous les joueurs devront proposés une valeur monétaire minimum d'une pièce d'or pour participer aux enchères.")
    print("Vous disposez de 6 tours de propositions. Au bout du 6ème tour, le joueur ayant proposé la meilleur valeur monétaire remporte les enchères et la propriété !")
    print("Si vous souhaitez vous retirer des enchères, entrer une valeur nulle de 0 pièce d'or pour être retiré !")
    while tour != 6:
        tour += 1
        if propositions[0] != 0:
            proposition = GOLD + 1
            if or1 >= 0:
                print(player1,": Veuillez insérer une valeur d'achat pour la propriété suivante :",terrain[position])
                while proposition > or1:
                    proposition = int(input("Votre proposition : "))
                    if proposition > or1:
                        print("Votre proposition excède vos moyens financiers ! Vous disposez de",or1,"pièces d'or.")
                propositions[0] = proposition
                print("\n\n")
        if propositions[1] != 0:
            proposition = GOLD + 1
            if or2 >= 0:
                print(player2,": Veuillez insérer une valeur d'achat pour la propriété suivante :",terrain[position])
                while proposition > or2:
                    proposition = int(input("Votre proposition : "))
                    if proposition > or2:
                        print("Votre proposition excède vos moyens financiers ! Vous disposez de",or2,"pièces d'or.")
                propositions[1] = proposition
                print("\n\n")
        if propositions[2] != 0:
            proposition = GOLD + 1
            if or3 >= 0:
                print(player3,": Veuillez insérer une valeur d'achat pour la propriété suivante :",terrain[position])
                while proposition > or3:
                    proposition = int(input("Votre proposition : "))
                    if proposition > or3:
                        print("Votre proposition excède vos moyens financiers ! Vous disposez de",or3,"pièces d'or.")
                propositions[2] = proposition
        print("\n\n\n\n\n\n\n\n\n\nRécapitulatif de vos propositions :")
        print(player1,"a proposé",propositions[0],"pièces d'or.")
        print(player2,"a proposé",propositions[1],"pièces d'or.")
        print(player3,"a proposé",propositions[2],"pièces d'or.")
        MAX = max(propositions)
        compt = 0
        for i in propositions:
            if i == MAX:
                if compt == 0:
                    plus_Offrant = player1
                elif compt == 1:
                    plus_Offrant = player2
                elif compt == 2:
                    plus_Offrant = player3
            compt+=1
        if tour != 6:
            print("\n\nPour le moment,",plus_Offrant,"est celui qui a proposé la meilleure offre. Montant proposé :",MAX,"pièces d'or.")
    print(plus_Offrant,"a remporté les enchères pour un montant de",MAX,"pièces d'or.")



def market(position):
    price_Property = value_Terrain[position]
    return price_Property

def check_Couleurs(position):
    global couleurs
    couleurPropriete = couleurs[position]
    return couleurPropriete

def nb_Couleur(couleur,player):
    global marron_P1,marron_P2,marron_P3,rose_P1,rose_P2,rose_P3,violet_P1,violet_P2,violet_P3,orange_P1,orange_P2,orange_P3,rouge_P1,rouge_P2,rouge_P3,jaune_P1,jaune_P2,jaune_P3,vert_P1,vert_P2,vert_P3,bleu_P1,bleu_P2,bleu_P3
    global build_marron_P1,build_marron_P2,build_marron_P3,build_rose_P1,build_rose_P2,build_rose_P3,build_violet_P1,build_violet_P2,build_violet_P3,build_orange_P1,build_orange_P2,build_orange_P3,build_rouge_P1,build_rouge_P2,build_rouge_P3,build_jaune_P1,build_jaune_P2,build_jaune_P3,build_vert_P1,build_vert_P2,build_vert_P3,build_bleu_P1,build_bleu_P2,build_bleu_P3
    if player == 1:
        if couleur == 'Marron':
            marron_P1 += 1
            if marron_P1 == 2:
                build_marron_P1 = True
        elif couleur == 'Rose':
            rose_P1 += 1
            if rose_P1 == 3:
                build_rose_P1 = True
        elif couleur == 'Violet':
            violet_P1 += 1
            if violet_P1 == 3:
                build_violet_P1 = True
        elif couleur == 'Orange':
            orange_P1 += 1
            if orange_P1 == 3:
                build_orange_P1 = True
        elif couleur == 'Rouge':
            rouge_P1 +1
            if rouge_P1 == 3:
                build_rouge_P1 = True
        elif couleur == 'Jaune':
            jaune_P1 += 1
            if jaune_P1 == 3:
                build_jaune_P1 = True
        elif couleur == 'Vert':
            vert_P1 += 1
            if vert_P1 == 3:
                build_vert_P1 = True
        elif couleur == 'Bleu':
            bleu_P1 += 1
            if bleu_P1 == 2:
                build_bleu_P1 = True
    if player == 2:
        if couleur == 'Marron':
            marron_P2 += 1
            if marron_P2 == 2:
                build_marron_P2 = True
        elif couleur == 'Rose':
            rose_P2 += 1
            if rose_P2 == 3:
                build_rose_P2 = True
        elif couleur == 'Violet':
            violet_P2 += 1
            if violet_P2 == 3:
                build_violet_P2 = True
        elif couleur == 'Orange':
            orange_P2 += 1
            if orange_P2 == 3:
                build_orange_P2 = True
        elif couleur == 'Rouge':
            rouge_P2 +1
            if rouge_P2 == 3:
                build_rouge_P2 = True
        elif couleur == 'Jaune':
            jaune_P2 += 1
            if jaune_P2 == 3:
                build_jaune_P2 = True
        elif couleur == 'Vert':
            vert_P2 += 1
            if vert_P2 == 3:
                build_vert_P2 = True
        elif couleur == 'Bleu':
            bleu_P2 += 1
            if bleu_P2 == 2:
                build_bleu_P2 = True
    if player == 3:
        if couleur == 'Marron':
            marron_P3 += 1
            if marron_P3 == 2:
                build_marron_P3 = True
        elif couleur == 'Rose':
            rose_P3 += 1
            if rose_P3 == 3:
                build_rose_P3 = True
        elif couleur == 'Violet':
            violet_P3 += 1
            if violet_P3 == 3:
                build_violet_P3 = True
        elif couleur == 'Orange':
            orange_P3 += 1
            if orange_P3 == 3:
                build_orange_P3 = True
        elif couleur == 'Rouge':
            rouge_P3 +1
            if rouge_P3 == 3:
                build_rouge_P3 = True
        elif couleur == 'Jaune':
            jaune_P3 += 1
            if jaune_P3 == 3:
                build_jaune_P3 = True
        elif couleur == 'Vert':
            vert_P3 += 1
            if vert_P3 == 3:
                build_vert_P3 = True
        elif couleur == 'Bleu':
            bleu_P3 += 1
            if bleu_P3 == 2:
                build_bleu_P3 = True

def etat_double(etat,rand):
    global player1,player2,player3
    if etat:
        if rand == 1:
            try:
                print("\033[33m",player1,"\033[0m: Vous avez réalisé un double !")
                input("Vous allez pouvoir relancer les dés !")
            except SyntaxError:
                pass
            joueur1()
        elif rand == 2:
            try:
                print("\033[33m",player2,"\033[0m: Vous avez réalisé un double !")
                input("Vous allez pouvoir relancer les dés !")
            except SyntaxError:
                pass
            joueur2()
        elif rand == 3:
            try:
                print("\033[33m",player3,"\033[0m: Vous avez réalisé un double !")
                input("Vous allez pouvoir relancer les dés !")
            except SyntaxError:
                pass
            joueur3()


def propriete_Joueur1():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete,value_Propriete1
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,or1,or2,or3,double1_statut,impots_Terrain,player1_NB_Gare,player2_NB_Gare,player3_NB_Gare,couleurs
    if terrain[position1] not in allpropriete:
        choix = ''
        prix = market(position1)
        couleur = check_Couleurs(position1)
        print("\033[33mCouleur de la carte :\033[36m",couleur,"\033[0m")
        print("\033[31mRappel\033[0m : vous possédez",or1,"pièces d'or.")
        print("Cette propriété est \033[32mlibre\033[0m, voulez vous l'acheté pour un montant de\033[33m",prix,"\033[0mpièces d'or ? ( 'oui' ou 'non' )")
        choix = input("Réponse : \033[36m")
        print("\033[0m")
        if choix == 'oui':
            if prix > or1:
                print("\033[31mVous ne possédez pas d'assez d'argent pour acquérir cette propriété.\033[0m")
                #Mettre en place l'hypothéque de carte et/ou revente Maison/Hotel et/ou proposé de vendre une carte à un joueur et/ou proposé la propriété aux enchères.
            elif prix == or1:
                choix = ''
                choix = input("\033[33mAttention, si vous achetez cette propriété vous n'aurez plus d'argent pour le prochain tour !\033[0m Voulez-vous continuer ? ('oui' ou 'non')\nRéponse : \033[36m")
                print("\033[0m")
                if choix == 'oui':
                    or1 -= prix
                    propriete1.append(terrain[position1])
                    allpropriete.append(terrain[position1])
                    value_Propriete1.append(prix)
                    #print("Le prix de vos propriétés dans l'ordre :\n",value_Propriete1)
                    if (position1 == 5) or (position1 == 15) or (position1 == 25) or (position1 == 35):
                        player1_NB_Gare += 1
                    nb_Couleur(couleur,rand)
                    print("\033[36mVous avez acheté la propriété\033[33m",terrain[position1],"\033[0mpour un montant de\033[33m",prix,"pièces d'or\033[0m !\nElle a été ajoutée à vos possessions actuelles.\n")
                    print("RAPPEL :\nVos possessions actuelles :\n",propriete1,"\n")
                    print("Vous n'avez plus d'argent actuellement pour le prochain tour.")
                else:
                    print("Vous avez abandonné l'achat de cette propriété.")
            else:
                or1 -= prix
                propriete1.append(terrain[position1])
                allpropriete.append(terrain[position1])
                value_Propriete1.append(prix)
                #print("Le prix de vos propriétés dans l'ordre :\n",value_Propriete1)
                if (position1 == 5) or (position1 == 15) or (position1 == 25) or (position1 == 35):
                    player1_NB_Gare += 1
                nb_Couleur(couleur,rand)
                print("\033[36mVous avez acheté la propriété\033[33m",terrain[position1],"\033[0mpour un montant de\033[33m",prix,"pièces d'or\033[0m !\nElle a été ajoutée à vos possessions actuelles.\n")
                print("RAPPEL :\nVos possessions actuelles :\n",propriete1,"\n")
        else:
            #print("Oh dommage !")
            encheres(position1,prix)
    elif terrain[position1] in propriete1:
        print("\033[36mVous possédez déjà cette carte.\033[0m")

    elif terrain[position1] in propriete2:
        print("\033[36m")
        print(player2,'\033[0mpossède cette carte, \033[31mvous devez lui payer un impôt\033[0m')
        if (position1 == 12) or (position1 == 28):
            if (terrain[12] in propriete2) and (terrain[28] in propriete2):
                print("\033[31mVous êtes sur une propriété de Service Public !\nLe propriétaire de cette propriété possède également l'autre propriété de Service Public.\033[0m")
                print("\t=> De ce fait, vous devez \033[33mpayer 1000 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 1000 * lancer
                or1 -= montant_Service
                or2 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or1,"pièces d'or.")
            elif (terrain[12] in propriete2) or (terrain[28] in propriete2):
                print("\033[31mVous êtes sur une propriété de Service Public\033[0m, vous devez \033[33mpayer 400 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 400 * lancer
                or1 -= montant_Service
                or2 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or1,"pièces d'or.")
        elif (position1 == 5) or (position1 == 15) or (position1 == 25) or (position1 == 35):
            print("Vous êtes arrivé à la\033[33m",terrain[position1],"\033[0m: vous devez payer l'impôt de cette propriété à\033[36m",player2,"\033[0msachant qu'il \033[33mpossède actuellement",player2_NB_Gare,"gare(s)\033[0m.")
            if player2_NB_Gare < 3:
                impot_Gare = player2_NB_Gare * impots_Terrain[position1]
            elif player2_NB_Gare == 3:
                impot_Gare = player2_NB_Gare * impots_Terrain[position1] + impots_Terrain[position1]
            else:
                impot_Gare = (2 * player2_NB_Gare) * impots_Terrain[position1]
            or1 -= impot_Gare
            or2 += impot_Gare
            print("Vous devez payer un montant de\033[33m",impot_Gare,"pièces d'or\033[0m.\nIl vous reste\033[33m",or1,"pièces d'or.\033[36m")
            print(player2,"\033[0ma désormais\033[0m",or2,"pièces d'or.\033[0m")
        else:
            print("Vous êtes sur la propriété\033[33m",terrain[position1],"\033[0mqui appartient à\033[36m",player2,"!\033[0m")
            print("\033[31mVous devez lui payer les impôts liés à cette propriété.\033[0m")
            impots = impots_Terrain[position1]
            or1 -= impots
            or2 += impots
            print("\033[31mMontant des impôts\033[0m :",impots,"pièces d'or.\nIl vous reste",or1,"pièces d'or.")

    else:
        print("\033[36m")
        print(player3,'\033[0mpossède cette carte, \033[31mvous devez lui payer un impôt\033[0m')
        if (position1 == 12) or (position1 == 28):
            if (terrain[12] in propriete3) and (terrain[28] in propriete3):
                print("\033[31mVous êtes sur une propriété de Service Public !\nLe propriétaire de cette propriété possède également l'autre propriété de Service Public.\033[0m")
                print("\t=> De ce fait, vous devez \033[33mpayer 1000 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 1000 * lancer
                or1 -= montant_Service
                or3 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or1,"pièces d'or.")
            elif (terrain[12] in propriete3) or (terrain[28] in propriete3):
                print("\033[31mVous êtes sur une propriété de Service Public\033[0m, vous devez \033[33mpayer 400 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 400 * lancer
                or1 -= montant_Service
                or3 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or1,"pièces d'or.")
        elif (position1 == 5) or (position1 == 15) or (position1 == 25) or (position1 == 35):
            print("Vous êtes arrivé à la\033[33m",terrain[position1],"\033[0m: vous devez payer l'impôt de cette propriété à\033[36m",player3,"\033[0msachant qu'il \033[33mpossède actuellement",player3_NB_Gare,"gare(s)\033[0m.")
            if player3_NB_Gare < 3:
                impot_Gare = player3_NB_Gare * impots_Terrain[position1]
            elif player2_NB_Gare == 3:
                impot_Gare = player3_NB_Gare * impots_Terrain[position1] + impots_Terrain[position1]
            else:
                impot_Gare = (2 * player3_NB_Gare) * impots_Terrain[position1]
            or1 -= impot_Gare
            or3 += impot_Gare
            print("Vous devez payer un montant de\033[33m",impot_Gare,"pièces d'or\033[0m.\nIl vous reste\033[33m",or1,"pièces d'or.\033[36m")
            print(player3,"\033[0ma désormais\033[0m",or3,"pièces d'or.\033[0m")
        else:
            print("Vous êtes sur la propriété\033[33m",terrain[position1],"\033[0mqui appartient à\033[36m",player3,"!\033[0m")
            print("\033[31mVous devez lui payer les impôts liés à cette propriété.\033[0m")
            impots = impots_Terrain[position1]
            or1 -= impots
            or3 += impots
            print("\033[31mMontant des impôts\033[0m :",impots,"pièces d'or.\nIl vous reste",or1,"pièces d'or.")
    etat_double(double1_statut,rand)


def propriete_Joueur2():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,or1,or2,or3,double2_statut,impots_Terrain,player2_NB_Gare,value_Propriete2
    if terrain[position2] not in allpropriete:
        choix = ''
        prix = market(position2)
        couleur = check_Couleurs(position2)
        print("\033[33mCouleur de la carte :\033[36m",couleur,"\033[0m")
        print("\033[31mRappel\033[0m : vous possédez",or2,"pièces d'or.")
        print("Cette propriété est \033[32mlibre\033[0m, voulez vous l'acheté pour un montant de\033[33m",prix,"\033[0mpièces d'or ? ( 'oui' ou 'non' )")
        choix = input("Réponse : \033[36m")
        print("\033[0m")
        if choix == 'oui':
            if prix > or2:
                print("\033[31mVous ne possédez pas d'assez d'argent pour acquérir cette propriété.\033[0m")
                #Mettre en place l'hypothéque de carte et/ou revente Maison/Hotel et/ou proposé de vendre une carte à un joueur et/ou proposé la propriété aux enchères.
            elif prix == or2:
                choix = ''
                choix = input("\033[33mAttention, si vous achetez cette propriété vous n'aurez plus d'argent pour le prochain tour !\033[0m Voulez-vous continuer ? ('oui' ou 'non')\nRéponse : \033[36m")
                print("\033[0m")
                if choix == 'oui':
                    or2 -= prix
                    propriete2.append(terrain[position2])
                    allpropriete.append(terrain[position2])
                    if (position2 == 5) or (position2 == 15) or (position2 == 25) or (position2 == 35):
                        player2_NB_Gare += 1
                    nb_Couleur(couleur,rand)
                    print("\033[36mVous avez acheté la propriété\033[33m",terrain[position2],"\033[0mpour un montant de\033[33m",prix,"pièces d'or\033[0m !\nElle a été ajoutée à vos possessions actuelles.\n")
                    print("RAPPEL :\nVos possessions actuelles :\n",propriete2,"\n")
                    print("Vous n'avez plus d'argent actuellement pour le prochain tour.")
                else:
                    print("Vous avez abandonné l'achat de cette propriété.")
            else:
                or2 -= prix
                propriete2.append(terrain[position2])
                allpropriete.append(terrain[position2])
                if (position2 == 5) or (position2 == 15) or (position2 == 25) or (position2 == 35):
                    player2_NB_Gare += 1
                nb_Couleur(couleur,rand)
                print("\033[36mVous avez acheté la propriété\033[33m",terrain[position2],"\033[0mpour un montant de\033[33m",prix,"pièces d'or\033[0m !\nElle a été ajoutée à vos possessions actuelles.\n")
                print("RAPPEL :\nVos possessions actuelles :\n",propriete2,"\n")
        else:
            #print("Oh dommage !")
            encheres(position2,prix)
    elif terrain[position2] in propriete2:
        print("\033[36mVous possédez déjà cette carte.\033[0m")
    elif terrain[position2] in propriete1:
        print("\033[36m")
        print(player1,'\033[0mpossède cette carte, \033[31mvous devez lui payer un impôt\033[0m')
        if (position2 == 12) or (position2 == 28):
            if (terrain[12] in propriete1) and (terrain[28] in propriete1):
                print("\033[31mVous êtes sur une propriété de Service Public !\nLe propriétaire de cette propriété possède également l'autre propriété de Service Public.\033[0m")
                print("\t=> De ce fait, vous devez \033[33mpayer 1000 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 1000 * lancer
                or2 -= montant_Service
                or1 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or2,"pièces d'or.")
            elif (terrain[12] in propriete1) or (terrain[28] in propriete1):
                print("\033[31mVous êtes sur une propriété de Service Public\033[0m, vous devez \033[33mpayer 400 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 400 * lancer
                or2 -= montant_Service
                or1 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or2,"pièces d'or.")
        elif (position2 == 5) or (position2 == 15) or (position2 == 25) or (position2 == 35):
            print("Vous êtes arrivé à la\033[33m",terrain[position2],"\033[0m: vous devez payer l'impôt de cette propriété à\033[36m",player1,"\033[0msachant qu'il \033[33mpossède actuellement",player1_NB_Gare,"gare(s)\033[0m.")
            if player1_NB_Gare < 3:
                impot_Gare = player1_NB_Gare * impots_Terrain[position2]
            elif player1_NB_Gare == 3:
                impot_Gare = player1_NB_Gare * impots_Terrain[position2] + impots_Terrain[position2]
            else:
                impot_Gare = (2 * player1_NB_Gare) * impots_Terrain[position2]
            or2 -= impot_Gare
            or1 += impot_Gare
            print("Vous devez payer un montant de\033[33m",impot_Gare,"pièces d'or\033[0m.\nIl vous reste\033[33m",or2,"pièces d'or.\033[36m")
            print(player1,"\033[0ma désormais\033[0m",or1,"pièces d'or.\033[0m")
        else:
            print("Vous êtes sur la propriété\033[33m",terrain[position2],"\033[0mqui appartient à\033[36m",player1,"!\033[0m")
            print("\033[31mVous devez lui payer les impôts liés à cette propriété.\033[0m")
            impots = impots_Terrain[position2]
            or2 -= impots
            or1 += impots
            print("\033[31mMontant des impôts\033[0m :",impots,"pièces d'or.\nIl vous reste",or2,"pièces d'or.")
    else:
        print("\033[36m")
        print(player3,'\033[0mpossède cette carte, \033[31mvous devez lui payer un impôt\033[0m')
        if (position2 == 12) or (position2 == 28):
            if (terrain[12] in propriete3) and (terrain[28] in propriete3):
                print("\033[31mVous êtes sur une propriété de Service Public !\nLe propriétaire de cette propriété possède également l'autre propriété de Service Public.\033[0m")
                print("\t=> De ce fait, vous devez \033[33mpayer 1000 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 1000 * lancer
                or2 -= montant_Service
                or3 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or2,"pièces d'or.")
            elif (terrain[12] in propriete3) or (terrain[28] in propriete3):
                print("\033[31mVous êtes sur une propriété de Service Public\033[0m, vous devez \033[33mpayer 400 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 400 * lancer
                or2 -= montant_Service
                or3 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or2,"pièces d'or.")
        elif (position2 == 5) or (position2 == 15) or (position2 == 25) or (position2 == 35):
            print("Vous êtes arrivé à la\033[33m",terrain[position2],"\033[0m: vous devez payer l'impôt de cette propriété à\033[36m",player3,"\033[0msachant qu'il \033[33mpossède actuellement",player3_NB_Gare,"gare(s)\033[0m.")
            if player3_NB_Gare < 3:
                impot_Gare = player3_NB_Gare * impots_Terrain[position2]
            elif player3_NB_Gare == 3:
                impot_Gare = player3_NB_Gare * impots_Terrain[position2] + impots_Terrain[position2]
            else:
                impot_Gare = (2 * player3_NB_Gare) * impots_Terrain[position2]
            or2 -= impot_Gare
            or3 += impot_Gare
            print("Vous devez payer un montant de\033[33m",impot_Gare,"pièces d'or\033[0m.\nIl vous reste\033[33m",or2,"pièces d'or.\033[36m")
            print(player3,"\033[0ma désormais\033[0m",or3,"pièces d'or.\033[0m")
        else:
            print("Vous êtes sur la propriété\033[33m",terrain[position2],"\033[0mqui appartient à\033[36m",player3,"!\033[0m")
            print("\033[31mVous devez lui payer les impôts liés à cette propriété.\033[0m")
            impots = impots_Terrain[position2]
            or2 -= impots
            or3 += impots
            print("\033[31mMontant des impôts\033[0m :",impots,"pièces d'or.\nIl vous reste",or2,"pièces d'or.")


    etat_double(double2_statut,rand)


def propriete_Joueur3():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,or1,or2,or3,double3_statut,impots_Terrain,player3_NB_Gare,value_Propriete3
    if terrain[position3] not in allpropriete:
        choix = ''
        prix = market(position3)
        couleur = check_Couleurs(position3)
        print("\033[33mCouleur de la carte :\033[36m",couleur,"\033[0m")
        print("\033[31mRappel\033[0m : vous possédez",or3,"pièces d'or.")
        print("Cette propriété est \033[32mlibre\033[0m, voulez vous l'acheté pour un montant de\033[33m",prix,"\033[0mpièces d'or ? ( 'oui' ou 'non' )")
        choix = input("Réponse : \033[36m")
        print("\033[0m")
        if choix == 'oui':
            if prix > or3:
                print("\033[31mVous ne possédez pas d'assez d'argent pour acquérir cette propriété.\033[0m")
                #Mettre en place l'hypothéque de carte et/ou revente Maison/Hotel et/ou proposé de vendre une carte à un joueur et/ou proposé la propriété aux enchères.
            elif prix == or3:
                choix = ''
                choix = input("\033[33mAttention, si vous achetez cette propriété vous n'aurez plus d'argent pour le prochain tour !\033[0m Voulez-vous continuer ? ('oui' ou 'non')\nRéponse : \033[36m")
                print("\033[0m")
                if choix == 'oui':
                    or3 -= prix
                    propriete3.append(terrain[position3])
                    allpropriete.append(terrain[position3])
                    if (position3 == 5) or (position3 == 15) or (position3 == 25) or (position3 == 35):
                        player3_NB_Gare += 1
                    nb_Couleur(couleur,rand)
                    print("\033[36mVous avez acheté la propriété\033[33m",terrain[position3],"\033[0mpour un montant de\033[33m",prix,"pièces d'or\033[0m !\nElle a été ajoutée à vos possessions actuelles.\n")
                    print("RAPPEL :\nVos possessions actuelles :\n",propriete3,"\n")
                    print("Vous n'avez plus d'argent actuellement pour le prochain tour.")
                else:
                    print("Vous avez abandonné l'achat de cette propriété.")
            else:
                or3 -= prix
                propriete3.append(terrain[position3])
                allpropriete.append(terrain[position3])
                if (position3 == 5) or (position3 == 15) or (position3 == 25) or (position3 == 35):
                    player3_NB_Gare += 1
                nb_Couleur(couleur,rand)
                print("\033[36mVous avez acheté la propriété\033[33m",terrain[position3],"\033[0mpour un montant de\033[33m",prix,"pièces d'or\033[0m !\nElle a été ajoutée à vos possessions actuelles.\n")
                print("RAPPEL :\nVos possessions actuelles :\n",propriete3,"\n")
        else:
            #print("Oh dommage !")
            encheres(position3,prix)
    elif terrain[position3] in propriete3:
        print("\033[36mVous possédez déjà cette carte.\033[0m")
    elif terrain[position3] in propriete1:
        print("\033[36m")
        print(player1,'\033[0mpossède cette carte, \033[31mvous devez lui payer un impôt\033[0m')
        if (position3 == 12) or (position3 == 28):
            if (terrain[12] in propriete1) and (terrain[28] in propriete1):
                print("\033[31mVous êtes sur une propriété de Service Public !\nLe propriétaire de cette propriété possède également l'autre propriété de Service Public.\033[0m")
                print("\t=> De ce fait, vous devez \033[33mpayer 1000 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 1000 * lancer
                or3 -= montant_Service
                or1 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or3,"pièces d'or.")
            elif (terrain[12] in propriete1) or (terrain[28] in propriete1):
                print("\033[31mVous êtes sur une propriété de Service Public\033[0m, vous devez \033[33mpayer 400 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 400 * lancer
                or3 -= montant_Service
                or1 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or3,"pièces d'or.")
        elif (position3 == 5) or (position3 == 15) or (position3 == 25) or (position3 == 35):
            print("Vous êtes arrivé à la\033[33m",terrain[position3],"\033[0m: vous devez payer l'impôt de cette propriété à\033[36m",player1,"\033[0msachant qu'il \033[33mpossède actuellement",player1_NB_Gare,"gare(s)\033[0m.")
            if player1_NB_Gare < 3:
                impot_Gare = player1_NB_Gare * impots_Terrain[position3]
            elif player1_NB_Gare == 3:
                impot_Gare = player1_NB_Gare * impots_Terrain[position3] + impots_Terrain[position3]
            else:
                impot_Gare = (2 * player1_NB_Gare) * impots_Terrain[position3]
            or3 -= impot_Gare
            or1 += impot_Gare
            print("Vous devez payer un montant de\033[33m",impot_Gare,"pièces d'or\033[0m.\nIl vous reste\033[33m",or3,"pièces d'or.\033[36m")
            print(player1,"\033[0ma désormais\033[0m",or1,"pièces d'or.\033[0m")
        else:
            print("Vous êtes sur la propriété\033[33m",terrain[position3],"\033[0mqui appartient à\033[36m",player1,"!\033[0m")
            print("\033[31mVous devez lui payer les impôts liés à cette propriété.\033[0m")
            impots = impots_Terrain[position3]
            or3 -= impots
            or1 += impots
            print("\033[31mMontant des impôts\033[0m :",impots,"pièces d'or.\nIl vous reste",or3,"pièces d'or.")

    else:
        print("\033[36m")
        print(player2,'\033[0mpossède cette carte, \033[31mvous devez lui payer un impôt\033[0m')
        if (position3 == 12) or (position3 == 28):
            if (terrain[12] in propriete2) and (terrain[28] in propriete2):
                print("\033[31mVous êtes sur une propriété de Service Public !\nLe propriétaire de cette propriété possède également l'autre propriété de Service Public.\033[0m")
                print("\t=> De ce fait, vous devez \033[33mpayer 1000 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 1000 * lancer
                or3 -= montant_Service
                or2 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or3,"pièces d'or.")
            elif (terrain[12] in propriete2) or (terrain[28] in propriete2):
                print("\033[31mVous êtes sur une propriété de Service Public\033[0m, vous devez \033[33mpayer 400 fois le résultat de votre lancer de dés !\033[0m")
                print("\033[31mRappel\033[0m, votre lancer était de\033[33m",lancer,"points.\033[0m")
                montant_Service = 400 * lancer
                or3 -= montant_Service
                or2 += montant_Service
                print("Vous devez payer un montant de\033[31m",montant_Service,"pièces d'or\033[0m.\nIl vous reste",or3,"pièces d'or.")
        elif (position3 == 5) or (position3 == 15) or (position3 == 25) or (position3 == 35):
            print("Vous êtes arrivé à la\033[33m",terrain[position3],"\033[0m: vous devez payer l'impôt de cette propriété à\033[36m",player2,"\033[0msachant qu'il \033[33mpossède actuellement",player2_NB_Gare,"gare(s)\033[0m.")
            if player2_NB_Gare < 3:
                impot_Gare = player2_NB_Gare * impots_Terrain[position3]
            elif player2_NB_Gare == 3:
                impot_Gare = player2_NB_Gare * impots_Terrain[position3] + impots_Terrain[position3]
            else:
                impot_Gare = (2 * player2_NB_Gare) * impots_Terrain[position3]
            or3 -= impot_Gare
            or2 += impot_Gare
            print("Vous devez payer un montant de\033[33m",impot_Gare,"pièces d'or\033[0m.\nIl vous reste\033[33m",or3,"pièces d'or.\033[36m")
            print(player2,"\033[0ma désormais\033[0m",or2,"pièces d'or.\033[0m")
        else:
            print("Vous êtes sur la propriété\033[33m",terrain[position3],"\033[0mqui appartient à\033[36m",player2,"!\033[0m")
            print("\033[31mVous devez lui payer les impôts liés à cette propriété.\033[0m")
            impots = impots_Terrain[position3]
            or3 -= impots
            or2 += impots
            print("\033[31mMontant des impôts\033[0m :",impots,"pièces d'or.\nIl vous reste",or3,"pièces d'or.")

    etat_double(double3_statut,rand)


def type_Carte():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete,player1_Faillite,player2_Faillite,player3_Faillite
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,prison_Joker1,prison_Joker2,prison_Joker3,DEPART,or1,or2,or3,double1_statut,double2_statut,double3_statut
    double_sub = False
    if rand == 1:
        if position1 == 0:
            print("\033[35mVous êtes sur la Case Départ, vous gagnez ",DEPART*2," pièces d'or.\033[0m")
            or1 += DEPART * 2
        elif position1 == 4:
            print("\033[31mImpôts sur le Revenu !\033[0m Payer ",DEPART,"pièces d'or !")
            or1 -= DEPART
        elif position1 == 10:
            print("Vous vous trouvé en Simple Visite en Prison !")
        elif position1 == 20:
            print("Bienvenue au Parc Gratuit !")
        elif position1 == 30:
            player1_en_Prison = True
            position1 = 10
            print("\n\n\n\033[31mALLEZ EN PRISON !\033[0m\n")
        elif position1 == 38:
            print("\033[33mTaxe de Luxe !\033[0m Payer ",DEPART/2,"pièces d'or.")
            or1 -= DEPART / 2
        elif (position1 == 2) or (position1 == 17) or (position1 == 33):
            print("\n\n\n\t\033[36mCaisse de Communauté !\033[0m\n")
            communaute = random.randint(1,12)
            if communaute > 0 and communaute <= 3 :
                print("Dettes payées !\nVous devez payer aux autres joueurs 5000 pièces d'or !\033[36m")
                or2 += 5000
                or1 -= 5000
                if NB_player == 3:
                    or3 += 5000
                    or1 -= 5000
                print(player1,"\033[0mn'a plus que ",or1,"pièces d'or\033[36m")
                print(player2,"\033[0ma désormais ",or2,"pièces d'or\033[36m")
                if NB_player == 3:
                    print(player3,"\033[0ma désormais ",or3,"pièces d'or")
            elif communaute > 3 and communaute <= 6 :
                print("\033[31mVous avez des réparations à faire dans vos maisons !\033[0m")
                ''' A CODER PLUS TARD '''
                print("Pour le moment vous ne disposez d'aucune maison, donc aucun montant à payer.")
            elif communaute == 7:
                print("\033[32mC'est votre anniversaire !\033[0m Recevez 7 500 pièces d'or de la banque et 1 000 pièces d'or de chaque joueur.")
                or1 += 7500
                or1 += 1000
                or2 -= 1000
                if NB_player == 3:
                    or1 += 1000
                    or3 -= 1000
                print("Vous avez désormais \033[32m",or1,"\033[0m pièces d'or.")
            elif communaute == 8:
                print("Vous avez dépassé la vitesse réglementaire du code de la Route, payer 500 pièces d'or !")
                or1 -= 500
                print("Votre solde s'élève actuellement à ",or1,"pièces d'or.")
            elif communaute >= 9:
                print("\033[32mRendez vous à la case Parc Gratuit et recevez 4500 pièces d'or.\033[0m")
                position1 = 20
                or1 += 4500
                print(player1,"se trouve désormais au ",terrain[position1],"et dispose de ",or1,"pièces d'or.")
            print("\n\n")
        elif (position1 == 7) or (position1 == 22) or (position1 == 36) :
            print("\n\n\n\t\033[36mCHANCE !\033[0m\n")
            chance = random.randint(1,16)
            if chance == 1:
                print("\033[32mAvancer de trois cases !\033[0m\033[36m")
                position1 += 3
                print(player1,"\033[0mse trouve désormais a ",terrain[position1])
                type_Carte()
            elif chance == 4:
                print("\033[35mReculer de trois cases !\033[0m\033[36m")
                position1 -= 3
                print(player1,"\033[0mse trouve désormais a ",terrain[position1])
                type_Carte()
            elif (chance == 2) or (chance == 3):
                print("Rendez vous à la Gare de Lyon, \033[32msi vous passez par la case Départ\033[0m, touchez ",DEPART,"pièces d'or.")
                if position1 == 7:
                    position1 += 8
                    print("Vous êtes à présent à la Gare de Lyon, mais n'avez pas franchis la case Départ.")
                    propriete_Joueur1()
                elif position1 == 22:
                    position1 += 33
                    if position1 > 39:
                        position1 -= 40
                        if position1 > 0:
                            print("Vous avez \033[32mfranchis la case Départ\033[0m, vous recevez ",DEPART,"pièces d'or.")
                            or1 += DEPART
                    propriete_Joueur1()
                elif position1 == 36:
                    position1 += 19
                    if position1 > 39:
                        position1 -= 40
                        if position1 > 0:
                            print("Vous avez \033[32mfranchis la case Départ\033[0m, vous recevez ",DEPART,"pièces d'or.")
                            or1 += DEPART
                    propriete_Joueur1()
            elif (chance > 4) and (chance <= 7):
                print("\033[36mVous recevez un prix de Beauté\033[0m, recevez 2 000 pièces d'or.")
                or1 += 2000
            elif (chance == 10) or (chance == 12):
                print("\033[36mVous recevez une carte 'Sortie de Prison'\033[0m que vous pourrez utilisé pour sortir de Prison gratuitement.")
                prison_Joker1 = True
            elif chance == 11:
                print("\033[32mRetour case Départ.\033[0m")
                position1 = 0
                type_Carte()
            elif chance == 8 :
                print("\033[32mLa banque vous doit une dividende de 5000 pièces d'or !\033[0m")
                or1 += 5000
            elif chance == 9:
                print("\033[36mRendez-vous Rue de la Paix.\033[0m")
                position1 = 39
                propriete_Joueur1()
            elif chance == 13 or chance == 15:
                print("\033[31mPayez les frais de scolarités !\033[0m Payez 15 000 pièces d'or.")
                or1 -= 15000
                print("Il vous reste\033[35m",or1,"pièces d'or.\033[0m")
            elif chance == 14:
                print("\033[32mVous avez remporté un concours de mot croisé !\033[0m Vous recevez 15 000 pièces d'or !")
                or1 += 15000
            elif chance == 16:
                fiscal = random.randint(0,1)
                print("\033[33mContrôle Fiscal ! Un expert contrôle votre comptabilité !\nAnalyse en cours ... Patientez !\033[0m\n")
                time.sleep(3.5)
                if fiscal == 0:
                    print("\033[32mVotre contrôle s'est bien passé !\033[0m Ouf !")
                else:
                    print("\033[31mVous avez été démasqué ! Vous devez à la banque 30 000 pièces d'or !\033[0m")
                    or1 -= 30000
                    print("Il vous reste\033[35m",or1,"pièces d'or.\033[0m")
        else:
            propriete_Joueur1()
        check_Faillite()
        if not player1_Faillite:
            double_sub = double1_statut

    elif rand == 2:
        if position2 == 0:
            print("\033[35mVous êtes sur la Case Départ, vous gagnez ",DEPART*2," pièces d'or.\033[0m")
            or2 += DEPART * 2
        elif position2 == 4:
            print("\033[31mImpôts sur le Revenu !\033[0m Payer ",DEPART,"pièces d'or !")
            or2 -= DEPART
        elif position2 == 10:
            print("Vous vous trouvé en Simple Visite en Prison !")
        elif position2 == 20:
            print("Bienvenue au Parc Gratuit !")
        elif position2 == 30:
            player2_en_Prison = True
            position2 = 10
            print("\n\n\n\033[31mALLEZ EN PRISON !\033[0m\n")
        elif position2 == 38:
            print("\033[33mTaxe de Luxe !\033[0m Payer ",DEPART/2,"pièces d'or.")
            or2 -= DEPART / 2
        elif (position2 == 2) or (position2 == 17) or (position2 == 33):
            print("\n\n\n\t\033[36mCaisse de Communauté !\033[0m\n")
            communaute = random.randint(1,12)
            if communaute > 0 and communaute <= 3 :
                print("Dettes payées !\nVous devez payer aux autres joueurs 5000 pièces d'or !\033[36m")
                or1 += 5000
                or2 -= 5000
                if NB_player == 3:
                    or3 += 5000
                    or2 -= 5000
                print(player2,"\033[0mn'a plus que ",or2,"pièces d'or\033[36m")
                print(player1,"\033[0ma désormais ",or1,"pièces d'or\033[36m")
                if NB_player == 3:
                    print(player3,"\033[0ma désormais ",or3,"pièces d'or")
            elif communaute > 3 and communaute <= 6 :
                print("\033[31mVous avez des réparations à faire dans vos maisons !\033[0m")
                ''' A CODER PLUS TARD '''
                print("Pour le moment vous ne disposez d'aucune maison, donc aucun montant à payer.")
            elif communaute == 7:
                print("\033[32mC'est votre anniversaire !\033[0m Recevez 7 500 pièces d'or de la banque et 1 000 pièces d'or de chaque joueur.")
                or2 += 7500
                or2 += 1000
                or1 -= 1000
                if NB_player == 3:
                    or2 += 1000
                    or3 -= 1000
                print("Vous avez désormais \033[32m",or2,"\033[0m pièces d'or.")
            elif communaute == 8:
                print("Vous avez dépassé la vitesse réglementaire du code de la Route, payer 500 pièces d'or !")
                or2 -= 500
                print("Votre solde s'élève actuellement à ",or2,"pièces d'or.")
            elif communaute >= 9:
                print("\033[32mRendez vous à la case Parc Gratuit et recevez 4500 pièces d'or.\033[0m")
                position2 = 20
                or2 += 4500
                print(player2,"se trouve désormais au ",terrain[position2],"et dispose de ",or2,"pièces d'or.")
            print("\n\n")
        elif (position2 == 7) or (position2 == 22) or (position2 == 36) :
            print("\n\n\n\t\033[36mCHANCE !\033[0m\n")
            chance = random.randint(1,12)
            if chance == 1:
                print("\033[32mAvancer de trois cases !\033[0m\033[36m")
                position2 += 3
                print(player2,"\033[0mse trouve désormais a ",terrain[position2])
                type_Carte()
            elif chance == 4:
                print("\033[35mReculer de trois cases !\033[0m\033[36m")
                position2 -= 3
                print(player2,"\033[0mse trouve désormais a ",terrain[position2])
                type_Carte()
            elif (chance == 2) or (chance == 3):
                print("Rendez vous à la Gare de Lyon, \033[32msi vous passez par la case Départ\033[0m, touchez ",DEPART,"pièces d'or.")
                if position2 == 7:
                    position2 += 8
                    print("Vous êtes à présent à la Gare de Lyon, mais n'avez pas franchis la case Départ.")
                    propriete_Joueur2()
                elif position2 == 22:
                    position2 += 33
                    if position2 > 39:
                        position2 -= 40
                        if position2 > 0:
                            print("Vous avez \033[32mfranchis la case Départ\033[0m, vous recevez ",DEPART,"pièces d'or.")
                            or2 += DEPART
                    propriete_Joueur2()
                elif position2 == 36:
                    position2 += 19
                    if position2 > 39:
                        position2 -= 40
                        if position2 > 0:
                            print("Vous avez \033[32mfranchis la case Départ\033[0m, vous recevez ",DEPART,"pièces d'or.")
                            or2 += DEPART
                    propriete_Joueur2()
            elif (chance > 4) and (chance <= 7):
                print("\033[36mVous recevez un prix de Beauté\033[0m, recevez 2 000 pièces d'or.")
                or2 += 2000
            elif (chance == 10) or (chance == 12):
                print("\033[36mVous recevez une carte 'Sortie de Prison'\033[0m que vous pourrez utilisé pour sortir de Prison gratuitement.")
                prison_Joker2 = True
            elif chance == 11:
                print("\033[32mRetour case Départ.\033[0m")
                position2 = 0
                type_Carte()
            elif chance == 8 :
                print("\033[32mLa banque vous doit une dividende de 5000 pièces d'or !\033[0m")
                or2 += 5000
            elif chance == 9:
                print("\033[36mRendez-vous Rue de la Paix.\033[0m")
                position2 = 39
                propriete_Joueur2()
            elif chance == 13 or chance == 15:
                print("\033[31mPayez les frais de scolarités !\033[0m Payez 15 000 pièces d'or.")
                or2 -= 15000
                print("Il vous reste\033[35m",or2,"pièces d'or.\033[0m")
            elif chance == 14:
                print("\033[32mVous avez remporté un concours de mot croisé !\033[0m Vous recevez 15 000 pièces d'or !")
                or2 += 15000
            elif chance == 16:
                fiscal = random.randint(0,1)
                print("\033[33mContrôle Fiscal ! Un expert contrôle votre comptabilité !\nAnalyse en cours ... Patientez !\033[0m\n")
                time.sleep(3.5)
                if fiscal == 0:
                    print("\033[32mVotre contrôle s'est bien passé !\033[0m Ouf !")
                else:
                    print("\033[31mVous avez été démasqué ! Vous devez à la banque 30 000 pièces d'or !\033[0m")
                    or2 -= 30000
                    print("Il vous reste\033[35m",or2,"pièces d'or.\033[0m")
        else:
            propriete_Joueur2()
        check_Faillite()
        if not player2_Faillite:
            double_sub = double2_statut

    elif rand == 3:
        if position3 == 0:
            print("\033[35mVous êtes sur la Case Départ, vous gagnez ",DEPART*2," pièces d'or.\033[0m")
            or3 += DEPART * 2
        elif position3 == 4:
            print("\033[31mImpôts sur le Revenu !\033[0m Payer ",DEPART,"pièces d'or !")
            or3 -= DEPART
        elif position3 == 10:
            print("Vous vous trouvé en Simple Visite en Prison !")
        elif position3 == 20:
            print("Bienvenue au Parc Gratuit !")
        elif position3 == 30:
            player3_en_Prison = True
            position3 = 10
            print("\n\n\n\033[31mALLEZ EN PRISON !\033[0m\n")
        elif position3 == 38:
            print("\033[33mTaxe de Luxe !\033[0m Payer ",DEPART/2,"pièces d'or.")
            or3 -= DEPART / 2
        elif (position3 == 2) or (position3 == 17) or (position3 == 33):
            print("\n\n\n\t\033[36mCaisse de Communauté !\033[0m\n")
            communaute = random.randint(1,12)
            if communaute > 0 and communaute <= 3 :
                print("Dettes payées !\nVous devez payer aux autres joueurs 5000 pièces d'or !\033[36m")
                or1 += 5000
                or2 += 5000
                or3 -= 10000
                print(player3,"\033[0mn'a plus que ",or3,"pièces d'or\033[36m")
                print(player1,"\033[0ma désormais ",or1,"pièces d'or\033[36m")
                print(player2,"\033[0ma désormais ",or2,"pièces d'or")
            elif communaute > 3 and communaute <= 6 :
                print("\033[31mVous avez des réparations à faire dans vos maisons !\033[0m")
                ''' A CODER PLUS TARD '''
                print("Pour le moment vous ne disposez d'aucune maison, donc aucun montant à payer.")
            elif communaute == 7:
                print("\033[32mC'est votre anniversaire !\033[0m Recevez 7 500 pièces d'or de la banque et 1 000 pièces d'or de chaque joueur.")
                or3 += 7500
                or3 += 2000
                or1 -= 1000
                or2 -= 1000
                print("Vous avez désormais \033[32m",or3,"\033[0m pièces d'or.")
            elif communaute == 8:
                print("Vous avez dépassé la vitesse réglementaire du code de la Route, payer 500 pièces d'or !")
                or3 -= 500
                print("Votre solde s'élève actuellement à ",or3,"pièces d'or.")
            elif communaute >= 9:
                print("\033[32mRendez vous à la case Parc Gratuit et recevez 4500 pièces d'or.\033[0m")
                position3 = 20
                or3 += 4500
                print(player3,"se trouve désormais au ",terrain[position3],"et dispose de ",or3,"pièces d'or.")
            print("\n\n")
        elif (position3 == 7) or (position3 == 22) or (position3 == 36) :
            print("\n\n\n\t\033[36mCHANCE !\033[0m\n")
            chance = random.randint(1,12)
            if chance == 1:
                print("\033[32mAvancer de trois cases !\033[0m\033[36m")
                position3 += 3
                print(player3,"\033[0mse trouve désormais a ",terrain[position3])
                type_Carte()
            elif chance == 4:
                print("\033[35mReculer de trois cases !\033[0m\033[36m")
                position3 -= 3
                print(player3,"\033[0mse trouve désormais a ",terrain[position3])
                type_Carte()
            elif (chance == 2) or (chance == 3):
                print("Rendez vous à la Gare de Lyon, \033[32msi vous passez par la case Départ\033[0m, touchez ",DEPART,"pièces d'or.")
                if position3 == 7:
                    position3 += 8
                    print("Vous êtes à présent à la Gare de Lyon, mais n'avez pas franchis la case Départ.")
                    propriete_Joueur3()
                elif position3 == 22:
                    position3 += 33
                    if position3 > 39:
                        position3 -= 40
                        if position3 > 0:
                            print("Vous avez \033[32mfranchis la case Départ\033[0m, vous recevez ",DEPART,"pièces d'or.")
                            or3 += DEPART
                    propriete_Joueur3()
                elif position3 == 36:
                    position3 += 19
                    if position3 > 39:
                        position3 -= 40
                        if position3 > 0:
                            print("Vous avez \033[32mfranchis la case Départ\033[0m, vous recevez ",DEPART,"pièces d'or.")
                            or3 += DEPART
                    propriete_Joueur3()
            elif (chance > 4) and (chance <= 7):
                print("\033[36mVous recevez un prix de Beauté\033[0m, recevez 2 000 pièces d'or.")
                or3 += 2000
            elif (chance == 10) or (chance == 12):
                print("\033[36mVous recevez une carte 'Sortie de Prison'\033[0m que vous pourrez utilisé pour sortir de Prison gratuitement.")
                prison_Joker3 = True
            elif chance == 11:
                print("\033[32mRetour case Départ.\033[0m")
                position3 = 0
                type_Carte()
            elif chance == 8 :
                print("\033[32mLa banque vous doit une dividende de 5000 pièces d'or !\033[0m")
                or3 += 5000
            elif chance == 9:
                print("\033[36mRendez-vous Rue de la Paix.\033[0m")
                position3 = 39
                propriete_Joueur3()
            elif chance == 13 or chance == 15:
                print("\033[31mPayez les frais de scolarités !\033[0m Payez 15 000 pièces d'or.")
                or3 -= 15000
                print("Il vous reste\033[35m",or3,"pièces d'or.\033[0m")
            elif chance == 14:
                print("\033[32mVous avez remporté un concours de mot croisé !\033[0m Vous recevez 15 000 pièces d'or !")
                or3 += 15000
            elif chance == 16:
                fiscal = random.randint(0,1)
                print("\033[33mContrôle Fiscal ! Un expert contrôle votre comptabilité !\nAnalyse en cours ... Patientez !\033[0m\n")
                time.sleep(3.5)
                if fiscal == 0:
                    print("\033[32mVotre contrôle s'est bien passé !\033[0m Ouf !")
                else:
                    print("\033[31mVous avez été démasqué ! Vous devez à la banque 30 000 pièces d'or !\033[0m")
                    or3 -= 30000
                    print("Il vous reste\033[35m",or3,"pièces d'or.\033[0m")
        else:
            propriete_Joueur3()
        check_Faillite()
        if not player3_Faillite:
            double_sub = double3_statut
    etat_double(double_sub,rand)


def joueur1():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,prison_Joker1,prison_Joker2,prison_Joker3,or1,double1_statut
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    '''
    de1 = 3
    de2 = 3
    '''
    lancer = de1 + de2
    if de1 == de2:
        double1 += 1
        if double1 < 3:
            print("\033[32mVous avez réalisé :",double1,"doubles consécutifs.\033[0m")
        if double1 == 3:
            player1_en_Prison = True
            double1_statut = False
            position1 = 10
            print("Dé #1 :",de1,'point(s)\tDé #2 :',de2,'point(s)')
            print("\033[31mVous avez réalisé 3 doubles ! Vous allez en prison !\033[0m")
        else:
            double1_statut = True
    else:
        double1 = 0
        double1_statut = False
        '''
        A FAIRE : Précisé que la règle des Doubles doit s'appliquer 3 fois consécutivement  pour être en Prison
        A FAIRE : Si le joueur fait un double, il gagne le droit de rejouer tant que double1 != 3
        '''

    if not player1_en_Prison:
        position1 += lancer
        #position1 = 15
        if position1 > 39:
            position1 -= 40
            if position1 > 0:
                print("\033[35mVous avez franchis la case Départ, vous recevez ",DEPART,"pièces d'or.\033[0m")
                or1 += DEPART

            ''' METTRE case Départ +15 000 '''

        print("Dé #1 :",de1,'point(s)\tDé #2 :',de2,'point(s)')
        print("\033[36m",player1,'\033[0mva avancer de \033[36m',lancer,'cases.\033[0m')
        print("\033[36m",player1,"\033[0m: Vous êtes arrivé sur la case : \033[33m",terrain[position1],"\033[0m")
        type_Carte()

def joueur2():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,prison_Joker1,prison_Joker2,prison_Joker3,or2,double2_statut
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    lancer = de1 + de2
    if de1 == de2:
        double2 += 1
        if double2 < 3:
            print("\033[32mVous avez réalisé :",double2,"doubles consécutifs.\033[0m")
        if double2 == 3:
            player2_en_Prison = True
            double2_statut = False
            position2 = 10
            print("Dé #1 : ",de1,'point(s)\tDé #2 : ',de2,'point(s)')
            print("\033[31mVous avez réalisé 3 doubles ! Vous allez en prison !\033[0m")
        else:
            double2_statut = True
    else:
        double2 = 0
        double2_statut = False
        '''
        A FAIRE : Précisé que la règle des Doubles doit s'appliquer 3 fois consécutivement  pour être en Prison
        A FAIRE : Si le joueur fait un double, il gagne le droit de rejouer tant que double1 != 3
        '''

    if not player2_en_Prison:

        position2 += lancer
        if position2 > 39:
            position2 -= 40
            if position2 > 0:
                print("\033[35mVous avez franchis la case Départ, vous recevez ",DEPART,"pièces d'or.\033[0m")
                or2 += DEPART


            ''' METTRE case Départ +15 000 '''

        print(" Dé #1 :",de1,'point(s)\tDé #2 :',de2,'point(s)')
        print("\033[36m",player2,'\033[0mva avancer de \033[36m',lancer,'cases.\033[0m')
        print("\033[36m",player2,"\033[0m: Vous êtes arrivé sur la case : \033[33m",terrain[position2],"\033[0m")
        type_Carte()

def joueur3():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,prison_Joker1,prison_Joker2,prison_Joker3,or3,double3_statut
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    lancer = de1 + de2
    if de1 == de2:
        double3 += 1
        if double3 < 3:
            print("\033[32mVous avez réalisé :",double3,"doubles consécutifs.\033[0m")
        if double3 == 3:
            player3_en_Prison = True
            double3_statut = False
            position3 = 10
            print("Dé #1 :",de1,'point(s)\tDé #2 :',de2,'point(s)')
            print("\033[31mVous avez réalisé 3 doubles ! Vous allez en prison !\033[0m")
        else:
            double3_statut = True
    else:
        double3 = 0
        double3_statut = False
        '''
        A FAIRE : Précisé que la règle des Doubles doit s'appliquer 3 fois consécutivement  pour être en Prison
        A FAIRE : Si le joueur fait un double, il gagne le droit de rejouer tant que double1 != 3
        '''

    if not player3_en_Prison:
        position3 += lancer
        if position3 > 39:
            position3 -= 40
            if position3 > 0:
                print("\033[35mVous avez franchis la case Départ, vous recevez ",DEPART,"pièces d'or.\033[0m")
                or3 += DEPART


            ''' METTRE case Départ +15 000 '''

        print("Dé #1 :",de1,'point(s)\tDé #2 :',de2,'point(s)')
        print("\033[36m",player3,'\033[0mva avancer de \033[36m',lancer,'cases.\033[0m')
        print("\033[36m",player3,"\033[0m: Vous êtes arrivé sur la case : \033[33m",terrain[position3],"\033[0m")
        type_Carte()


def prison():
    global double1,double2,double3,position1,position2,position3,terrain,or1,or2,or3,PRIX_PRISON,tentative1,tentative2,tentative3
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,prison_Joker1,prison_Joker2,prison_Joker3
    if player1_en_Prison:
        position1 = 10
        print("Le joueur se retrouve en \033[35m",terrain[position1],"\033[0m et doit effectuer un \033[36mdouble\033[0m pour sortir ou \033[35mpayer",PRIX_PRISON,"\033[0mpièces d'or.")
        choixPrison= ''
        jokerPrison = ''
        if prison_Joker1 and jokerPrison == '':

            while jokerPrison != 'oui' and jokerPrison != 'non':
                jokerPrison = input("\033[33mVous disposez d'une carte Joker 'Sortie de Prison'\033[0m, voulez vous l'utiliser ?\n('oui' ou 'non') Réponse : \033[36m")
                print("\033[0m")
            if jokerPrison == 'oui':
                prison_Joker1 = False
                player1_en_Prison = False
                try:
                    input("\033[36mVous avez utilisé votre Joker !\033[0m Vous sortez de prison immédiatement. Lancez vos dés...")
                except SyntaxError:
                    pass
                joueur1()
            else:
                print("Vous gardez votre Joker pour plus tard !")

        if ((prison_Joker1 == False) and (player1_en_Prison == True)) or (jokerPrison == 'non'):
            while choixPrison != 'payer' and choixPrison != 'double':
                choixPrison = input("Entrez \033[36mdouble\033[0m pour Faire un double ou \033[35mpayer\033[0m pour sortir de la prison : ")
            if choixPrison == 'payer':
                or1 -= PRIX_PRISON
                double1 = 0
                tentative1 = 3
                player1_en_Prison = False
                try:
                    print("\033[32mVous avez payé votre caution de ",PRIX_PRISON,"pièces d'or\033[0m")
                    print("Il vous reste un montant de : ",or1,"pièces d'or")
                    input("\n\nVous pouvez désormais lancer vos dés ...\n")
                except SyntaxError:
                    pass
                joueur1()
            else:
                de1 = random.randint(1,6)
                de2 = random.randint(1,6)
                print("Dé #1 : ",de1,'point(s)\tDé #2 : ',de2,'point(s)\n')
                if de1 == de2:
                    lancer = de1 + de2
                    position1 += lancer
                    print("\033[32mFélicitation\033[0m, vous avez \033[36mréalisé un doublé\033[0m : vous sortez de Prison et avancé immédiatement à la case : \033[36m",terrain[position1],"\033[0m")
                    if position1 > 39:
                        position1 -= 40
                        if position1 > 0:
                            print("\033[35mVous avez franchis la case Départ, vous recevez ",DEPART,"pièces d'or.\033[0m")
                            or1 += DEPART
                    double1 = 0
                    tentative1 = 3
                    player1_en_Prison = False
                    type_Carte()
                else:
                    tentative1 -= 1
                    if tentative1 > 0:
                        print("\033[35mVous n'avez pas réalisé de double\033[0m, il ne vous reste que \033[31m",tentative1,"tentative(s)\033[0m.")
                    else:
                        print("\033[33mVous n'avez pas réalise de double et vous n'avez plus de tentative \033[0m: \033[31mvous devez obligatoirement payer.\033[0m")
                if tentative1 == 0:
                    or1 -= PRIX_PRISON
                    double1 = 0
                    tentative1 = 3
                    player1_en_Prison = False
                    try:
                        print("\033[32mVous avez payé votre caution de ",PRIX_PRISON,"pièces d'or\033[0m")
                        print("Il vous reste un montant de : ",or1,"pièces d'or")
                        input("\n\nVous pouvez désormais lancer vos dés ...\n")
                    except SyntaxError:
                        pass
                    joueur1()


    if player2_en_Prison:
        position2 = 10
        print("Le joueur se retrouve en \033[35m",terrain[position2],"\033[0m et doit effectuer un \033[36mdouble\033[0m pour sortir ou \033[35mpayer",PRIX_PRISON,"\033[0mpièces d'or.")
        choixPrison= ''
        jokerPrison = ''
        if prison_Joker2 and jokerPrison == '':

            while jokerPrison != 'oui' and jokerPrison != 'non':
                jokerPrison = input("\033[33mVous disposez d'une carte Joker 'Sortie de Prison'\033[0m, voulez vous l'utiliser ?\n('oui' ou 'non') Réponse : \033[36m")
                print("\033[0m")
            if jokerPrison == 'oui':
                prison_Joker2 = False
                player2_en_Prison = False
                try:
                    input("\033[36mVous avez utilisé votre Joker !\033[0m Vous sortez de prison immédiatement. Lancez vos dés...")
                except SyntaxError:
                    pass
                joueur2()
            else:
                print("Vous gardez votre Joker pour plus tard !")

        if ((prison_Joker2 == False) and (player2_en_Prison == True)) or (jokerPrison == 'non'):
            while choixPrison != 'payer' and choixPrison != 'double':
                choixPrison = input("Entrez \033[36mdouble\033[0m pour Faire un double ou \033[35mpayer\033[0m pour sortir de la prison : ")
            if choixPrison == 'payer':
                or2 -= PRIX_PRISON
                double2 = 0
                tentative2 = 3
                player2_en_Prison = False
                try:
                    print("\033[32mVous avez payé votre caution de ",PRIX_PRISON,"pièces d'or\033[0m")
                    print("Il vous reste un montant de : ",or2,"pièces d'or")
                    input("\n\nVous pouvez désormais lancer vos dés ...\n")
                except SyntaxError:
                    pass
                joueur2()
            else:
                de1 = random.randint(1,6)
                de2 = random.randint(1,6)
                print("Dé #1 : ",de1,'point(s)\tDé #2 : ',de2,'point(s)\n')
                if de1 == de2:
                    lancer = de1 + de2
                    position2 += lancer
                    print("\033[32mFélicitation\033[0m, vous avez \033[36mréalisé un doublé\033[0m : vous sortez de Prison et avancé immédiatement à la case : \033[36m",terrain[position2],"\033[0m")
                    if position2 > 39:
                        position2 -= 40
                        if position2 > 0:
                            print("\033[35mVous avez franchis la case Départ, vous recevez ",DEPART,"pièces d'or.\033[0m")
                            or2 += DEPART
                    double2 = 0
                    tentative2 = 3
                    player2_en_Prison = False
                    type_Carte()
                else:
                    tentative2 -= 1
                    if tentative2 > 0:
                        print("\033[35mVous n'avez pas réalisé de double\033[0m, il ne vous reste que \033[31m",tentative2,"tentative(s)\033[0m.")
                    else:
                        print("\033[33mVous n'avez pas réalise de double et vous n'avez plus de tentative \033[0m: \033[31mvous devez obligatoirement payer.\033[0m")
                if tentative2 == 0:
                    or2 -= PRIX_PRISON
                    double2 = 0
                    tentative2 = 3
                    player2_en_Prison = False
                    try:
                        print("\033[32mVous avez payé votre caution de ",PRIX_PRISON,"pièces d'or\033[0m")
                        print("Il vous reste un montant de : ",or2,"pièces d'or")
                        input("\n\nVous pouvez désormais lancer vos dés ...\n")
                    except SyntaxError:
                        pass
                    joueur2()


    if player3_en_Prison:
        position3 = 10
        print("Le joueur se retrouve en \033[35m",terrain[position3],"\033[0m et doit effectuer un \033[36mdouble\033[0m pour sortir ou \033[35mpayer",PRIX_PRISON,"\033[0mpièces d'or.")
        choixPrison= ''
        jokerPrison = ''
        if prison_Joker3 and jokerPrison == '':

            while jokerPrison != 'oui' and jokerPrison != 'non':
                jokerPrison = input("\033[33mVous disposez d'une carte Joker 'Sortie de Prison'\033[0m, voulez vous l'utiliser ?\n('oui' ou 'non') Réponse : \033[36m")
                print("\033[0m")
            if jokerPrison == 'oui':
                prison_Joker3 = False
                player3_en_Prison = False
                try:
                    input("\033[36mVous avez utilisé votre Joker !\033[0m Vous sortez de prison immédiatement. Lancez vos dés...")
                except SyntaxError:
                    pass
                joueur3()
            else:
                print("Vous gardez votre Joker pour plus tard !")

        if ((prison_Joker3 == False) and (player3_en_Prison == True)) or (jokerPrison == 'non'):
            while choixPrison != 'payer' and choixPrison != 'double':
                choixPrison = input("Entrez \033[36mdouble\033[0m pour Faire un double ou \033[35mpayer\033[0m pour sortir de la prison : ")
            if choixPrison == 'payer':
                or3 -= PRIX_PRISON
                double3 = 0
                tentative3 = 3
                player3_en_Prison = False
                try:
                    print("\033[32mVous avez payé votre caution de ",PRIX_PRISON,"pièces d'or\033[0m")
                    print("Il vous reste un montant de : ",or3,"pièces d'or")
                    input("\n\nVous pouvez désormais lancer vos dés ...\n")
                except SyntaxError:
                    pass
                joueur3()
            else:
                de1 = random.randint(1,6)
                de2 = random.randint(1,6)
                print("Dé #1 : ",de1,'point(s)\tDé #2 : ',de2,'point(s)\n')
                if de1 == de2:
                    lancer = de1 + de2
                    position3 += lancer
                    print("\033[32mFélicitation\033[0m, vous avez \033[36mréalisé un doublé\033[0m : vous sortez de Prison et avancé immédiatement à la case : \033[36m",terrain[position3],"\033[0m")
                    if position3 > 39:
                        position3 -= 40
                        if position3 > 0:
                            print("\033[35mVous avez franchis la case Départ, vous recevez ",DEPART,"pièces d'or.\033[0m")
                            or3 += DEPART
                    double3 = 0
                    tentative3 = 3
                    player3_en_Prison = False
                    type_Carte()
                else:
                    tentative3 -= 1
                    if tentative3 > 0:
                        print("\033[35mVous n'avez pas réalisé de double\033[0m, il ne vous reste que \033[31m",tentative3,"tentative(s)\033[0m.")
                    else:
                        print("\033[33mVous n'avez pas réalise de double et vous n'avez plus de tentative \033[0m: \033[31mvous devez obligatoirement payer.\033[0m")
                if tentative3 == 0:
                    or3 -= PRIX_PRISON
                    double3 = 0
                    tentative3 = 3
                    player3_en_Prison = False
                    try:
                        print("\033[32mVous avez payé votre caution de ",PRIX_PRISON,"pièces d'or\033[0m")
                        print("Il vous reste un montant de : ",or3,"pièces d'or")
                        input("\n\nVous pouvez désormais lancer vos dés ...\n")
                    except SyntaxError:
                        pass
                    joueur3()


def launch():
    global NB_player,player1,player2,player3,rand,lancer,double1,double2,double3,position1,position2,position3,terrain,allpropriete
    global player1_en_Prison,player2_en_Prison,player3_en_Prison,player1_Faillite,player2_Faillite,player3_Faillite
    lancer = 0
    if rand == 1:
        if not player1_Faillite:
            if player1_en_Prison:
                print("\nAu tour de",player1,"de jouer !")
                prison()
            else:
                try:
                    print("\nAu tour de",player1,"de jouer !")
                    input("\n\nAppuyer sur une touche pour lancer vos dés ...\n")
                except SyntaxError:
                    pass
                joueur1()
        else:
            print("\033[36m",player1,"\033[35ma fait faillite.\033[0m")

    elif rand == 2:
        if player2_en_Prison:
            print("\nAu tour de",player2,"de jouer !")
            prison()
        else:
            try:
                print("\nAu tour de",player2,"de jouer !")
                input("\n\nAppuyer sur une touche pour lancer vos dés ...\n")
            except SyntaxError:
                pass
            joueur2()

    elif rand == 3:
        if player3_en_Prison:
            print("\nAu tour de",player3,"de jouer !")
            prison()
        else:
            try:
                print("\nAu tour de",player3,"de jouer !")
                input("\n\nAppuyer sur une touche pour lancer vos dés ...\n")
            except SyntaxError:
                pass
            joueur3()

    constat()


def start():
    global NB_player,player1,player2,player3,GOLD,rand
    print("Le jeu va à présent démarrer.")
    print("Vous démarrez avec\033[32m",GOLD,"\033[0mpièces d'or chacun.")
    print("\n\033[32mQue le meilleur Picsou gagne !\033[0m")
    rand = random.randint(1,NB_player)
    if rand==1:
        print("\033[36m",player1,"\033[0mva commencer la partie !")
    elif rand==2:
        print("\033[36m",player2,"\033[0mva commencer la partie !")
    elif rand==3:
        print("\033[36m",player3,"\033[0mva commencer la partie !")
    try:
        input("\n\n\033[35mAppuyer sur une touche lorsque vous êtes prêt à démarrer la partie !\033[0m\n")
    except SyntaxError:
        pass
    launch()

def select():
    global NB_player,NB_player_alt,player1,player2,player3
    print("\n\n\n")
    while (NB_player != 2) and (NB_player != 3):
        NB_player = int(input("Veuillez sélectionner le nombre de joueur \033[33m(2-3)\033[0m : "))
    print(NB_player,"joueurs. \033[32mLet's start\033[0m !")
    NB_player_alt = NB_player
    print("Veuillez saisir vos prénoms : \n")
    if NB_player == 2:
        player1 = input("Prénom joueur 1 : \033[36m")
        print("\033[0m")
        player2 = input("Prénom joueur 2 : \033[36m")
        print("\033[0m")
        #print("Bonjour,\n",player1,"et ",player2)
    else:
        player1 = input("Prénom joueur 1 : \033[36m")
        print("\033[0m")
        player2 = input("Prénom joueur 2 : \033[36m")
        print("\033[0m")
        player3 = input("Prénom joueur 3 : \033[36m")
        print("\033[0m")
        #print("Bonjour, ",player1,",",player2,",",player3)
    start()



def play():
    init()
    global version
    print("\n\n\t\tBienvenue sur le jeu du \033[35mMONO\033[0m\033[36mPOLY\033[0m !")
    print("\t\tVous pouvez joué à ce jeu à 2-3 joueurs.")
    print("\t\tÊtes vous prêt à dominer vos amis ?\n\n")
    print("\t\t\033[33mCe jeu est régie par les règles du Monopoly Classique Français.\n\t\tVoir http://www.monopolypedia.fr/regles/Regle.php pour plus d'informations.\033[0m")
    print("\t\t\t\t\t\t\t\t\tMonopoly Version :\033[31m",version,"\033[0m")
    select()



#Boucle infinie
'''
for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
    if event.type == QUIT:    #Si un de ces événements est de type QUIT
        sys.exit(0)    #On arrête la boucle
'''
#play()

''' LANCEMENT DU PROGRAMME '''
play()
''' LANCEMENT DU PROGRAMME '''


''' TEST DES PRIX DES VALEURS '''
'''
init()
print("La taille de value_Terrain est : ",len(value_Terrain))
print("La taille de terrain est : ",len(terrain))
global value_Terrain,terrain
for i in range(len(value_Terrain)):
    print(terrain[i],"=",value_Terrain[i])
'''


'''
Guide de couleurs Terminal:
31 : Rouge
32 : Vert
33 : Orange
34 : Bleu
35 : Rose
36 : Bleu clair

Format :
\033[31m \033[0m
\033[32m \033[0m
\033[33m \033[0m
\033[34m \033[0m
\033[35m \033[0m
'''
