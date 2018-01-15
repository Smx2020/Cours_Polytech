##############################################################################
#                                                                            #
#                                                        :::      ::::::::   #
#   bot.py                                             :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: Enzo ISNARD, Olivier DOUSSAUD              +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2017/04/12 09:50:30                    #+#    #+#               #
#   Updated: 2018/01/10 09:13:38                   ###   ########.fr         #
#                                                                            #
##############################################################################

from rules import *

WIN=1
LOST=-1
result = {}			#Stoque le nombre d'allumettes et si il est victorieux

def f(allu, myTurn=False):
	"Donne si le nombre d'allumettes est gagnant ou non"
	if allu <= 0:
		return(LOST if myTurn else WIN)
	if allu in result :
		if myTurn == result[allu][1]:
			return(result[allu][0])
		else :
			return(-result[allu][0])
	if myTurn:
		for value in RULES:
			result[allu - value] = f(allu-value,not myTurn), not myTurn
			if result[allu - value][0] == WIN:
				return(WIN)
		return(LOST)
	else :
		for value in RULES:
			result[allu - value] = f(allu-value,not myTurn), not myTurn
			if result[allu - value][0] == LOST:
				return(LOST)
		return(WIN)

def play(allumettes):
	"Le bot joue sur les tas d'allumettes"
	for i in range(len(allumettes)):
		condition = play_one_stack(allumettes[i])
		if allumettes[i] > 0 and condition[0] == WIN :
			return(i,condition[1])
	return(0,RULES[0])


def play_one_stack(allu):
	"Le bot joue sur un tas d'allumettes"
	for value in RULES:
		if f(allu-value) == WIN:
			return(WIN,value)
	return(LOST,1)
