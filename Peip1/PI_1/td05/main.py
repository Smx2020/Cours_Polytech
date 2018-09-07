####	Exercice_1

mot = input("un mot ")
i=0
while i< len(mot):
	print(mot[i])
	i=i+2

####	Exercice_2

def nb_letter(phrase, letter):
	out = 0
	i = 0
	while i < len(phrase) :
		if phrase[i] == letter :
			out += 1
		i += 1
	return(out)

####	Exercice_3

def voyelle(l):
	voy = "eaiouy"
	i = 0
	while i < len(voy):
		if l == voy[i]:
			return(True)
		i += 1
	return(False)

####	Exercice_4

total_v = 0
total_l = 0
go = True
while go :
	phrase = input("Le texte : ")
	i=0
	nb_voy = 0
	while i< len(phrase):
		if voyelle(phrase[i]):
			nb_voy += 1
		i=i+1
	print("il y a {} voyelles dans {}".format(nb_voy,phrase))
	total_l += i
	total_v += nb_voy
	go = (True if input("encore ? o/n ") == "o" else False)
print("Au total, il y a {} voyelles parmi {} lettres".format(total_v,total_l))

###	Exercice_5

def deugueuIse(phrase):
	out = ""
	i = 0
	while i < len(phrase):
		if phrase[i] == "e":
			out = out + phrase[i] + "gu" + phrase[i]
		elif voyelle(phrase[i]) :
			out = out + phrase[i] + "g" + phrase[i]
		else :
			out = out + phrase[i]
		i += 1
	return(out)

####	Exercice_6

def nb_phrase_for(texte):
	out = 0
	for letter in texte :
		if letter == "." :
			out += 1
		elif letter == "?":
			out += 1
		elif letter == "!":
			out += 1
	return(out)

def nb_phrase_while(texte):
	out = 0
	i = 0
	while i < len(texte) :
		if texte[i] == "." :
			out += 1
		elif texte[i] == "?":
			out += 1
		elif texte[i] == "!":
			out += 1
		i += 1
	return(out)

####	Exercice_7

def nb_phrase(texte):
	out = 0
	point = 0
	for i in range(len(texte)):
		if texte[i] == "." :
			if point % 3 == 0:
				out += 1
			point += 1
		elif texte[i] == "?":
			out += 1
		elif texte[i] == "!":
			out += 1
		else :
			point = 0
	return(out)
