print("quotient de {0} par {1}: {2}".format(3124,6,3124 // 6))
print("reste de {0} par {1}: {2}".format(3124,6,3124 % 6))
print("type de 123*(1.56 -3): {0}".format(type(123*(1.56 -3))))
print("valeur de 123*(1.56 -3): {0}".format(123*(1.56 -3)))


def pizza(n):
	print("Pate à pizza pour {0} personnes".format(n))
	print("farine {0} g, sel {1} c. à cafè, levure {2} sachet, huile d'olive {3} c. à soupe, eau tiède {4} cl".format((350/4)*n,(2/4)*n,(1/4)*n,(3/4)*n,(25/4)*n))

def quo_e(v1,v2,i = 0):
	if v1 < v2:
		print(i)
		return(i)
	else :
		return(quo_e(v1-v2,v2,i+1))


def division(v1,v2):
	print("division euclidienne de {0} par {1} :".format(v1,v2))
	q = quo_e(v1,v2)
	print("{0} = {1} * {2} + {3}".format(v1, q, v2,v1 - q*v2))


def sq_name(L,l,name):
	for i in range(L):
		for i in range(l):
			print("*{0}".format(name),end = "")
		print()

pizza(4)
pizza(10)

division(83,4)

sq_name(4,4,"Olivier")

v1 = input("v1 = :")
v2 = input("v2 = :")
division(int(v1),int(v2))

name = input("nom = ")
sq_name(4,4,name)






def carre(v):
	return(x*x)
