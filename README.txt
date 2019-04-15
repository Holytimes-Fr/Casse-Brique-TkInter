CASSE_BRIQUE Version 1.7 09/01/18
_________________________________________________________
 
� PROPOS
---------

Ce projet est une r�alisation du c�l�bre jeu du casse brique
sorti en 1976, aussi connu sous le nom de 'Breakout'. 
Il a �t� r�alis� dans le cadre des cours de programmation
Python lors de la premi�re ann�e de DUT INFORMATIQUE 
au campus de l'universit� Marne la Vall�e par
Soudsada KOULABOUTH et William AMMOUIAL.

_________________________________________________________

R�GLES DU JEU
-------------
Le jeu consiste � casser des briques (d'o� son nom) 
align�es dans le haut de la fen�tre, en utilisant 
une balle qui traverse la zone de jeu et qui
rebondit sur les bords et le haut de la fen�tre. 
Le joueur poss�de une raquette, ici dirigeable � l'aide
des touches directionnelles de mani�re horizontale. Gr�ce � 
celles-ci, le joueur peut faire se d�placer la balle via
des rebonds, et faire en sorte que la balle touche 
les briques. Une fois touch�e, la brique perd un point de
r�sistance et le joueur gagne un point.
On peut noter que si une brique poss�de une
r�sistance de 3 par exemple, il faudra au joueur toucher
cette brique 3 fois afin de la faire dispara�tre. Si il 
n'y a plus de briques, le joueur gagne, et si la balle ne
rebondit pas sur la raquette et tombe vers le bas de la
fen�tre, le joueur perd. 

__________________________________________________________ 

CONSIGNES DE BON D�ROULEMENT DU PROGRAMME
------------------------------------------

Ce programme peut �tre ex�cut� � l'aide de n'importe 
quel terminal, pourvu que l'ordinateur soit pr�alablement
�quip� de python3 et de tkinter.
V�rifiez que 'Upemtk.py' soit bien situ� dans le
dossier modules du programme. Ce dernier �tant compris
dans le dossier compress� fourni, cela ne devrait pas 
�tre un probl�me.
Notez qu'il est possible de jouer en mode automatique
si vous souhaitez avoir un premier aper�u du jeu.
Pour cela il suffit lorsque vous lancez le jeu,
de s�lectionner "Automatique" dans le menu qui va 
s'afficher
Aussi, il est possible de s�lectionner des niveaux de jeu
cr��s � partir d'un fichier texte format� d'une certaine 
mani�re.
Pour cela veuillez s�lectionner "Charger un fichier" dans
le menu. Et par la suite de choisir le fichier nomm�
"niv1" par exemple, qui correspond au niveau 1.
Le jeu se lance par la suite de lui-m�me en mode manuel.
Il n'est pas possible � ce jour de choisir un niveau pour
le mode automatique.

_________________________________________________________

ORGANISATION DU PROGRAMME
--------------------------

Le programme pour des questions de praticit� et de 
lisibilit� a �t� divis� en diff�rents fichiers '.py'. 
Il y les fichiers 'affichage', 'collisions' , 'constantes'
, 'fichier', 'menu' et 'upemtk' contenus dans 
le dossier 'modules'.

'upemtk' est une biblioth�que graphique 
simplifi�e utilisant le module tkinter fait par l'IUT de 
Champs-sur-Marne. 

'affichage' est le fichier qui contient toutes les 
fonctions ayant pour but de r�aliser l'affichage du jeu,
que ce soit les briques, la balle, la raquette etc.

'collision' est un fichier contenant les fonctions 
propres aux diff�rentes interactions qu'a la balle avec 
son milieu. Il contient par exemple les fonctions de 
v�rification de la collision entre la balle et le mur, 
entre la balle et la raquette etc. 

'constantes' est le fichier qui contient toutes les 
valeurs fixes n�cessaires au bon fonctionnement du programme.
C'est ici que sont stock�es la taille des briques, de la
balle, taille de la fen�tre de jeu etc.
Comme ces valeurs sont utilis�es dans tout le programme
il est plus facile de modifier les param�tres de ce
dernier en modifiant juste les valeurs des constantes. 

'fichier' est un fichier contenant les diff�rentes 
fonctions n�cessaires � la gestion des fichiers du jeu.
Notamment ceux des niveaux, des scores et des high scores.
Car en effet, une des fonctionnalit�s du jeu est de 
permettre au joueur d'enregistrer son score et de le 
consulter plus tard dans la partie 'High-scores' du menu
qui enregistre et affiche tous les scores des joueurs 
ainsi que d'autres informations telles que leur pseudo.

'menu' est le fichier qui contient toutes les fonctions
r�alisant l'affichage de tous les diff�rents menu du
jeu. Que ce soit le menu principal ou le menu des high
score par exemple. Il g�re aussi les fonctions permettant
au joueur de s�lectionner un choix dans le menu. 


Ensuite ses diff�rents fichiers sont appel�s dans le 
programme principal. 
Ce dernier contient lui aussi diff�rentes fonctions 
telles que celles sur les mouvements : balle , raquette.
Et �galement celle pour le calcul du temps de jeu.
Et puis viennent les fonctions de jeu automatique et
manuelle.

Le corps principal du programme permet de rediriger le
joueur en fonction des choix qu'il effectue dans le menu.
Il peut choisir entre jouer lui-m�me ou en automatique.
Ainsi que de s�lectionner un niveau ou visualiser les 
high scores. 
(Cf. CONSIGNES DE BON D�ROULEMENT DU PROGRAMME)



_________________________________________________________

EXPLICATION DES DIFF�RENTS CHOIX FAITS
--------------------------------------

Choix graphique / esth�tique : 

On retrouve les majeures fonctionnalit�s graphiques 
dans le fichier 'affichage' et 'menu'.
On peut noter que le jeu poss�de un certain style 'r�tro'.
Que ce soit les couleurs vives ou la police.
C'est en partie afin de faire un rappel aux premiers jeux
d'arcades sortis qui avaient ce m�me type de design.
Des photos des �tudiants ayant particip� au projet ont
�t� ajout�es sur le menu principal.
Notez l� qu'il s'agit d'une note humoristique afin de 
rendre plus 'original' l'affichage principal jeu. 

=============================================

Choix techniques : 

* Premi�rement, concernant le mouvement de la balle.
On peut noter qu'ayant d�fini d�s le d�but un vecteur 
vitesse [3,3] , on se retrouve avec un mouvement plut�t
r�gulier, ce qui donne une certaine monotonie. Et il 
est certain que c'est un mouvement loin d'�tre proche de
la r�alit�. Il aurait fallu implanter un facteur de 
hasard sur les valeurs du vecteur vitesse. N�anmoins il a
�t� consid�r� que le mouvement quelque peu r�p�titif 
de la balle n'emp�chait en rien le bon d�roulement 
du programme ni du jeu. 



* Le mur de brique : le mur est construit de telle 
mani�re � ce qu'on ait un mur 'virtuel' et 'physique'.
Pourquoi ? Et bien parce que on a dans un premier temps
les briques physiques, celles que l'on voit et qui ont
des couleurs etc. Et ensuite on a les briques dites
virtuelles compos�es de 1 , de 2 ou de 3. Nombres g�n�r�s
de mani�re al�atoire. En fonction de leur r�sistance. 
Cela permet une mod�lisation plus simple lorsque l'on 
souhaite ajouter des fonctionnalit�s aux briques. 
Aussi, pour le moment les briques sont repr�sent�es sous 
forme d'une liste, bien qu'il aurait �t� possible de 
faire un dictionnaire. C'est un choix simplement 
pratique. 

_________________________________________________________

PROBL�MES RENCONTR�S 
---------------------

* Au cours de ce projet, diff�rents probl�mes ont fait 
surface. Notamment comme indiqu� ci-dessus, le mouvement
de la balle. Ce probl�me reste � ce jour non r�solu. 
En appliquant des formules de trigonom�trie sur la 
raquette par exemple, c'est une id�e. 
En la rendant 'arrondie' virtuellement afin que les 
rebonds de la balle sur la raquette soient un peu moins 
pr�visibles. Car la raquette �tant toute droite, cela 
fait que les rebonds sont sym�triques par rapport � 
l'angle d'incidence. Du moins d'apr�s le code de 
celle-ci.

* Aussi, on pouvait remarquer une inconsistance dans la
r�sistance des briques. En effet en mettant une 
r�sistance de 3 sur toutes les briques, on se retrouvait
avec des briques ayant tout de m�me une r�sistance de 2.
Bien que cela n'aurait pas d� �tre le cas.

* De plus, il y avait un probl�me avec la raquette qui
sortait � chaque fois de l'�cran de jeu. Pas la raquette 
enti�re mais seulement 1/4. 

* Lorsqu'on essaye de lancer le jeu sur les machines de
l'IUT, la balle ralenti subitement et il est presque
impossible de jouer normalement, sans modifier et 
augmenter de beaucoup la vitesse initiale de la balle. 

_________________________________________________________

SOLUTIONS APPORT�ES & OPTIMISATION
----------------------------------

Suite aux probl�mes rencontr�s, des solutions ont �t�
apport�es afin d'y rem�dier.

* Par exemple concernant l'inconsistance des r�sistances,
cela venait en r�alit� d'une condition qui dans la 
fonction de collision faisait que certaines briques 
�taient consid�r�es comme ayant d�j� �t� touch�es alors 
que la partie n'avait pas encore d�but�. Il fallait donc
juste modifier les conditions qui �taient erron�es.

* Concernant le probl�me de la raquette, cela n'�tait en
soi pas si grave que �a pour le d�roulement du jeu. 
Et le probl�me venant aussi des conditions dans la 
fonction de d�placement de la raquette, entre o� et o� 
elle doit se d�placer.
La fonction verif_outside_auto a ainsi �t� con�ue afin de 
rem�dier � ce probl�me dans le mode automatique.
On peut donc comprendre cela comme
une optimisation dans le cas o� cela a donn� au jeu,
de meilleures conditions d'utilisation et de 
fonctionnement. 

* Le probl�me de la vitesse sur les machines de l'IUT
venait principalement du syst�me d'affichage. Que ce soit
des briques ou de la zone d'information. En effet, au lieu
de ne s'afficher qu'une seule fois, ces derniers se 
r�affichaient de nouveau � chaque fois qu'une nouvelle 
boucle du jeu avait lieu. Ce qui ralentissait 
grandement la vitesse de la balle.
Ce contre temps a �t� r�solu en mettant en place des 
fonctions qui indiquent les �l�ments � ne pas r�afficher
� chaque fois (certains �l�ments de la zone d'info), 
prenez par exemple la fonction 'draw_init' du fichier 
'affichage'. Aussi, l'ajout de tag aux briques �vite de 
r�afficher sans cesse les briques non d�truites. 

* Aussi concernant le d�placement de la balle, une 
fonction a �t� cr�e afin que lorsque la balle touche le
milieu de la raquette elle aille tout droit, et si elle
touche � droite elle va � droite et � gauche lorsqu'elle
touche le c�t� gauche de la raquette. En soit, le 
mouvement de la balle est toujours le m�me, mais 
cela ajoute un peu plus de dynamisme au jeu et donne 
de meilleures conditions de jeu, c'est plus agr�able. 
Petit plus et nouvelle am�liorations, maintenant lorsque
la balle touche des un coins extr�me de la raquette, 
celle-ci augmente hautement sa vitesse. Une autre touche
permettant de rendre le jeu un peu moins pr�visible.

_________________________________________________________

COMMENTAIRES
------------

Nous vous souhaitons un bon jeu. :)

_________________________________________________________

ECRIT AVEC
--------------

Python3

_________________________________________________________

MEMBRES DE L'�QUIPE
-------------------

William AMMOUIAL

Soudsada KOULABOUTH

