"""Ce module contient toutes les constantes du jeu, venir ici pour modifier un des paramètre du casse brique."""
import os
### Constantes ecran ##################

WIDTH = 500		#Largeur de la fenêtre de jeu
HEIGHT = 500	#Hauteur de la fenêtre de jeu
EXTRA_TOP = 100  #Taille de l'interface au dessus
HEIGHT_TOTAL = HEIGHT + EXTRA_TOP  #Hauteur totale de la fenêtre

### Constantes briques ################

ENVERGURE_BRIQUES = HEIGHT // 3    #Portion de HEIGHT où il y aura les briques
BLOCK_BASE = (WIDTH//5, 41, 1)  #(width, height, resistance)

### Constantes balle ##################

BALL_BASE = (WIDTH / 2, (HEIGHT / 2)+EXTRA_TOP, 1, 1)  #Position et valeurs de base de la balle

BALL_SPEED_Y = 3                            #!!!!!!!!!!!!!!!!!!MODIFIER ICI POUR CHANGER LES VITESSES !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
BALL_SPEED_X = 3                            #!!!!!!!!!!!!!!!!!!           ET ICI AUSSI                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

BALL_SPEED0 = (0, BALL_SPEED_Y)
BALL_SPEED1 = (BALL_SPEED_X, BALL_SPEED_Y*1.25)  #Déplacement de base de la balle
BALL_SPEED2 = (BALL_SPEED_X*2, BALL_SPEED_Y*1.5)

BALL_RADIUS = 5  #Rayon de la balle

### Constantes raquette ###############

BAR_RECT = (WIDTH / 4, (HEIGHT / 40))     #Longueur et hauteur de la raquette
BAR_MID_WIDTH = BAR_RECT[0] // 2
BAR_BASE = (WIDTH / 4 * 1.5, (HEIGHT_TOTAL / 20 * 19))    #Position de base de la raquette
BAR_MOUV = 8                                #!!!!!!!!!!!!!!!!!!MODIFIER ICI POUR CHANGER VITESSE RAQUETTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

### Pause dans boucle principale ######

FREQUENCE = 0.0125                         #!!!!!!!!!!!!!!!!!!MODIFIER ICI POUR CHANGER FREQUENCE DE BOUCLE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#################### Constantes style ############################

COLOR_TUP = ["white", "yellow", "orange", "red"]  #Couleurs des briques en fonction de leur résistance

#################### Constantes fichiers #################

SCORE_PATH = os.path.join("scores", "high.score")   #Chemin du fichier des scores
SCORE_FIRST_LINE = "-|| CASSE-BRIQUE HIGH-SCORES ||-\n"

IMAGE1_PATH = os.path.join("images", "soud.gif")
IMAGE2_PATH = os.path.join("images", "wil.gif")
ICON_PATH = os.path.join(os.getcwd(), "images", "soud.ico")  #Besoin du chemin absolu
