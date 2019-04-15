"""Ce module gère tous les menus du jeu et les petites fenetres externes."""

from modules import upemtk as tk
from modules import constantes as C
from modules import fichier as FI

import os
import time
from tkinter.filedialog import askopenfilename #Pour ouvrir un fichier avec le menu parcourir
from tkinter.messagebox import showerror #Pour afficher des fenetres d'erreur

	
def init_window():
	"""Initialise la fenetre du module upemtk."""
	
	tk.cree_fenetre(C.WIDTH, C.HEIGHT_TOTAL)
	screen_width = tk.__canevas.root.winfo_screenwidth() #Hauteur de l'écran
	screen_height = tk.__canevas.root.winfo_screenheight()  #Longueur de l'écran
	tk.__canevas.root.geometry("%dx%d+%d+%d" %(C.WIDTH, C.HEIGHT_TOTAL, (screen_width - C.WIDTH)/2, (screen_height - C.HEIGHT_TOTAL)/4))
	#A partir de la taille de l'ecran on positionne la fenetre au milieu.
	tk.__canevas.root.resizable(width=False, height=False)  #Pas possible de redimensionner la fenetre.
	if os.name == "nt":  #Ne marche pas sous Linux de l'IUT et fait planter le jeu
		tk.__canevas.root.iconbitmap(C.ICON_PATH) #Change l'icone de la fenetre
	tk.__canevas.root.title("Menu Casse Brique")  #Titre de la fenetre
	tk.__canevas.root.protocol("WM_DELETE_WINDOW", on_exit)  #Fonction à appeler si on appuie sur la croix de la fenetre tkinter
															 #A été ajoutée car vraiment ennuyant de devoir faire controle C pour quitter
															 
def on_exit():
	"""Fonction activée si on appuie sur la croix de la fenêtre tkinter."""
	
	global bye
	bye = True
	
def draw_init():
	"""Affichage de la fenetre de menu(formes, images, texte)."""
	
	sixieme = C.HEIGHT_TOTAL//6
	tk.rectangle(0, 0, C.WIDTH, sixieme*2, "black", "blue2", epaisseur=2)
	
	tk.rectangle(0, sixieme*2, C.WIDTH, sixieme*3, "black", "yellow", epaisseur=2)
	tk.rectangle(0, sixieme*3, C.WIDTH, sixieme*4, "black", "yellow", epaisseur=2)
	tk.rectangle(0, sixieme*4, C.WIDTH, sixieme*5, "black", "yellow", epaisseur=2)
	tk.rectangle(0, sixieme*5, C.WIDTH, C.HEIGHT_TOTAL, "black", "yellow", epaisseur=2)
	

	tk.texte(C.WIDTH/2, sixieme//2, "Casse-Brique", "red2", police="fixedsys", ancrage="center", taille=54)
	tk.texte(C.WIDTH/2, sixieme//2*3, "--SW--", "red2", police="fixedsys", ancrage="center", taille=60)
	#Image gif 100x84
	tk.image(C.WIDTH//16*2, sixieme//2*3, C.IMAGE1_PATH)
	tk.image(C.WIDTH//16*14.25, sixieme//2*3, C.IMAGE2_PATH)
	
	tk.texte(C.WIDTH/2, sixieme//2*5, "Normal", "black", police="fixedsys", ancrage="center", taille=20)
	tk.texte(C.WIDTH/2, sixieme//2*7, "Automatique", "black", police="fixedsys", ancrage="center", taille=20)
	tk.texte(C.WIDTH/2, sixieme//2*9, "Charger un fichier", "black", police="fixedsys", ancrage="center", taille=20)
	tk.texte(C.WIDTH/2, sixieme//2*11, "High-scores", "black", police="fixedsys", ancrage="center", taille=20)
	
def inside_rect(x, y, rect):
	"""Renvoie True si le point de coordonnees (x,y) est dans le rectangle rect de forme (a,b,c,d)."""
	
	if (x >= rect[0] and x <= rect[2]) and (y >= rect[1] and y <= rect[3]):
		return True
	return False

def choix_clic():
	"""Attend un clic sur une des cases du menu et renvoie une chaine de caracterere en consequence.
	Fonction permettant la sélection par le joueur. """
	
	sixieme = C.HEIGHT_TOTAL//6
	x, y, type_clic = tk.attente_clic()
	
	if inside_rect(x, y, (0, sixieme*2, C.WIDTH, sixieme*3)): #Normal
		tk.ferme_fenetre()
		return "N"
	
	elif inside_rect(x, y, (0, sixieme*3, C.WIDTH, sixieme*4)): #Automatique
		tk.ferme_fenetre()
		return "A"
	
	elif inside_rect(x, y, (0, sixieme*4, C.WIDTH, sixieme*5)): #Charger fichier
		fichier = tk.StringVar()
		fichier.set(askopenfilename(initialdir=os.path.join(os.getcwd(), "niveaux"), title="Selectionnez un fichier"))
		tk.ferme_fenetre()
		return ("F", fichier.get())
	
	elif inside_rect(x, y, (0, sixieme*5, C.WIDTH, sixieme*6)): #High-scores
		tk.ferme_fenetre()
		return "H"
	
	return
	
def menu():
	"""Affiche la fenetre de menu jusqu'a ce que l'utilisateur clique sur une des cases. """
	init_window()
	draw_init()
	global bye
	bye = False
	
	while True:
		if bye:
			break
		result = choix_clic()
		if result is not None:
			return result
		
		tk.mise_a_jour()
		time.sleep(0.1)
		
		
def error_window(title, message):
	"""Fonction de tkinter pour afficher des petites fenetres d'erreur."""
	
	showerror(title, message)
	
	
def draw_scores():
	"""Affichage de la fentre des high_scores."""
	
	dixieme = C.HEIGHT_TOTAL//10
	tk.rectangle(0, 0, C.WIDTH, dixieme*3, "black", "blue2", epaisseur=2)
	
	tk.rectangle(0, dixieme*3, C.WIDTH, dixieme*4, "black", "yellow", epaisseur=2)
	tk.rectangle(0, dixieme*4, C.WIDTH, dixieme*5, "black", "yellow", epaisseur=2)
	tk.rectangle(0, dixieme*5, C.WIDTH, dixieme*6, "black", "yellow", epaisseur=2)
	tk.rectangle(0, dixieme*6, C.WIDTH, dixieme*7, "black", "yellow", epaisseur=2)
	tk.rectangle(0, dixieme*7, C.WIDTH, dixieme*8, "black", "yellow", epaisseur=2)
	tk.rectangle(0, dixieme*8, C.WIDTH, dixieme*9, "black", "yellow", epaisseur=2)
	tk.rectangle(0, dixieme*9, C.WIDTH, C.HEIGHT_TOTAL, "black", "yellow", epaisseur=2)
	

	tk.texte(C.WIDTH/2, dixieme//1.5, "Casse-Brique", "red2", police="fixedsys", ancrage="center", taille=54)
	tk.texte(C.WIDTH/2, dixieme//2*4.5, "SCORES", "black", police="fixedsys", ancrage="center", taille=60)
	#Image gif 100x84
	tk.image(C.WIDTH//16*2, dixieme//2*4.5, C.IMAGE1_PATH)
	tk.image(C.WIDTH//16*14.25, dixieme//2*4.5, C.IMAGE2_PATH)
	
	tk.texte(C.WIDTH/2, dixieme//2*7, "JOUEUR / DATE / TEMPS / SCORE", "black", police="fixedsys", ancrage="center", taille=18)
	
	score_list = FI.read_score()
	score_list = sorted(score_list, key=lambda x: x[3], reverse=True)
	score_list = score_list[:10]
	if score_list != []:
		i = 9
		for s in score_list:
			chaine_score = " / ".join(s)
			taille = 17
			
			if tk.longueur_texte(chaine_score) > C.WIDTH - 10:
				taille = 16
			tk.texte(C.WIDTH/2, dixieme//1.9*i, chaine_score, "blue", police="fixedsys", ancrage="center", taille=taille)
			i += 2
			
def high_score():
	"""Affiche la fenetre des high_score tant qu'elle n'est pas quittee avec la croix."""
	
	init_window()
	draw_scores()
	global bye
	bye = False
	
	while True:
		if bye:
			break
		tk.mise_a_jour()
		time.sleep(0.1)
	tk.ferme_fenetre()
		
	
