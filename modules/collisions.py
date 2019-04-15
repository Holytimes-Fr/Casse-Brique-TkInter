"""Ce module contient les principales fonctions pour les calculs des collisions."""
from modules import upemtk as tk  #Dans le même dossier mais comme import fais depuis le main qui est dans le dossier du dessus
from modules import constantes as C

#################### Fonctions de collision #########################

def check_collisions_window(ball_coord):
	"""Vérifie si la balle touche un des bords de la fenêtre, si ce n'est pas le bords inférieur, la balle est renvoyée 
		dans le sens contraire duquel elle est venue.
	    Si au contraire c'est le bas de la fenêtre, la balle tombe et la fonction renvoie False et la fonction défaite() du module affichage est lancée.
	    Avec ball_coord les coordonnées de la balle au moment de l'incidence. """
	   
	#Côtés
	if ball_coord[0] - C.BALL_RADIUS < 0:
		ball_deca_x = 1
	elif ball_coord[0] + C.BALL_RADIUS >= C.WIDTH:
		ball_deca_x = -1
	else:
		ball_deca_x = ball_coord[2]
	
	#Haut-Bas	
	if ball_coord[1] - C.BALL_RADIUS < C.EXTRA_TOP:
		ball_deca_y = 1
	elif ball_coord[1] + C.BALL_RADIUS >= C.HEIGHT_TOTAL:
		return False
	else:
		ball_deca_y = ball_coord[3]
	
	return (ball_coord[0], ball_coord[1], ball_deca_x, ball_deca_y)

	
def check_collisions_bar_auto(ball_coord, bar_coord):
	"""Vérifie si la balle touche la raquette, si oui la renvoie vers le haut.
		Avec ball_coord les coordonnées de la balle 
		et bar_coord les coordonnées de la raquette. """
	
	if (ball_coord[0] - C.BALL_RADIUS <= bar_coord[2] and ball_coord[0] + C.BALL_RADIUS >= bar_coord[0]) and ball_coord[1] + C.BALL_RADIUS >= bar_coord[1]:
		ball_deca_x = ball_coord[2]
		ball_deca_y = -1
	else:
		ball_deca_x = ball_coord[2]
		ball_deca_y = ball_coord[3]
	
	return (ball_coord[0], ball_coord[1], ball_deca_x, ball_deca_y)
	
def check_collisions_bar(ball_coord, ball_speed, bar_coord): 
	"""Vérifie si la balle touche la raquette, si oui la renvoie :
		tout droit si la balle rebondit sur le milieu de la raquette
		et vers la droite si elle touche le côté droit de la raquette
		et vers la gauche si elle touche le côté gauche de la raquette. 
		Avec ball_coord les coordonnées de la balle 
		bar_coord les coordonnées de la raquette
		et ball_speed, la vitesse de déplacement de la balle. """
	
	if (ball_coord[0] - C.BALL_RADIUS <= bar_coord[2] and ball_coord[0] + C.BALL_RADIUS >= bar_coord[0]) and ball_coord[1] + C.BALL_RADIUS >= bar_coord[1]:
		distance = ball_coord[0] - bar_coord[0]
		repartition = C.BAR_RECT[0] / 6
		if distance <= repartition:
			ball_speed = C.BALL_SPEED2
			ball_deca_x = -1
		elif distance <= repartition * 2:
			ball_speed = C.BALL_SPEED1
			ball_deca_x = -1
		elif distance <= repartition * 4:
			ball_speed = C.BALL_SPEED0
			ball_deca_x = 1
		elif distance <= repartition * 5:
			ball_speed = C.BALL_SPEED1
			ball_deca_x = 1
		elif distance <= repartition * 6:
			ball_speed = C.BALL_SPEED2
			ball_deca_x = 1
		else:
			ball_deca_x = 1
		ball_deca_y = -1
		
		return (ball_coord[0], ball_coord[1], ball_deca_x, ball_deca_y), ball_speed
	
	return ball_coord, ball_speed
				


def check_collisions_block(ball_coord, blocks_list, score):
	"""Vérifie si la balle touche une des briques, si oui elle repart dans le sens inverse d'arrivée et la brique perd 1 de résistance.
		Avec ball_coord les coordonnées de la balle
		Blocks_list, la liste contenant les coordonnées et résistance des briques
		et score , le nombre total de point du joueur en fonction du nombre de briques qu'il a détruite. """
	
	x = ball_coord[2]
	y = ball_coord[3]
	amplitude_x = (ball_coord[0] - C.BALL_RADIUS, ball_coord[0] + C.BALL_RADIUS)
	amplitude_y = (ball_coord[1] - C.BALL_RADIUS, ball_coord[1] + C.BALL_RADIUS)
	b = False
	for block in blocks_list:
		if (amplitude_x[0] <= block[2] and amplitude_x[1] >= block[0]) and (amplitude_y[0] <= block[3] and amplitude_y[1] >= block[1]):
			if (block[1] <= amplitude_y[1] and block[1] >= amplitude_y[0]) or (block[3] <= amplitude_y[1] and block[3] >= amplitude_y[0]):
				y = y * -1
				block[4] -= 1
				score += 1
				b = True
			if (block[0] <= amplitude_x[1] and block[0] >= amplitude_x[0]) or (block[2] <= amplitude_x[1] and block[2] >= amplitude_x[0]):
				x = x * -1
				if not b:
					block[4] -= 1
					score += 1
				b = True
			if b:
				break

	return (ball_coord[0], ball_coord[1], x, y), score
	
	
def check_destroy(blocks_list):
	"""Vérifie si la résistance d'une des briques est à 0, si oui la supprime de la liste.
		 Avec blocks_list, la liste contenant les coordonnées et résistance des briques. """
	
	i = 0
	while i < len(blocks_list):
		if blocks_list[i][4] == 0:
			b = blocks_list[i]
			tk.efface(b[5])
			tk.rectangle(b[0], b[1], b[2], b[3], "black", "black") #Pour repasser par dessus l'ancien block
			blocks_list.pop(i)
		else:
			i += 1

			
def verif_outside_auto(ball_coord, bar_coord):
	"""Fonction utilisée dans le mode automatique au cas où la raquette viendrait à dépasser des côtés.
		Avec ball_coord les coordonnées de la balle 
		et bar_coord les coordonnées de la raquette. """
	
	bar_coord2 = (ball_coord[0] - C.BAR_RECT[0]/2, bar_coord[1], ball_coord[0] + C.BAR_RECT[0]/2, bar_coord[3])
	if bar_coord2[0] < 0:
		return (0, bar_coord2[1], bar_coord2[2] + (0-bar_coord2[0]), bar_coord2[3])
	elif bar_coord2[2] > C.WIDTH:
		return (bar_coord2[0] - (bar_coord2[2] - C.WIDTH), bar_coord2[1], C.WIDTH, bar_coord2[3])
	return bar_coord2
			
