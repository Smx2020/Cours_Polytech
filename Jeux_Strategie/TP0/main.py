##############################################################################
#                                                                            #
#                                                        :::      ::::::::   #
#   main.py                                            :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: olivier <olivier@doussaud.org>             +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2018/03/13 18:39:49 by olivier           #+#    #+#             #
#   Updated: 2018/03/13 19:16:32 by olivier          ###   ########.fr       #
#                                                                            #
##############################################################################
R = 1
B = -1

def get_2_pow(x):
	value = 1
	i = 0
	while x != value :
		value = value*0.5
		i += 1
	return(i)

def afficheTour(lst):
	out = ""
	for value in lst:
		if value == R :
			out = out + "R"
		else :
			out = out + "B"
	return(out)

def valTour(tour):
	#Cas limite
	if tour == "":
		return(0)
	elif tour == "R":
		return(R)
	elif tour == "B":
		return(B)

	#s'occupe des premieres allumettes de meme couleur
	i = 1
	value = (R if tour[0] == "R" else B)
	while i < len(tour) and tour[i] == tour[i-1]:
		if tour[i] == "B":
			value += B
		else :
			value += R
		i += 1

	#s'occupe des allumettes restantes
	temp = 1/2
	for letter in tour[i:]:
		if letter == "R":
			value += temp*R
		else :
			value += temp*B
		temp = temp * 0.5

	return(value)

def floor(x):
	y = 0
	while abs(x - y) >= 1 or x < y:
		if x - y > 0 :
			y = y + 1
		else :
			y = y - 1
	return(y)

def construitTour(game_value,epsilon):
	tour = ""
	value = 0
	while floor(game_value-value) != 0 :
		if value > game_value:
			tour = tour + "B"
			value += B
		else :
			tour = tour + "R"
			value += R

	temp = 1/2
	while abs(game_value - value) > epsilon :
		if game_value > value:
			value += temp*R
			tour = tour + "R"
		else :
			value += temp*B
			tour = tour + "B"
		temp = temp * 0.5

	return(tour)


print(construitTour(-1.99,0.0001))
print(construitTour(+1.99,0.0001))
