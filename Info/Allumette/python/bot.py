from rules import *

WIN=1
LOST=-1
result = {}

def f(allu, myTurn=False):
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

def play(allu):
	for value in RULES:
		if f(allu-value) == WIN:
			return(value)
	return(1)
