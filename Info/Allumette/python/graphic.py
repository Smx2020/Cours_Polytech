import turtle
from random import randint

WIDTH, HEIGHT = turtle.screensize()
WIDTH, HEIGHT = 600, 500

MONEY = "$" + str(randint(10,99)) + " " + str(randint(100,999)) + "$"
FONT_SIZE = 36
sizePlayer = 350
sizeBot = 350
turtle.pensize(5)
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)

def draw_tube(x,y,taille,color):

	turtle.up()
	turtle.goto(x,y)
	turtle.down()
	turtle.goto(x,y+taille)
	turtle.goto(x,y)
	turtle.goto(x+taille/4,y)
	turtle.goto(x+taille/4,y+taille)
	turtle.goto(x+taille/4,y+taille/2)
	turtle.begin_fill()
	turtle.fillcolor(color)
	turtle.goto(x,y+taille/2)
	turtle.goto(x,y)
	turtle.goto(x+taille/4,y)
	turtle.goto(x+taille/4,y+taille/2)
	turtle.end_fill()

def draw_tube_serie(x,y,n,taille):
	if n > 0:
		draw_tube(x,y,taille,"green")
	for i in range(1,n):
		draw_tube(x+i*taille/3,y,taille,"purple")


def	draw_man(x,y,taille,tilt=0):
	#turtle.settiltangle(0)
	turtle.up()
	turtle.goto(x,y)
	turtle.seth(tilt)
	turtle.down()
	#tete
	turtle.circle(taille/8)
	turtle.right(90)
	#corps
	turtle.forward(taille/4)
	#jambes
	turtle.left(35)
	turtle.forward(taille/6)
	turtle.backward(taille/6)
	turtle.right(70)
	turtle.forward(taille/6)
	turtle.backward(taille/6)
	turtle.left(35)
	#bras
	turtle.backward(taille/6)
	turtle.left(40)
	turtle.forward(taille/6)
	turtle.backward(taille/6)
	turtle.right(80)
	turtle.forward(taille/6)

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


def draw_interface(allu,pick_player,pick_bot,RULES,player_stack,victory=False):
	#Affiche si le jeu et finis que l'ecran de victoire
	if victory:
		if victory == "Player":
			draw_man(-WIDTH,0,sizePlayer)
			draw_man(WIDTH,0,sizeBot,270)
		else :
			draw_man(-WIDTH,0,sizePlayer,90)
			draw_man(WIDTH,0,sizeBot)
		draw_text("Victoire de " + victory,-WIDTH*.75,-50,80)
		return
	#Terrain de jeu
	draw_rect(-WIDTH,HEIGHT,WIDTH,-HEIGHT*0.4)
	for i in range(len(allu)):
		draw_tube_serie(-WIDTH*0.95,-HEIGHT*0.2*(-1.5*i+1)-HEIGHT*0.18,allu[i],80)
		draw_text(str(allu[i]),WIDTH*0.75,-HEIGHT*0.2*(-1.5*i+1)-HEIGHT*0.2,font=80)
		if i == player_stack :
			draw_text("_",WIDTH*0.75,-HEIGHT*0.2*(-1.5*i+1)-HEIGHT*0.2,font=80*2)

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

	#Affiche le background
	draw_man(WIDTH-100,HEIGHT*0.8,sizeBot)
	draw_man(-WIDTH+100,HEIGHT*0.8,sizePlayer)
	draw_text(MONEY,-WIDTH*0.7,HEIGHT-200,150)


def reduce_size(pick_player,pick_bot):
	global sizeBot,sizePlayer
	sizePlayer -= pick_player*3
	sizeBot -= pick_bot*3

def clear():
	turtle.clear()

#m = input(" ")
