from turtle import *
from random import *

# pour se déplacer sans écrire
def va(x,y) :
    up()
    goto(x,y)
    down()

# construit une grille g
# g est une liste de la forme [nbLigne,nbColonnes,largeur,hauteur,xbasG,ybasG]
def construitGrille(g) :
    nbLigne = g[0]
    nbColonne = g[1]
    largeur = g[2]
    hauteur = g[3]
    x = g[4]
    y = g[5]

    va(x,y)

    largeurLigne = largeur/nbLigne
    largeurColonne = hauteur/nbColonne

    x1=x
    y1=y

    # lignes verticales
    left(90)
    for i in range(0,nbColonne+1) :
        forward(largeur)
        x1=x1+largeurColonne
        va(x1,y)

    va(x,y)
    right(90)

    # lignes horizontales
    for i in range(0,nbLigne+1) :
        forward(hauteur)
        y1=y1+largeurLigne
        va(x,y1)


# calcule la position de (x,y) dans la grille g
def calculePosition(x,y,g) :
    xRelatif = x-g[4]
    yRelatif = y-g[5]
    largeurLigne = g[2]/g[0]
    largeurColonne = g[3]/g[1]
    return [yRelatif//largeurLigne,xRelatif//largeurColonne]

# calcule le point (bas,gauche) dans la fenêtre turtle associé
# à l'élément (i,j) de la grille
def calculeCoordonnee(i,j,g):
    largeurLigne = g[2]/g[0]
    largeurColonne = g[3]/g[1]
    return [g[4]+j*largeurColonne,g[5]+i*largeurLigne]

# localise le point (x,y) de la fenêtre turtle
# en fonction de sa position dans "grille"
def localiser(x,y):
	global turn
	va(x,y)
	color("black")
	if not estDedans(x,y,grille):
		write("dehors")
	else:
		position = calculePosition(x,y,grille)
		y = int(position[0])
		x = int(position[1])
		if lesObjets[y][x] != [] :
			return
		if turn == True:	#AAAAAARRRRRRRRRRRRRGGGGGGGGGG A mort les globales
			lesObjets[y][x] = ["carre","red"]
			turn = False
		else :
			lesObjets[y][x] = ["cercle","blue"]
			turn = True
		dessineObjets(lesObjets,grille)

# renvoie vrai si (x,y) est un point de la grille g
def estDedans(x,y,g) :
    return g[4]<=x and x<=g[4]+g[2] and g[5]<=y and y<=g[5]+g[3]

# dessine le carré point (bas,gauche) = (x,y), largeur l
def dessineCarre(x,y,l,c):
    va(x,y)
    color(c)
    begin_fill()
    for i in range(0,4):
        forward(l)
        left(90)
    end_fill()


# dessine le cercle centré dans le carré point (bas,gauche) = (x,y), largeur l
def dessineCercle(x,y,l,c):
    va(x+l/2,y)
    color(c)
    begin_fill()
    circle(l/2)
    end_fill()

# dessine les objets de la liste l dans la grille g
# les objets sont des carrés ou des triangles isoscelles avec une couleur
# PRECOND : l et g sont de taille compatible
def dessineObjets(l,g) :
	i=0
	for o1 in l:
		j=0
		for o2 in o1 :
			dessineObjet(i,j,o2,g)	#modification ici j,i avant
			j=j+1
		i=i+1

def dessineObjet(i,j,o,g):
    if not o==[]:
        coordonne = calculeCoordonnee(i,j,g)
        x = coordonne[0]
        y = coordonne[1]
        if o[0]=="carre" :
            dessineCarre(x,y,g[2]/g[0],o[1])
        else :
            dessineCercle(x,y,g[2]/g[0],o[1])


# programme principal
title("un jeu de grille")

maxX = window_width()//2-10
maxY = window_height()//2-10
speed(400)
# grille à 3 lignes, 3 colonnes, carré de 300x300 placé en (-100,-100)
grille = [3,3,300,300,-100,-100]
construitGrille(grille)
lesObjets = [
			[[],[],[]],
			[[],[],[]],
			[[],[],[]]
			]
dessineObjets(lesObjets,grille)
turn = True
# quand on clique n'importe où dans la fenêtre
# cela appelle la fonction localiser
sc=getscreen()
sc.onclick(localiser)
input("?")
