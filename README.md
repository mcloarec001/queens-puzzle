# queens-puzzle

## Execution

Les librairies à installer sont dans le fichier `requirements.txt`. 
Pour executer le code il faut lancer le fichier `main.py` en le modifiant pour réaliser la tâche souhaitée, comme indiqué ci-dessous.

### Paramètres
Les paramètres sont au début du fichier `main.py`, ils peuvent être modifiés.
 - GRID_SIZE : la taille de la grille, le problème classique est de taille 8*8 mais il est possible de tester des plus grandes tailles
 - NB_MAX_TRIES : le nombre maximum d'essais pour une simulation
 - NB_HPT : le nombre de paramètres à tester, pour la probabilité de choisir la dame à bouger de façon aléatoire, et la probabilité de réaliser des mouvements aléatoires

### Fonctions
A la fin du fichier `main.py`, il faut passez en comment/uncomment pour n'éxecuter qu'une seule des trois fonctions
- Find one solution : trouve juste une solution et l'affiche
- Find many solutions : bouge les dames autant de fois qu'autorisé et retient les différentes solutions trouvés
- Hyperparameter tuning : lance des simulations pour différentes valeurs des paramètres de probabilité, afin de voir lesquelles sont optimales

## Analyse

L'analyse est disponible dans le rapport annexe. 