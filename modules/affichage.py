"""Ce module contient les principales fonctions d'affichage du casse brique."""
from modules import upemtk as tk  #Dans le même dossier mais comme import fais depuis le main qui est dans le dossier du dessus
from modules import constantes as C

################### Fonctions d'affichage ##########################

def victoire(blocks_list, bar_coord, time_spend, score):
	"""Cette fonction affiche Victoire si toutes les briques ont été déruites.
		Avec blocks_list, la liste contenant les coordonnées et résistance des briques
		Bar_coord les coordonnées de la raquette
		score , le nombre total de point du joueur en fonction du nombre de briques qu'il a détruite
		et time_spend, le temps s'étant écoulé depuis le debut. """
	
	if blocks_list == []:
		draw_variable(["balle", "raquette", "temps", "score"], balle=(-10,-10,0,0), raquette=bar_coord, temps=time_spend, score=score)
		#On affiche la balle en dehors de l'écran car l'arg est nécessaire
		tk.texte(C.WIDTH/2, ((C.HEIGHT/2)+C.EXTRA_TOP), "GAGNE !", "orange red", ancrage="center", police="fixedsys", taille=72)
		tk.attente_clic_ou_touche()
		return True   #Si True est retourné, un break est levé dans la boucle principale
	return False

def defaite(ball_coord, blocks_list, bar_coord, time_spend, score):  #A voir avec style
	"""Cette fonction affiche Defaite si la balle est partie en dessous.
		Avec blocks_list, la liste contenant les coordonnées et résistance des briques
		Bar_coord les coordonnées de la raquette
		ball_coord les coordonnées de la balle
		score , le nombre total de point du joueur en fonction du nombre de briques qu'il a détruite
		et time_spend, le temps s'étant écoulé depuis le debut. """
	
	if not ball_coord:
		draw_variable(["balle", "raquette", "temps", "score"], balle=(-10,-10,0,0), raquette=bar_coord, temps=time_spend, score=score)
		tk.texte(C.WIDTH/2, ((C.HEIGHT/2)+C.EXTRA_TOP), "PERDU !", "orange red", ancrage="center", police="fixedsys",taille=72)
		tk.attente_clic_ou_touche()
		return True  #Meme fonctionnement que pour victoire()
	return False
			

def compare_efface(id_dico, **kwargs):
	"""Efface les objets qui ont été modifiés et renvoie une liste contenant leur noms pour les réafficher après.
	id_dico contient en clés [raquette, blocs, temps, score]
	**kwargs prend l'ensemble des arguments nommés, sans avoir besoin de les déclarer 
	il les met par la suite dans id_dico. """
	
	change_list = ["balle"]
	tk.efface("balle")
	
	#Comp ancien int raquette et nouveau :
	nouveau = sum(kwargs["raquette"])
	if nouveau != id_dico["raquette"]:
		tk.efface("raquette")
		id_dico["raquette"] = nouveau
		change_list.append("raquette")
	
	#Comp ancien blocs et nouveau :
	nouveau = sum([x[4] for x in kwargs["blocs"]])
	if nouveau != id_dico["blocs"]:
		for block in kwargs["blocs"]:
			tk.efface(block[5])
			id_dico["blocs"] = nouveau
			change_list.append("blocs")
			
	#Comp temps:
	if int(kwargs["temps"][0]) != id_dico["temps"]:
		tk.efface("inter_temps")
		id_dico["temps"] = int(kwargs["temps"][0])
		change_list.append("temps")
		
	#Comp score:
	if kwargs["score"] != id_dico["score"]:
		tk.efface("inter_score")
		id_dico["score"] = kwargs["score"]
		change_list.append("score")
	
	return change_list
	
def draw_init():
	"""Affiche au début les éléments qui ne seront jamais effaces."""
	
	tk.rectangle(0, C.EXTRA_TOP, C.WIDTH, C.HEIGHT_TOTAL, "black", "black")
	tk.rectangle(0, 0, 0 + C.WIDTH, 0 + C.EXTRA_TOP, "black", "blue2", epaisseur=2)  #Le fond de la fenêtre
	tk.texte(C.WIDTH/2, 70/2, "Casse Brique", "firebrick1", police="fixedsys", ancrage="center", taille=42)
	tk.texte(C.WIDTH//7, 80, "Score: ", "green2", police="fixedsys", ancrage="center", taille=23)
	tk.texte(C.WIDTH//5*4, 80, "Temps: ", "green2", police="fixedsys", ancrage="center", taille=23)
	
def draw_variable(change_list, **kwargs):
	"""Affiche certains objets du jeu en fonction de si ils ont ete modifies depuis la boucle d'avant.
	change_list de la forme ["balle", "score",], on utilisera ensuite les str pour acceder au kwargs."""
	
	if change_list == []:
		return
	for argument in change_list:
		if argument == "balle":
			tk.cercle(kwargs["balle"][0], kwargs["balle"][1], C.BALL_RADIUS, "red", "red", tag="balle")
		elif argument == "raquette":
			tk.rectangle(kwargs["raquette"][0], kwargs["raquette"][1], kwargs["raquette"][2], kwargs["raquette"][3], "green2", "green2", tag="raquette")
		elif argument == "blocs":
			for block in kwargs["blocs"]:
				color = C.COLOR_TUP[block[4]]
				efface_obj = tk.rectangle(block[0], block[1], block[2], block[3], "black", color)
				block[5] = efface_obj
		elif argument == "temps":
			tk.texte(C.WIDTH//5*4.6, 80, str(int(kwargs["temps"][0])), "green2", police="fixedsys", ancrage="center", taille=23, tag="inter_temps")
		elif argument == "score":
			tk.texte(C.WIDTH//7*1.8, 80, str(kwargs["score"]), "green2", police="fixedsys", ancrage="center", taille=23, tag="inter_score")
	return
