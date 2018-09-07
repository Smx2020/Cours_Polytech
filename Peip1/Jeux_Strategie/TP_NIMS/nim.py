##############################################################################
#                                                                            #
#                                                        :::      ::::::::   #
#   nim.py                                             :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: olivier <olivier@doussaud.org>             +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2018/05/22 13:26:34 by olivier           #+#    #+#             #
#   Updated: 2018/05/28 16:30:13 by olivier          ###   ########.fr       #
#                                                                            #
##############################################################################


def mex(l):
	i = 0
	while i in l:
		i += 1
	return(i)

def strNim(n):
	if n == 0:
		return("0")
	elif n == 1:
		return("*")
	return("*"+str(n))

def decomposNim(n):
	return(list(range(n)))

def valStack(n,R):
	if n <= 0:
		return(0)

	l = []
	for i in R:
		l.append(valStack(n-i,R))
	return(mex(l))

def val(J,R):
	out = 0
	for value in J:
		out = sum(out,valStack(value,R))
	return(out)

def sumNim(a, b):
	a,b = min(a,b),max(a,b)
	if a == b:			#5
		return(0)

	if a == 1:			#2
		if b%2 == 0:
			return(b+1)
		else :
			return(b-1)

	if a == 2:
		if b%4 == 0:		#3
			return(b+2)
		elif b%4 == 2:
			return(b-2)

		elif b%4 == 1:	#4
			return(b+2)
		elif b%4 == 3:
			return(b-2)

	if a%2 == 0 and b%2 == 1:
		return(1)
	elif a%4 == 0 and b%4 == 2:
		return(2)
	elif a%4 == 1 and b%4 == 3:
		return(2)
	if a == 0:
		return(b)

def sum(a,b):

	if a == b:
		return(0)

	if a == 0 or b == 0:
		return(max(a,b))

	l = []

	for i in range(a):
		l.append(sum(b,i))

	for j in range(b):
		l.append(sum(a,j))

	return(mex(l))



#####################################_BOT_######################################

WIN=1
result = {}			#Stoque le nombre d'allumettes et si il est victorieux
LOST=-1

def f(allu, myTurn, R):
	"Donne si le nombre d'allumettes est gagnant ou non"
	if allu <= 0:
		return(LOST if myTurn else WIN)
	if allu in result :
		if myTurn == result[allu][1]:
			return(result[allu][0])
		else :
			return(-result[allu][0])
	if myTurn:
		for value in R:
			result[allu - value] = f(allu-value,not myTurn, R), not myTurn
			if result[allu - value][0] == WIN:
				return(WIN)
		return(LOST)
	else :
		for value in R:
			result[allu - value] = f(allu-value,not myTurn, R), not myTurn
			if result[allu - value][0] == LOST:
				return(LOST)
		return(WIN)

def play_one_stack(allu,R):
	"Le bot joue sur un tas d'allumettes"
	for value in R:
		if f(allu-value,False,R) == WIN:
			return(value)
	return(0)

########################################_/BOT_##################################

#for i in range(8):
#	for j in range(8):
#		print(i,j,"-->",sumNim(i,j),sum(i,j))
