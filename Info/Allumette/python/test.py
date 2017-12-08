import graphic,bot
from rules import *
START = 16

def clique(x,y):
	print("TEST")
	if y > -HEIGHT*0.5 or y < -HEIGHT*0.9:
		return
	l = WIDTH*0.4
	for i in range(X):
		x1,x2 = l*((2*i/X)-1),l*((2*(i+1)/X)-1)
		if x > x1 and x < x2:
			if myTurn :
				allumettes = allumettes - RULES[i]
				last_player_pick = RULES[i]
				myTurn = not myTurn

myTurn = True
allumettes = START
last_player_pick = 0
last_bot_pick = 0
graphic.draw_interface(allumettes,last_player_pick,last_bot_pick,RULES)

while allumettes > 0:

	if not myTurn :
		last_bot_pick = bot.play(allumettes)
		print("Bot :",last_bot_pick)
		allumettes -= last_bot_pick
		graphic.clear()
		graphic.draw_interface(allumettes,last_player_pick,last_bot_pick,RULES)
		myTurn = not myTurn

if not myTurn:
	victory_player = "Joueur"
else :
	victory_player = "Bot"

print("Victoire de", victory_player, "!")
