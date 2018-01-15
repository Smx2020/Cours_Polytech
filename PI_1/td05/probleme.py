####	Exercice_1

def capitalize(letter):
	mini = "abcdefghijklmnopqrstuvwxyz"
	maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	i = 0
	while i < 26:
		if letter == mini[i]:
			return(maj[i])
		i += 1
	return(letter)

def majusculise(texte):
	out = ""
	for i in range(len(texte)):
		if texte[i-1] == " " or texte[i-1] == "\t" or i == 0 :
			out = out + capitalize(texte[i])
		else :
			out = out + texte[i]
	return(out)

####	Exercice_2

def code(letter,c):
	dico = "abcdefghijklmnopqrstuvwxyz"
	for i in range(26):
		if letter == dico[i]:
			return(letter[(i+c)%26])
	return(letter)


def crypto1(texte, c):
	out = ""
	for i in range(len(texte)):
		out = out + code(texte[i],c)
	return(out)

####	Exercice_3

def code_str(lettre, clef):
	dico = "abcdefghijklmnopqrstuvwxyz"
	for i in range(26):
		if letter == dico[i]:
			return(clef[i])
	return(lettre)

def crypto2(texte, clef):
	out = ""
	for lettre in texte:
		out = out + code_str(lettre,clef)
	return(out)

####	Exercice_4

def audio_active(texte):
	out = ""
	i = 0
	while i < len(texte) :
		char = texte[i]
		j = 0
		while j+i < len(texte) and texte[i + j] == texte[i]:
			j += 1
		out = out + str(j) + texte[i]
		i += j
	return(out)

def suite_audio_active():
	maxi = int(input("combien de termes (>=2) ? "))
	temp = "1"
	print("terme 1 : ", 1)
	for i in range(maxi-1):
		temp = audio_active(temp)
		print("terme {} : {}".format(i+2,temp))

suite_audio_active()
