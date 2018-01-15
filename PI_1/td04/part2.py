####	Exercice_3

def dessinePolygone(nb_cote, l, x=0, y=0, couleur="blue"):
	"dessine un polygone regulier en x,y d'une certaine couleur"
	import turtle

	i = 0

	turtle.up()
	turtle.goto(x,y)
	turtle.color(couleur)
	turtle.down()

	while i < nb_cote:
		turtle.forward(l)
		turtle.left(360/nb_cote)
		i += 1

def dessineTriangle(l, x=0, y=0, couleur="blue"):
	dessinePolygone(3,l,x,y,couleur)

def dessineCarre(l, x=0, y=0, couleur="blue"):
	dessinePolygone(4,l,x,y,couleur)

####	Exercice_5

def table_de_multi(a,b=10):
	"affiche la table de a jusqu'a b"
	for i in range(1,b+1):
		print(i, " fois ", table, "  : ", table*i)

print("Révision des tables de multiplication")
go = True

while go :
	print("")
	table = int(input("Quelle table voulez-vous réviser ? "))
	maximum = int(input("Jusqu'à quel rang ? "))
	print("***************************")
	print("révision de la table de ", table, " jusqu'à ", maximum)
	table_de_multi(table,maximum)
	print("***************************")
	go = (True if input("Encore ? (o/n) ") == "o" else False)

####	Exercice_6

nbCote = int(input("le nombre de cotes du polygone (>3)"))
l =	int(input("la longueur des cotes du 1er polygone"))
nbPoly = int(input("le nombre de polygones"))
coeff = int(input("le coefficient :"))

x = 0
y = 0

for i in range(nbPoly):
	dessinePolygone(nbCote,l,x,y)
	x += l
	l = l*(1+coeff/100)
