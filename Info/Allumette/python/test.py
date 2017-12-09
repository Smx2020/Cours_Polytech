import bot
from graphic import *
from rules import *
from random import randint
import time

START = randint(1,20)
global allumettes
allumettes = START
last_player_pick = 0
last_bot_pick = 0

def clique(x,y):
	X = len(RULES)
	global allumettes
	victory = False
	if allumettes <= 0:
		return

	if y > -HEIGHT*0.5 or y < -HEIGHT*0.9:
		return
	l = WIDTH*0.4
	for i in range(X):
		x1,x2 = l*((2*i/X)-1),l*((2*(i+1)/X)-1)
		if x > x1 and x < x2:

			last_player_pick = RULES[i]
			allumettes = allumettes - last_player_pick

			last_bot_pick = bot.play(allumettes)
			if allumettes > 0:
				allumettes = allumettes - last_bot_pick
				if allumettes <= 0:
					victory = "Bot"
			else :
				victory = "Player"
			clear()
			draw_interface(allumettes,last_player_pick,last_bot_pick,RULES,victory)


screen = turtle.getscreen()
draw_interface(allumettes,last_player_pick,last_bot_pick,RULES)
screen.onclick(clique)

turtle.mainloop()
