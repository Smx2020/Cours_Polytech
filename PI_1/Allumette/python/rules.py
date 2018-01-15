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
	"Verifie si x est dans L"
	for value in L:
		if value == x:
			return(True)
	return(False)

START = []
RULES = []

i = 0
Lenght = randint(2,4)
while i < Lenght:
	x = randint(1,7)
	if not inside(x,RULES):
		RULES.append(x)
		i += 1
RULES.sort()

for i in range(randint(1,3)):
	START.append(randint(10,36))
