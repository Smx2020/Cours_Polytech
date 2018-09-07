def tete(s):
	if len(s) < 3:
		return(s)
	out = ""
	if s[0] == "e" and s[1] == "u" and s[2] == "h":
		out = out + tete(s[3:])
	else :
		out = out + s[0] + tete(s[1:])
	return out

print(tete("euh bonjoureuh salut"))
