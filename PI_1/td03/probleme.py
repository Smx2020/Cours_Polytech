from turtle import *
import time
import math

####	Probleme_1

hauteur = window_height() # récupère la hauteur de la fenêtre
largeur = window_width()  # récupère la largeur de la fenêtre
pas = int(input("La hauteur de la marche ="))
x,y = -largeur/2,-hauteur/2
state = -1
i = 0
up()
speed(2000)
goto(x,y)
down()
write("arrivee")

while x < largeur/2 and y < hauteur/2 :
	if i >= pas :
		i = 0
		state = -state
		left(state * 90)
	if state == 1:
		x += 1
	else :
		y += 1
	forward(1)
	i += 1

write("depart")

####	Probleme_2

def factoriel(n) :
	return(1 if n == 0 else n * factoriel(n-1))

x = float(input("x dans [-Pi,Pi] :"))
epsilon = float(input("seuil d'arrêt (>0):"))

somme = 0
terme = x
i = -1
while abs(terme) > epsilon :
	i += 1
	terme = ((-1)**i) * (x**(2*i+1)) / (factoriel(2*i +1))
	somme += terme
print("résultat exact :",math.sin(x))
print("résultat approximé :",somme)
print("ordre du développement :",i)

####	Probleme_3

def polygone(cote, nb_sommets):
	i = 0
	while i < nb_sommets:
		forward(cote)
		right(360/nb_sommets)
		i += 1

goto(0,0)
nbPoly = int(input("le nombre de polygones"))
nbCote = int(input("le nombre de cotes du polygone (>3)"))
l =	int(input("la longueur des cotes du 1er polygone"))
f = int(input("un facteur"))
i = 0

while i < nbPoly :
	polygone(l,nbCote)
	i += 1
	l = l * (f/100)
	forward(l)
	right(360/nbCote)	#formule pour l'angle a
time.sleep(10)
