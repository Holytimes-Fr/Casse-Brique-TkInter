CASSE_BRIQUE Version 1.7 09/01/18
_________________________________________________________
 
À PROPOS
---------

Ce projet est une réalisation du célèbre jeu du casse brique
sorti en 1976, aussi connu sous le nom de 'Breakout'. 
Il a été réalisé dans le cadre des cours de programmation
Python lors de la première année de DUT INFORMATIQUE 
au campus de l'université Marne la Vallée par
Soudsada KOULABOUTH et William AMMOUIAL.

_________________________________________________________

RÈGLES DU JEU
-------------
Le jeu consiste à casser des briques (d'où son nom) 
alignées dans le haut de la fenêtre, en utilisant 
une balle qui traverse la zone de jeu et qui
rebondit sur les bords et le haut de la fenêtre. 
Le joueur possède une raquette, ici dirigeable à l'aide
des touches directionnelles de manière horizontale. Grâce à 
celles-ci, le joueur peut faire se déplacer la balle via
des rebonds, et faire en sorte que la balle touche 
les briques. Une fois touchée, la brique perd un point de
résistance et le joueur gagne un point.
On peut noter que si une brique possède une
résistance de 3 par exemple, il faudra au joueur toucher
cette brique 3 fois afin de la faire disparaître. Si il 
n'y a plus de briques, le joueur gagne, et si la balle ne
rebondit pas sur la raquette et tombe vers le bas de la
fenêtre, le joueur perd. 

__________________________________________________________ 

CONSIGNES DE BON DÉROULEMENT DU PROGRAMME
------------------------------------------

Ce programme peut être exécuté à l'aide de n'importe 
quel terminal, pourvu que l'ordinateur soit préalablement
équipé de python3 et de tkinter.
Vérifiez que 'Upemtk.py' soit bien situé dans le
dossier modules du programme. Ce dernier étant compris
dans le dossier compressé fourni, cela ne devrait pas 
être un problème.
Notez qu'il est possible de jouer en mode automatique
si vous souhaitez avoir un premier aperçu du jeu.
Pour cela il suffit lorsque vous lancez le jeu,
de sélectionner "Automatique" dans le menu qui va 
s'afficher
Aussi, il est possible de sélectionner des niveaux de jeu
créés à partir d'un fichier texte formaté d'une certaine 
manière.
Pour cela veuillez sélectionner "Charger un fichier" dans
le menu. Et par la suite de choisir le fichier nommé
"niv1" par exemple, qui correspond au niveau 1.
Le jeu se lance par la suite de lui-même en mode manuel.
Il n'est pas possible à ce jour de choisir un niveau pour
le mode automatique.

_________________________________________________________

ORGANISATION DU PROGRAMME
--------------------------

Le programme pour des questions de praticité et de 
lisibilité a été divisé en différents fichiers '.py'. 
Il y les fichiers 'affichage', 'collisions' , 'constantes'
, 'fichier', 'menu' et 'upemtk' contenus dans 
le dossier 'modules'.

'upemtk' est une bibliothèque graphique 
simplifiée utilisant le module tkinter fait par l'IUT de 
Champs-sur-Marne. 

'affichage' est le fichier qui contient toutes les 
fonctions ayant pour but de réaliser l'affichage du jeu,
que ce soit les briques, la balle, la raquette etc.

'collision' est un fichier contenant les fonctions 
propres aux différentes interactions qu'a la balle avec 
son milieu. Il contient par exemple les fonctions de 
vérification de la collision entre la balle et le mur, 
entre la balle et la raquette etc. 

'constantes' est le fichier qui contient toutes les 
valeurs fixes nécessaires au bon fonctionnement du programme.
C'est ici que sont stockées la taille des briques, de la
balle, taille de la fenêtre de jeu etc.
Comme ces valeurs sont utilisées dans tout le programme
il est plus facile de modifier les paramètres de ce
dernier en modifiant juste les valeurs des constantes. 

'fichier' est un fichier contenant les différentes 
fonctions nécessaires à la gestion des fichiers du jeu.
Notamment ceux des niveaux, des scores et des high scores.
Car en effet, une des fonctionnalités du jeu est de 
permettre au joueur d'enregistrer son score et de le 
consulter plus tard dans la partie 'High-scores' du menu
qui enregistre et affiche tous les scores des joueurs 
ainsi que d'autres informations telles que leur pseudo.

'menu' est le fichier qui contient toutes les fonctions
réalisant l'affichage de tous les différents menu du
jeu. Que ce soit le menu principal ou le menu des high
score par exemple. Il gère aussi les fonctions permettant
au joueur de sélectionner un choix dans le menu. 


Ensuite ses différents fichiers sont appelés dans le 
programme principal. 
Ce dernier contient lui aussi différentes fonctions 
telles que celles sur les mouvements : balle , raquette.
Et également celle pour le calcul du temps de jeu.
Et puis viennent les fonctions de jeu automatique et
manuelle.

Le corps principal du programme permet de rediriger le
joueur en fonction des choix qu'il effectue dans le menu.
Il peut choisir entre jouer lui-même ou en automatique.
Ainsi que de sélectionner un niveau ou visualiser les 
high scores. 
(Cf. CONSIGNES DE BON DÉROULEMENT DU PROGRAMME)



_________________________________________________________

EXPLICATION DES DIFFÉRENTS CHOIX FAITS
--------------------------------------

Choix graphique / esthétique : 

On retrouve les majeures fonctionnalités graphiques 
dans le fichier 'affichage' et 'menu'.
On peut noter que le jeu possède un certain style 'rétro'.
Que ce soit les couleurs vives ou la police.
C'est en partie afin de faire un rappel aux premiers jeux
d'arcades sortis qui avaient ce même type de design.
Des photos des étudiants ayant participé au projet ont
été ajoutées sur le menu principal.
Notez là qu'il s'agit d'une note humoristique afin de 
rendre plus 'original' l'affichage principal jeu. 

=============================================

Choix techniques : 

* Premièrement, concernant le mouvement de la balle.
On peut noter qu'ayant défini dès le début un vecteur 
vitesse [3,3] , on se retrouve avec un mouvement plutôt
régulier, ce qui donne une certaine monotonie. Et il 
est certain que c'est un mouvement loin d'être proche de
la réalité. Il aurait fallu implanter un facteur de 
hasard sur les valeurs du vecteur vitesse. Néanmoins il a
été considéré que le mouvement quelque peu répétitif 
de la balle n'empêchait en rien le bon déroulement 
du programme ni du jeu. 



* Le mur de brique : le mur est construit de telle 
manière à ce qu'on ait un mur 'virtuel' et 'physique'.
Pourquoi ? Et bien parce que on a dans un premier temps
les briques physiques, celles que l'on voit et qui ont
des couleurs etc. Et ensuite on a les briques dites
virtuelles composées de 1 , de 2 ou de 3. Nombres générés
de manière aléatoire. En fonction de leur résistance. 
Cela permet une modélisation plus simple lorsque l'on 
souhaite ajouter des fonctionnalités aux briques. 
Aussi, pour le moment les briques sont représentées sous 
forme d'une liste, bien qu'il aurait été possible de 
faire un dictionnaire. C'est un choix simplement 
pratique. 

_________________________________________________________

PROBLÈMES RENCONTRÉS 
---------------------

* Au cours de ce projet, différents problèmes ont fait 
surface. Notamment comme indiqué ci-dessus, le mouvement
de la balle. Ce problème reste à ce jour non résolu. 
En appliquant des formules de trigonométrie sur la 
raquette par exemple, c'est une idée. 
En la rendant 'arrondie' virtuellement afin que les 
rebonds de la balle sur la raquette soient un peu moins 
prévisibles. Car la raquette étant toute droite, cela 
fait que les rebonds sont symétriques par rapport à 
l'angle d'incidence. Du moins d'après le code de 
celle-ci.

* Aussi, on pouvait remarquer une inconsistance dans la
résistance des briques. En effet en mettant une 
résistance de 3 sur toutes les briques, on se retrouvait
avec des briques ayant tout de même une résistance de 2.
Bien que cela n'aurait pas dû être le cas.

* De plus, il y avait un problème avec la raquette qui
sortait à chaque fois de l'écran de jeu. Pas la raquette 
entière mais seulement 1/4. 

* Lorsqu'on essaye de lancer le jeu sur les machines de
l'IUT, la balle ralenti subitement et il est presque
impossible de jouer normalement, sans modifier et 
augmenter de beaucoup la vitesse initiale de la balle. 

_________________________________________________________

SOLUTIONS APPORTÉES & OPTIMISATION
----------------------------------

Suite aux problèmes rencontrés, des solutions ont été
apportées afin d'y remédier.

* Par exemple concernant l'inconsistance des résistances,
cela venait en réalité d'une condition qui dans la 
fonction de collision faisait que certaines briques 
étaient considérées comme ayant déjà été touchées alors 
que la partie n'avait pas encore débuté. Il fallait donc
juste modifier les conditions qui étaient erronées.

* Concernant le problème de la raquette, cela n'était en
soi pas si grave que ça pour le déroulement du jeu. 
Et le problème venant aussi des conditions dans la 
fonction de déplacement de la raquette, entre où et où 
elle doit se déplacer.
La fonction verif_outside_auto a ainsi été conçue afin de 
remédier à ce problème dans le mode automatique.
On peut donc comprendre cela comme
une optimisation dans le cas où cela a donné au jeu,
de meilleures conditions d'utilisation et de 
fonctionnement. 

* Le problème de la vitesse sur les machines de l'IUT
venait principalement du système d'affichage. Que ce soit
des briques ou de la zone d'information. En effet, au lieu
de ne s'afficher qu'une seule fois, ces derniers se 
réaffichaient de nouveau à chaque fois qu'une nouvelle 
boucle du jeu avait lieu. Ce qui ralentissait 
grandement la vitesse de la balle.
Ce contre temps a été résolu en mettant en place des 
fonctions qui indiquent les éléments à ne pas réafficher
à chaque fois (certains éléments de la zone d'info), 
prenez par exemple la fonction 'draw_init' du fichier 
'affichage'. Aussi, l'ajout de tag aux briques évite de 
réafficher sans cesse les briques non détruites. 

* Aussi concernant le déplacement de la balle, une 
fonction a été crée afin que lorsque la balle touche le
milieu de la raquette elle aille tout droit, et si elle
touche à droite elle va à droite et à gauche lorsqu'elle
touche le côté gauche de la raquette. En soit, le 
mouvement de la balle est toujours le même, mais 
cela ajoute un peu plus de dynamisme au jeu et donne 
de meilleures conditions de jeu, c'est plus agréable. 
Petit plus et nouvelle améliorations, maintenant lorsque
la balle touche des un coins extrême de la raquette, 
celle-ci augmente hautement sa vitesse. Une autre touche
permettant de rendre le jeu un peu moins prévisible.

_________________________________________________________

COMMENTAIRES
------------

Nous vous souhaitons un bon jeu. :)

_________________________________________________________

ECRIT AVEC
--------------

Python3

_________________________________________________________

MEMBRES DE L'ÉQUIPE
-------------------

William AMMOUIAL

Soudsada KOULABOUTH

