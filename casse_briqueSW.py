from modules import upemtk as tk
from modules import constantes as C  #Fichier contenant toutes les constantes du jeu
from modules import affichage as AFF #Fichier contenant les fonctions d'affichage du jeu
from modules import collisions as COL   #Fichier contenant les fonctions de collision du jeu
from modules import menu as ME  #Fichier contenant la fenetre de menu et ses sous-fenetres
from modules import fichier as FI  #Fichier contenant les fonctions pour la gestion des fichiers

import os  #Pour os.path
import time  #Pour le time.sleep() à la fin de la boucle
import sys   #Pour le sys.argv
import random  #Pour la création des briques
from tkinter.messagebox import *  #Pour demander si on enregistre le score a la fin d'une partie
from tkinter import simpledialog  #-------------------------------------------------------------

############ Fonctions ################

def on_exit():
	"""Fonction activée si on appuie sur la croix de la fenêtre tkinter."""
	
	global bye
	bye = True

def init_window():
	"""Initialise la fenetre du module upemtk. Permet de rajouter des détails esthétiques.
	   Par exemple va centrer la fenetre en fonction de la taille de l'ecran,
	   lui ajouter une icone originale, un titre et permettre d'appuyer sur la croix pour quitter."""
	
	tk.cree_fenetre(C.WIDTH, C.HEIGHT_TOTAL)
	screen_width = tk.__canevas.root.winfo_screenwidth() #Hauteur de l'écran
	screen_height = tk.__canevas.root.winfo_screenheight()  #Longueur de l'écran
	tk.__canevas.root.geometry("%dx%d+%d+%d" %(C.WIDTH, C.HEIGHT_TOTAL, (screen_width - C.WIDTH)/2, (screen_height - C.HEIGHT_TOTAL)/4))
	#A partir de la taille de l'ecran on positionne la fenetre au milieu.
	tk.__canevas.root.resizable(width=False, height=False)  #Pas possible de redimensionner la fenetre.
	if os.name == "nt":  #Ne marche pas sous Linux de l'IUT et fait planter le jeu
		tk.__canevas.root.iconbitmap(C.ICON_PATH) #Change l'icone de la fenetre
	tk.__canevas.root.title("Casse Brique SW")  #Titre de la fenetre
	tk.__canevas.root.protocol("WM_DELETE_WINDOW", on_exit)  #Fonction à appeler si on appuie sur la croix de la fenetre 
	tk.__canevas.root.focus_force()							 #A été ajoutée car ce n'est pas pratique de devoir faire contrôle C pour quitter
	#Pour remettre le focus sur la nouvelle fenetre apres la fenetre de menu et pouvoir jouer directement
	
def create_resistants_blocks():
	"""Créé une liste de briques dans les 1/3 supérieurs de l'écran avec 2 chances sur 3 qu'il y ait une brique
	   et donne aux briques une résistance comprise entre 1 et 3 de manière aléatoire."""
	   
	blocks_list = []
	max_line = C.WIDTH // C.BLOCK_BASE[0]  #Nombre de blocs par ligne
	max_column = C.ENVERGURE_BRIQUES // C.BLOCK_BASE[1]  #Nombre de blocs par colonne
	
	x = 0
	y = C.EXTRA_TOP
	for i in range(max_column):
		for j in range(max_line):
			if random.randint(1, 3) > 1:  #2 chances sur 3 qu'il y ait un bloc à cet endroit
				resistance = random.randint(1, 3)  #Resistance du bloc
				blocks_list.append([x, y, x + C.BLOCK_BASE[0]-1, y + C.BLOCK_BASE[1]-1, resistance, 0])
				#Le 0 a la fin de chaque bloc sera remplacé par son tag d'affichage
				#Pour ensuite pouvoir l'effacer vite, cela limite le temps d'affichage fenêtre.
			x += C.BLOCK_BASE[0]
		x = 0
		y += C.BLOCK_BASE[1]
	return blocks_list
	
def create_blocks_from_file(nom_fichier):
	"""Créé et renvoie une liste de briques en fonction d'un schema donné par un fichier.
	   Arrange la taille des briques pour que ca rentre dans la fenetre."""
	correct = FI.correct_niveau(nom_fichier)
	if not correct[0]:
		ME.error_window("Erreur dans le fichier", correct[1])
		return False
	
	n_ligne = len(correct[0])
	n_colonne = len(correct[0][0])
	w_block = C.WIDTH // n_colonne
	h_block = C.ENVERGURE_BRIQUES // n_ligne
	
	blocks_list = []
	x = 0
	y = C.EXTRA_TOP
	for i in range(n_ligne):
		for res in correct[0][i]:
			if res != ".":
				blocks_list.append([x, y, x + w_block-1, y + h_block-1, int(res), 0])
			x += w_block
		x = 0
		y += h_block
	return blocks_list
	

def balle_actu(ball_coord, ball_speed):
	"""Actualise la position de la balle.
	   Avec ball_coord la position de la balle.
	   Et ball_speed sa vitesse. """
	
	ball_x = ball_coord[0] + ball_speed[0] * ball_coord[2]
	ball_y = ball_coord[1] + ball_speed[1] * ball_coord[3]
	return (ball_x, ball_y, ball_coord[2], ball_coord[3])
		
	
def mouvement_raquette(bar_coord):
	"""Si une des touche droite ou gauche du clavier a été appuyée 
		alors il s'effectue un mouvement de la raquette,
		tant qu'elle ne se trouve pas au bord de la fenêtre.
		Avec bar_coord les coordonnées de la raquette. """
	
	event = tk.donne_evenement()
	chaine = ""
	
	if tk.type_evenement(event) == "Touche":
		chaine = tk.touche(event)
	
	if chaine == "":
		return bar_coord
	if chaine == "Right" and not(bar_coord[2] + C.BAR_MOUV > C.WIDTH + C.BAR_MOUV):
		return (bar_coord[0] + C.BAR_MOUV, bar_coord[1], bar_coord[2] + C.BAR_MOUV, bar_coord[3])
	if chaine == "Left" and not(bar_coord[0] - C.BAR_MOUV < 0 - C.BAR_MOUV):
		return (bar_coord[0] - C.BAR_MOUV, bar_coord[1], bar_coord[2] - C.BAR_MOUV, bar_coord[3])
	return bar_coord

def actu_time(time_spend):
	"""Actualisation du temps passé. Renvoie un tuple de la forme (secondes passées, time.time()).
		Avec time_spend la durée du temps qui s'est écoulé."""
	
	now = time.time()
	return (time_spend[0] + (now - time_spend[1]), now)
	
def main(mode=("N","")):
	"""Fonction principale du programme, avec un joueur humain."""
	
	############# Initialisations ###########################################################
	
	time_spend = (0, time.time())
	score = 0
	ball_speed = C.BALL_SPEED0
	
	global bye          #Si on appuie sur la croix de la fenêtre, bye vaudra True et un break sera levé dans la boucle principale
	bye = False
	bad_file = False    #Si le main est quitté car le fichier lu est mauvais
	
	############# Gestion de la creation et de la position de la fenetre ################# 
	init_window()
	AFF.draw_init()
	
	############ Creation des objets #####################################################
	ball_coord = C.BALL_BASE
	bar_coord = (C.BAR_BASE[0], C.BAR_BASE[1], C.BAR_BASE[0] + C.BAR_RECT[0] , C.BAR_BASE[1] + C.BAR_RECT[1])
	
	#Mode de creation des briques
	if mode[0] == "F":
		blocks_list = create_blocks_from_file(mode[1])
		if not blocks_list:
			bye = True
			bad_file = True
	else:
		blocks_list = create_resistants_blocks()
	
	#Dico pour gestion des modifications
	id_dico = {"balle": 0, "raquette" : 0, "blocs" : 0, "temps" : 0, "score" : 0}
	
	############ Boucle principale #######################################################
	while True:
		if bye:     #Comme dit precédemment
			break
		
		ball_coord = balle_actu(ball_coord, ball_speed)
		
		####### Perdu ou Gagne ###########################################################
		ball_coord = COL.check_collisions_window(ball_coord)  #Renvoie False si la balle en dehors de l'écran
		if AFF.defaite(ball_coord, blocks_list, bar_coord, time_spend, score): #Si ball_coord == False
			break
		if AFF.victoire(blocks_list, bar_coord, time_spend, score):   #Si plus d'éléments dans blocks_list
			break
		
		####### Collisions et destructions ################################################
		ball_coord, ball_speed = COL.check_collisions_bar(ball_coord, ball_speed, bar_coord)  #Collisions sur la raquette
		ball_coord, score = COL.check_collisions_block(ball_coord, blocks_list, score)  #Collisions sur les blocs
		COL.check_destroy(blocks_list)  #Supprime un bloc de la liste si sa résistance est à 0
		
		####### Dessin, Mouvement, Mise a Jour de la Fenetre, Sleep #######################
		change_list = AFF.compare_efface(id_dico, balle=ball_coord, raquette=bar_coord, blocs=blocks_list, temps=time_spend, score=score)
		AFF.draw_variable(change_list, balle=ball_coord, raquette=bar_coord, blocs=blocks_list, temps=time_spend, score=score)
		
		bar_coord = mouvement_raquette(bar_coord)  #Interaction de l'utilisateur
		
		tk.mise_a_jour()  #Affiche sur la fenetre ce qui a été dessinée
		time.sleep(C.FREQUENCE)  #Petite pause pour ne pas que cela aille trop vite et que cela prenne tout le processeur
		time_spend = actu_time(time_spend)
		
	########### Si Boucle principale finie ################################################
	
	#Gestion de l'enregistrement du score a la fin de la partie
	if not bad_file: #Pour eviter de demander d'enregistrer le score si le fichier lu est mauvais et donc pas eu de partie	
		to_score = askyesno("Score ?","Voulez-vous enregistrer votre score?")
		if to_score:
			pseudo = simpledialog.askstring("Joueur", "Quel est votre pseudo?",parent=tk.__canevas.root)
			if pseudo is not None:
				FI.add_score(pseudo, score, int(time_spend[0]))
	tk.ferme_fenetre()
	
def main_auto():
	"""Fonction principale du programme, en mode automatique.
	   Si problèmes sur le fonctionnement aller voir les commentaires de main().
	   + Cf. READ_ME. """
	   
	############# Statistiques ###########################################################
	
	time_spend = (0, time.time())
	score = 0
	ball_speed = C.BALL_SPEED1
	
	global bye          #Si on appuie sur la croix de la fenêtre, bye vaudra True et un break sera levé dans la boucle principale
	bye = False
	
	############# Gestion de la creation et de la position de la fenetre ################# 
	init_window()
	AFF.draw_init()
	
	############ Creation des objets #####################################################
	ball_coord = C.BALL_BASE
	bar_coord = (C.BAR_BASE[0], C.BAR_BASE[1], C.BAR_BASE[0] + C.BAR_RECT[0] , C.BAR_BASE[1] + C.BAR_RECT[1])
	blocks_list = create_resistants_blocks()
	id_dico = {"balle": 0, "raquette" : 0, "blocs" : 0, "temps" : 0, "score" : 0}
	
	############ Boucle principale #######################################################
	while True:
		if bye:     #Comme dit precédemment
			break

		# tk.efface_tout()
		ball_coord = balle_actu(ball_coord, ball_speed)
		
		####### Perdu ou Gagne ###########################################################
		ball_coord = COL.check_collisions_window(ball_coord)
		if AFF.defaite(ball_coord, blocks_list, bar_coord, time_spend, score):
			break
		if AFF.victoire(blocks_list, bar_coord, time_spend, score):
			break
			
		####### Collisions et destructions ################################################
		ball_coord = COL.check_collisions_bar_auto(ball_coord, bar_coord)
		ball_coord, score = COL.check_collisions_block(ball_coord, blocks_list, score)
		COL.check_destroy(blocks_list)
		
		####### Dessin, Mouvement, Mise a Jour de la Fenetre, Sleep #######################
		change_list = AFF.compare_efface(id_dico, balle=ball_coord, raquette=bar_coord, blocs=blocks_list, temps=time_spend, score=score)
		AFF.draw_variable(change_list, balle=ball_coord, raquette=bar_coord, blocs=blocks_list, temps=time_spend, score=score)
		
		bar_coord = COL.verif_outside_auto(ball_coord, bar_coord)
		
		tk.mise_a_jour()
		time.sleep(C.FREQUENCE)
		time_spend = actu_time(time_spend)
		
	########### Si Boucle principale finie ################################################
	tk.ferme_fenetre()
	
		
########### Corps principal ##############################################################
if __name__ == "__main__":
	
	if len(sys.argv) < 2 or len(sys.argv) > 2:
		choix = ME.menu()
	elif sys.argv[1] == "auto":
		choix = "A"
	elif sys.argv[1] == "player":
		choix = "N"
	else:   #Si il y a bien un sys.argv[1] mais qu'il n'est pas connu
		choix = ME.menu()
		
	
	if choix == "N":
		main()
	elif choix == "A":
		main_auto()
	elif choix[0] == "F":
		main(mode=choix)
	elif choix == "H":
		ME.high_score()
	else:
		print("Pas encore implémenté...")
		sys.exit()
	
