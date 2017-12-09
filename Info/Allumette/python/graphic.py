import turtle


WIDTH, HEIGHT = turtle.screensize()
FONT_SIZE = 36
turtle.pensize(5)
turtle.speed(500)

TEST = 3
TEST2 = 1

def draw_rect(x1,y1,x2,y2):
	turtle.up()
	turtle.goto(x1,y1)
	turtle.down()
	turtle.goto(x2,y1)
	turtle.goto(x2,y2)
	turtle.goto(x1,y2)
	turtle.goto(x1,y1)

def draw_text(txt,x,y,font=FONT_SIZE):
	turtle.up()
	turtle.goto(x,y)
	turtle.down()
	turtle.write(txt,font=("Arial", font, "normal"))

def draw_pick_allumette(RULES):
	y1,y2 = -HEIGHT*0.5,-HEIGHT*0.9
	l = WIDTH*0.4
	X = len(RULES)
	for i in range(X):
		x1,x2 = l*((2*i/X)-1),l*((2*(i+1)/X)-1)
		draw_rect(x1,y1,x2,y2)
		draw_text(RULES[i],x1+0.5*l/X,y1*1.6)


def draw_interface(allu,pick_player,pick_bot,RULES,victory=False):
	if victory:
		draw_text("Victoire de " + victory,-WIDTH*.5,0)
		return
	#Terrain de jeu
	draw_rect(-WIDTH,HEIGHT,WIDTH,-HEIGHT*0.4)
	draw_text("|"*allu,-WIDTH*0.95,-HEIGHT*0.2,font=110)		#	Max 20
	draw_text(str(allu),-WIDTH*0.20,HEIGHT*0.45,font=110)

	#Le choix des allumettes
	draw_pick_allumette(RULES)

	#Boite Joueur
	draw_rect(-WIDTH,-HEIGHT,-WIDTH*0.6,-HEIGHT*0.6)
	draw_text("PLAYER",-WIDTH,-HEIGHT*0.6)
	draw_text(str(pick_player),-WIDTH*0.85,-HEIGHT*0.9)
	#Boite Bot
	draw_rect(WIDTH,-HEIGHT,WIDTH*0.6,-HEIGHT*0.6)
	draw_text("BOT",0.7*WIDTH,-HEIGHT*0.6)
	draw_text(str(pick_bot),WIDTH*0.8,-HEIGHT*0.9)


def clear():
	turtle.clear()

#m = input(" ")
