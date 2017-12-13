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
	for i in range(len(allumettes)):
		if allumettes[i] > 0:
			return(False)
	return(True)

def clique(x,y):
	global allumettes,last_player_pick,player_stack,bot_pick

	X = len(RULES)
	victory = checkVictory(allumettes)
	l = WIDTH*0.4
	if victory:
		return

	for i in range(len(allumettes)):
		if y > i*150-200 and y < (i+1)*150-200:
			player_stack = i

	if y <= -HEIGHT*0.5 and y >= -HEIGHT*0.9:
		for i in range(X):
			x1,x2 = l*((2*i/X)-1),l*((2*(i+1)/X)-1)
			if x > x1 and x < x2 and allumettes[player_stack] > 0:

				last_player_pick = RULES[i]
				allumettes[player_stack] -= last_player_pick

				bot_pick = bot.play(allumettes)
				if not checkVictory(allumettes):
					allumettes[bot_pick[0]] -= bot_pick[1]
					if checkVictory(allumettes):
						victory = "Bot"
				else :
					victory = "Player"
	clear()
	draw_interface(allumettes,last_player_pick,bot_pick[1],RULES,player_stack,victory)


screen = turtle.getscreen()
draw_interface(allumettes,last_player_pick,bot_pick[1],RULES,player_stack)
screen.onclick(clique)
turtle.mainloop()
