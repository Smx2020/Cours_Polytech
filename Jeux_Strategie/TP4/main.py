#!/usr/bin/python3
from sys import *
from os import *



def generationSuivante(liste):
	out = []
	out.append(liste[0]-1)
	out.append(liste[0])
	for i in range(len(liste)-1):
		out.append((liste[i]+liste[i+1])/2)
		out.append(liste[i+1])
	out.append(liste[len(liste)-1]+1)
	return out


def arbre(n):
	out = [0]
	for i in range(n):
		out = generationSuivante(out)
	return out

def get_2_pow(x):
	if x == int(x):
		return(str(x))
	value = 1
	i = 0
	while int(x/value) != x/value :
		value = value*0.5
		i += 1
	if i < 5:
		return("{}/{}".format(int(x/value),2**i))
	return("{}/2^{}".format(int(x/value),i))


def pprint(tab):
	for i in range(len(tab)):
		print(get_2_pow(tab[i]),end="")
		if i != len(tab)-1:
			print(", ",end="")
	print()
n = argv[1]

arbre = arbre(int(n))
pprint(arbre)
#print(len(arbre))
