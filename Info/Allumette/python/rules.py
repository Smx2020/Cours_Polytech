##############################################################################
#                                                                            #
#                                                        :::      ::::::::   #
#   rules.py                                           :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: Enzo ISNARD, Olivier DOUSSAUD              +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2017/04/12 09:50:30                    #+#    #+#               #
#   Updated: 2018/01/10 09:13:38                   ###   ########.fr         #
#                                                                            #
##############################################################################

from random import randint
def inside(x,L):
	for value in L:
		if value == x:
			return(True)
	return(False)

START = [10,10,10]
RULES = [1,1,1]
i = 0
Lenght = randint(2,4)
#while i < Lenght:
#	x = randint(1,7)
#	if x not in RULES:
#		RULES.append(x)
#		x += 1

print(RULES)
