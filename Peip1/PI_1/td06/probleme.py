####	Exercice_1

def get_rekt_kiddo(S,T="int"):
	out = []
	S = S.split(" ")
	for value in S:
		if T == "float":
			out.append(float(value))
		elif T == "int":
			out.append(int(value))
	return(out)

def Produit_Ligne(L,Vect):
	out = 0
	for i in range(len(Vect)):
		out += L[i]*Vect[i]
	return(out)

def Produit_Mat(Mat,Vect):
	out = []
	for i in range(len(Mat)):
		out.append(Produit_Ligne(Mat[i],Vect))
	return(out)

#go = True
#while go:
#	print("Produits matriciel")
#	Y = int(input("nb lignes de la matrice "))
#	X = int(input("nb colonnes de la matrice "))
#	print("lecture d'une matrice d'entiers de taille ( {} , {} )".format(Y,X))
#	Mat = [[] for j in range(Y)]
#	for i in range(Y):
#		Mat[i] = get_rekt_kiddo(input("ligne de taille {} :".format(X)))
#	Vect = get_rekt_kiddo(input("vecteur d'entiers de taille {} :".format(X)))
#	print("le produit est:  ",Produit_Mat(Mat,Vect))
#	go = (True if input("encore ? ") == "o" else False)
#

####	Exercice_2

def pascalFonction(L):
	out = [1]
	for i in range(1,len(L)):
		out.append(L[i]+L[i-1])
	out.append(1)
	return(out)

print(pascalFonction([1,4,6,4,1]))

####	Exercice_3
import random

def permute(L):
	r = random.randint(0,len(L))
	out = ""
	for i in range(len(L)):
		out = out + L[(i+r)%len(L)]
	return(out)

####	Exercice_4

def disp_classe(C):
	for i in range(len(C)):
		print(C[i][0],C[i][1])

def moyenne(C):
	out = 0
	for i in range(len(C)):
		out += C[i][2]
	return(out/len(C))

def major(C):
	maxi = 0
	for i in range(len(C)):
		if C[maxi][2] < C[i][2]:
			maxi = i
	return(C[maxi][0]+C[maxi][1])

Classe = [["Pd","Connard",20],["Bidet","Raclure",0],["Moyen","Moyen",10]]
#go = True
#while go:
#	print("Voulez-vous :\n1. afficher les élèves\n2. calculer la moyenne de la classe\n3. trouver le major de promo\n4. sortir")
#	n = int(input("votre choix : "))
#	print()
#	if n == 1 :
#		disp_classe(Classe)
#	elif n == 2:
#		print("La moyenne de la classe est ",moyenne(Classe))
#	elif n == 3:
#		print("Le major de promo est",major(Classe))
#	else :
#		go = False
#	print("\n")

####	Exercice_5
import turtle
import random

def setup_dico():
	import os

	out = []
	line = "Pd"
	f = open("dicoFrancais.txt","r",encoding="ISO-8859-1")
	while line != "":
		line = f.readline()
		out.append(line)
	return(out)

def draw_letter(letter,x,y):
	turtle.up()
	turtle.goto(x*75 - width ,y)
	turtle.down()
	turtle.write(letter,font=("Arial",40,"normal"))

dic = setup_dico()
rng = random.randint(0,len(dic)-1)
word = dic[rng]
width = turtle.window_width()/2 - 10
n = len(word) - 1
go = True
used = []
print(word)
for i in range(n):
	draw_letter("_",i,-5)

while go :
	test = True
	while test:
		a = input("lettre :")
		if len(a) == 1:
			test = False
			for letter in used:
				if a == letter :
					test = True

	for i in range(n):
		if a == word[i]:
			draw_letter(a,i,0)
			used.append(a)
	if len(used) == n:
		go = False

####	Exercice_6

def disp_shop(shop):
	for CD in shop:
		if CD[4] > 0:
			print('"{}" by {} '.format(CD[0],CD[1]))

def search(shop,word,field):
	out = []
	for CD in shop:
		if CD[field] == word:
			out.append(CD)
	return(out)

def buy(Shop,nb,song,band):
	for CD in shop:
		if CD[1] == band and CD[0] == song :
			if CD[4] >= nb :
				CD[4] = CD[4] - nb
				print("Les {} cd de {} fais par {} ont bien ete commande".format(nb,song,band))
				return
			else :
				print("Desole nous avons que {} de ces CD".format(CD[4]))
				return
	print("Desole nous n'avons pas ce CD")
	return


Shop = [
["Suites violoncelle seul","Bylsma","classique",23.50,1],
["No love","Eminem","rap",25.60,5],
["J'appuie sur la gâchette","NTM","rap",13.50,10],
["Symphonie du nouveau monde","Dvorak","classique",30.70,1],
["Adieu tristesse","Arthur H.", "chanson francaise",15.2,10],
["Mister mystère","M","chanson francaise",25.2,3],
["Je dis M","M","chanson francaise",25.2,3],
["Pacific 231","Raphaël","chanson francaise",28.6,8]
]

go = True
while go :
	print("Que voules vous faire :")
	print("[1]\tAfficher les CD disponible")
	print("[2]\tRechercher des CD")
	print("[3]\tAcheter des CD")
	print("[4]\tSortir")

	n = int(input("Votre choix: "))
	print("")
	if n == 1:
		disp_shop(Shop)
	elif n == 2 :
		print("Vous voulez rechercher selon :")
		print("[1]\tPar groupe ?")
		print("[2]\tPar type ?")
		opt = int(input("Votre choix: "))
		word = input("Vous recherchez quoi: ")
		print("")
		out = search(Shop,word,opt)
		if out == []:
			print("Aucun resultat")
		else :
			disp_shop(out)
	elif n == 3 :
		cd = input("Nom du CD: ")
		gr = input("Nom du groupe: ")
		nb = int(input("Nombre de CD voulue: "))
		buy(Shop,nb,cd,gr)
	elif n == 4:
		go = False
	else :
		print("Choix non reconnue")
