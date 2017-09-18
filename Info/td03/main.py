import random
from turtle import *
import time

####	Exercice_1

# Le programme boucle a l'infinis en affichant "1 fois 7 : 7"

####	Exercice_2

value = int(input("Quelle table voulez-vous reviser ? "))
max_value = int(input("Jusqu'a quelle valeur ? "))
print("Revision de la table de {} jusqu'a {}".format(value, max_value))
i = 1
while i <= max_value :
	print("{} fois {}  : {}".format(i, value, i * value))
	i += 1
print("fin de la revision")

####	Exercice_3

def factoriel(n) :
	return(1 if n == 0 else n * factoriel(n-1))

#La stack pete

####	Exercice_4

DIFFICULTY = 7
max_value = int(input("vous devez trouver un nombre compris entre 1 et "))
print("vous avez au plus {} tentatives".format(DIFFICULTY))
tentatives,nb = 0,-1
value = random.randint(1,max_value)

while tentatives < DIFFICULTY and nb != value:
	nb = int(input("le nombre ? "))
	if nb > value :
		print("trop grand")
	elif nb < value :
		print("trop petit")
	tentatives += 1
if nb == value :
	print("vous avez gagne en {} tentatives".format(tentatives))
else :
	print("Vous avez echoue")

####	Exercice_6

def polygone(cote, nb_sommets):
	i = 0
	while i < nb_sommets:
		forward(cote)
		right(360/nb_sommets)
		i += 1

cote = int(input("Longueur d'un cote :"))

polygone(cote,3)

####	Exercice_7
polygone(cote,4)

####	Exercice_8
polygone(cote,5)

####	Exercice_9

nb_petale = int(input("Nombre de petales :"))
i = 0
while i < nb_petale :
	polygone(100,4)
	right(360/nb_petale)
	i += 1
time.sleep(3)
