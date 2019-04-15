"""Module s'occupant de la gestion des fichiers."""

from modules import upemtk as tk
from modules import constantes as C
from modules import menu as ME

import os
import datetime  #Pour le score

#Exemple de fichier qui marche pour charger un schéma de briques particulier

"""
8
4

3 2 1 . . 1 2 3
1 2 3 1 1 3 2 1
2 2 2 2 2 2 2 2
. 1 . 1 . 1 . 1
"""

def correct_niveau(nom_fichier):
	"""Renvoie False si le fichier n'est pas conforme, sinon renvoie une matrice
    	contenant la resistance de chaque brique et un point si il y a un vide."""
	
	with open(nom_fichier, 'r') as f:
		data = f.read()
		
	lignes = data.split("\n")
	
	#On ne va garder que les chiffres, les points et les espaces
	
	lignes_numerique = []
	for ligne in lignes:
		l = ""
		for carac in ligne:
			if carac in "0123456789. ":
				l += carac
		if l != "":
			lignes_numerique.append(l)
	
	#On verifie que le formatage est comme on le veut
	
	if len(lignes_numerique[0]) > 2 or not str.isdecimal(lignes_numerique[0]):
		return (False, "Nombre de briques par colonne incorrect.")
	col = int(lignes_numerique[0])
	
	if len(lignes_numerique[1]) > 2 or not str.isdecimal(lignes_numerique[1]):
		return (False, "Nombre de lignes de briques incorrect.")
	lig = int(lignes_numerique[1])
	
	if len(lignes_numerique[2:]) != lig:
		return (False, "Nombre de lignes et lignes de briques non correspondant.")
		
	final = []
	for ligne in lignes_numerique[2:]:
		splited = ligne.split(" ")
		if len(splited) != col:
			return (False, "Pas assez de briques dans une ligne.")
		final.append(splited)
	
	return (final, "")
	
	
def verif_highscore_file():
	"""Cette fonction lancée au début du programme vérifie si le fichier des scores existe,
       si c'est le cas elle vérifie qu'il est correct et dans le cas contraire il est recréé à vide."""
       
	renew = False
	
	if not os.path.isfile(C.SCORE_PATH):
		renew = True
	
	else:
		with open(C.SCORE_PATH, "r") as scoreF:
			first_line = scoreF.readline()
			if first_line != C.SCORE_FIRST_LINE:
				renew = True
			
			else:
				for line in scoreF:
					line_sep = line.split("#")
					if len(line_sep) != 5 or line_sep[0] != "":	
						renew = True
						break
					
	
	if renew:
		with open(C.SCORE_PATH, "w") as scoreF:
			scoreF.write(C.SCORE_FIRST_LINE)
			return False
	return True
		
		
def add_score(player, score, temps):
	"""Ajoute un score de la forme #player#date#temps#score\n au fichier des scores."""
	
	verif_highscore_file()
	with open(C.SCORE_PATH, "a") as scoreW:
		date = str(datetime.date.today())
		scoreW.write('#'+player+'#'+date+'#'+str(temps)+'#'+str(score)+'\n')
		
		
def read_score():
	"""Renvoie une liste de liste de chaque score."""
	
	scores = []
	verif_highscore_file()
	
	with open(C.SCORE_PATH, 'r') as scoreR:
		for line in scoreR:
			if line[0] == "#":
				scores.append(line.split("#")[1:])
	return scores
	
