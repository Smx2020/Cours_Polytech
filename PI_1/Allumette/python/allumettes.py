##############################################################################
#                                                                            #
#                                                        :::      ::::::::   #
#   allumettes.py                                      :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: Enzo ISNARD, Olivier DOUSSAUD              +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2017/04/12 09:50:30                    #+#    #+#               #
#   Updated: 2018/01/10 09:13:38                   ###   ########.fr         #
#                                                                            #
##############################################################################


import bot
from graphic import *
from rules import *
import time

allumettes = START
last_player_pick = 0
bot_pick = [0,0]
player_stack = 0


def checkVictory(allumettes):
	"Verifie si le jeu est finis"
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

	#Si le jeu est termine il ne faut rien modifier
	if victory:
		return

	#Choix du tas d'allumettes du joueur
	for i in range(len(allumettes)):
		if y > i*150-200 and y < (i+1)*150-200:
			player_stack = i

	#Choix du nombre d'allumettes et passage du tour
	l = WIDTH*0.4
	if y <= -HEIGHT*0.5 and y >= -HEIGHT*0.9:
		for i in range(X):
			x1,x2 = l*((2*i/X)-1),l*((2*(i+1)/X)-1)
			if x > x1 and x < x2 and allumettes[player_stack] > 0:
				victory = play(i)
				reduce_size(RULES[i],bot_pick[1])

	#met a 0 si il y a un nombre d'allumettes negatif
	smooth(allumettes)
	#Rafraichi l'affichage
	clear()
	draw_interface(allumettes,last_player_pick,bot_pick[1],RULES,player_stack,victory)


screen = turtle.getscreen()
draw_interface(allumettes,last_player_pick,bot_pick[1],RULES,player_stack)

screen.onclick(clique)
turtle.mainloop()
