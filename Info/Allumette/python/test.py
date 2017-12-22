import bot
from graphic import *
from rules import *
from random import randint
import time

START = [36,36,36]
allumettes = START
last_player_pick = 0
bot_pick = [0,0]
player_stack = 1

def checkVictory(allumettes):
	"Verifie si le je est finis"
	for i in range(len(allumettes)):
		if allumettes[i] > 0:
			return(False)
	return(True)

def smooth(allumettes):
	"Met les allumettes negative a 0"
	for i in range(len(allumettes)):
		if allumettes[i] < 0:
			allumettes[i] = 0

def play(i) :
	"Joue le tour en cours"
	global last_player_pick,allumettes,bot_pick,player_stack
	victory = False

	last_player_pick = RULES[i]
	allumettes[player_stack] -= last_player_pick

	bot_pick = bot.play(allumettes)
	if not checkVictory(allumettes):
		allumettes[bot_pick[0]] -= bot_pick[1]
		if checkVictory(allumettes):
			victory = "Bot"
	else :
		victory = "Player"
	return(victory)

def clique(x,y):
	"Fonction lance au clique de la souris"
	global allumettes,last_player_pick,player_stack,bot_pick

	X = len(RULES)
	#Verifie si le jeu est termine
	victory = checkVictory(allumettes)
	l = WIDTH*0.4

	#Si le jeu est termine il ne faut rien modifier
	if victory:
		return

	#Choix du tas d'allumettes du joueur
	for i in range(len(allumettes)):
		if y > i*150-200 and y < (i+1)*150-200:
			player_stack = i

	#Choix du nombre d'allumettes et passage du tour
	if y <= -HEIGHT*0.5 and y >= -HEIGHT*0.9:
		for i in range(X):
			x1,x2 = l*((2*i/X)-1),l*((2*(i+1)/X)-1)
			if x > x1 and x < x2 and allumettes[player_stack] > 0:
				victory = play(i)

	#met a 0 si il y a un nombre d'allumettes negatif
	smooth(allumettes)
	#Rafraichi l'affichage
	clear()
	draw_interface(allumettes,last_player_pick,bot_pick[1],RULES,player_stack,victory)
	draw_background()


screen = turtle.getscreen()
draw_interface(allumettes,last_player_pick,bot_pick[1],RULES,player_stack)
draw_background()
screen.onclick(clique)
turtle.mainloop()
