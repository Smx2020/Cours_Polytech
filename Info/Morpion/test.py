from tkinter import *

WIDTH = 4	#Largeur des traits

class OXO_Game(object):
	"Un jeux de OXO"

	def __init__(self,player_count=2,CASE_LENGHT=200,CASES=3):
		"Cree un jeu d'OXO classique ou avec les parametre donne"
		self.map = [[0 for k in range(CASES)] for i in range(CASES)]
		self.PLAYERS = player_count
		self.CASE_LENGHT = CASE_LENGHT
		self.CASES = CASES
		self.turn = 1
		self.victory = 0
		self.victory_player = 0

		self.window = Tk()
		c = CASE_LENGHT*len(self.map)
		self.screen = Canvas(self.window,height=c,width=c)
		self.screen.pack()

		self.window.bind("<Button 1>",self.getorigin)
		self.refreshGame()

	def getorigin(self,eventorigin):
		"Recupere le x et y du clique de souris"
		x = eventorigin.x // self.CASE_LENGHT
		y = eventorigin.y // self.CASE_LENGHT
		self.play(x,y)

	def drawCircle(self,x,y):
		"Dessine un cercle dans la case x,y"
		x1 = self.CASE_LENGHT*x + 0.1* self.CASE_LENGHT
		x2 = self.CASE_LENGHT*(x+1) - 0.1* self.CASE_LENGHT
		y1 = self.CASE_LENGHT*y + 0.1* self.CASE_LENGHT
		y2 = self.CASE_LENGHT*(y+1) - 0.1* self.CASE_LENGHT
		self.screen.create_oval(x1,y1,x2,y2,width=WIDTH)

	def drawSquare(self,x,y):
		"Dessine un carre dans la case x,y"
		x1 = self.CASE_LENGHT*x + 0.1* self.CASE_LENGHT
		x2 = self.CASE_LENGHT*(x+1) - 0.1* self.CASE_LENGHT
		y1 = self.CASE_LENGHT*y + 0.1* self.CASE_LENGHT
		y2 = self.CASE_LENGHT*(y+1) - 0.1* self.CASE_LENGHT
		self.screen.create_rectangle(x1,y1,x2,y2,width=WIDTH)

	def drawGrid(self):
		"Dessine la grille du jeu"
		l = self.CASE_LENGHT
		c = self.CASES
		for i in range(1,c):
			self.screen.create_line(0, l*i, c*l, l*i,width=WIDTH)
			self.screen.create_line(l*i, 0, l*i, c*l,width=WIDTH)

	def checkCase(self,x,y,map=False):
		"Verifie si la case est disponible"
		if map == False :
			map = self.map
		if map[y][x] == 0 :
			return(True)
		return(False)

	def checkLine(self,y):
		"Verifie si il a la condition de victoir dans la ligne y"
		value = self.map[y][0]
		if value == 0 :
			return(False)
		for j in range(len(self.map)):
			if value != self.map[y][j]:
				return(False)
		self.victory_player = value
		return(True)

	def checkColumn(self,x):
		"Verifie si il a la condition de victoir dans la colonne x"
		value = self.map[0][x]
		if value == 0 :
			return(False)
		for j in range(len(self.map)):
			if value != self.map[j][x]:
				return(False)
		self.victory_player = value
		return(True)

	def checkDiag(self, diag = 0):
		"Verifie si il a la condition de victoir dans la diagonales 1"
		l = len(self.map)
		value = self.map[diag*(-l+1)][0]
		if value == 0:
			return(False)
		for j in range(l):
			if value != self.map[(1+diag)*j+diag*(1+j-l)][j]:
				return(False)
		self.victory_player = value
		return(True)

	def checkEnd(self):
		"Verifie si la partie est finie"
		for i in range(len(self.map)):
			if self.checkColumn(i) or self.checkLine(i):
				self.victory = 1
				return
		if self.checkDiag() or self.checkDiag(-1):
			self.victory = 1
			return
		for i in range(self.CASES):
			for j in range(self.CASES):
				if self.map[i][j] == 0 :
					return
		self.victory = 2


	def changeTurn(self):
		"Passe le tour au prochain joueur"
		self.turn += 1
		if self.turn > self.PLAYERS:
			self.turn = 1

	def play(self,x,y):
		"Joue a la position x,y"
		if self.victory == 0 and self.checkCase(x,y):
			self.map[y][x] = self.turn
			self.changeTurn()
			self.checkEnd()
			self.bot()
			self.refreshGame()
			return(True)
		return(False)

	def refreshGame(self):
		"Reactualise l'ecran"
		self.screen.delete("all")
		self.drawGrid()
		for i in range(len(self.map)):
			for j in range(len(self.map)):
				if self.map[i][j] == 1:
					self.drawCircle(j,i)
				elif self.map[i][j] == 2:
					self.drawSquare(j,i)
		if self.victory != 0 :
			f = "Times {} bold".format(WIDTH*10)
			if self.victory == 1 :
				t = "Player {} win".format(self.victory_player)
			elif self.victory == 2 :
				t = "Draw"
			l = 0.5*self.CASE_LENGHT*self.CASES
			self.screen.create_text(l, l, fill="darkred", font=f, text=t)


	def start(self):
		"demarre le jeu"
		self.window.mainloop()


	def bot(self):
		map = self.map
		for y in range(3):
			for x in range(3):
				if self.checkCase(x,y):
					map[y][x] = 2
					if f(map) == WIN:
						return(x,y)
					map[y][x] = 0
		return(1)

def f(map, myTurn=False):
	condition = checkEnd(map)
	if condition == 1:
		return(LOST)
	elif condition == 2:
		return(WIN)
	for y in range(3):
		for x in range(3):
			if self.checkCase(x,y):
				if myTurn:
					map[y][x] = 2
				else :
					map[y][x] = 1
				if f(map, not myTurn) == WIN:
					return(WIN)
				map[y][x] = 0
	return(LOST)


a = OXO_Game()
a.start()
