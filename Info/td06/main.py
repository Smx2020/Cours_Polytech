####	Exercice_1

l = ["fraise","kiwi",[12,34,56],5.34,"bonjour"]

print(l[1])
print(l[2])
print([l[1],l[2]])
print([l[3],l[4]])

l.insert(2,"pomme")
print(l)
l.append("adieu")
print(l)

####	Exercice_2

def Moyenne(L):
	S = 0
	for value in L:
		S += value
	return(S/len(L))

print(Moyenne([12,12,15,20,5]))

####	Exercice_3

def Moyenne_Coeff(N,C):
	S = 0
	C_total = 0
	i = 0
	while i < len(N):
		S += N[i]*C[i]
		C_total += C[i]
		i += 1
	return(S/C_total)

def get_rekt_kiddo(S,T="int"):
	out = []
	S = S.split(" ")
	for value in S:
		if T == "float":
			out.append(float(value))
		elif T == "int":
			out.append(int(value))
	return(out)

go = True
while go:
	print("calcul d'une moyenne pondérée")
	print("donner les notes et les coefficients dans le même ordre")
	Notes = input("les notes:")
	Coeff = input("les coefficients:")
	M = Moyenne_Coeff(get_rekt_kiddo(Notes,"float"),get_rekt_kiddo(Coeff))
	print("la moyenne pondérée est ",M)
	go = (True if input("encore ? ") == "o" else False)

####	Exercice_4

def Tri(L):
	if len(L) == 1:
		return(L)
	condition = True
	while condition:
		i = 1
		condition = False
		while i < len(L):
			if L[i-1] > L[i]:
				c = L[i-1]
				L[i-1] = L[i]
				L[i] = c
				condition = True
			i += 1
	return(L)

def Mex(L):
	L = Tri(L)
	i = 0
	while 42 :
		condition = True
		for value in L:
			if i == value:
				condition = False
		if condition:
			return(i)
		i += 1

####	Exercice_5

def Add(L,j):
	if len(L) == 0:
		return([j])
	for i in range(len(L)):
		if j <= L[i]:
			L.insert(i,j)
			return(L)
	L.append(j)
	return(L)

####	Exercice_6

def Merge(L1,L2):
	i = 0
	j = 0
	out = []
	condition = True
	while condition:

		if i >= len(L1) and j >= len(L2):
			condition = False
		elif i >= len(L1):
			out.append(L2[j])
			j += 1
		elif j >= len(L2):
			out.append(L1[i])
			i += 1

		elif L1[i] == L2[j] :
			out.append(L1[i])
			out.append(L1[i])
			i += 1
			j += 1
		elif L1[i] < L2[j]:
			out.append(L1[i])
			i += 1
		else :
			out.append(L2[j])
			j += 1

	return(out)
