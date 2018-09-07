#!/usr/bin/python3

import re,sys

def convert(filename):
	f = open(filename,"r")
	content = f.readlines()
	f.close()
	p = False
	for i in range(len(content)):
		content[i] = re.sub("&","&amp",content[i])
		content[i] = re.sub("<","&lt",content[i])
		content[i] = re.sub(">","&gt",content[i])
		if content[i] == "\n":
			if p == False:
				content[i] = "<p>\n"
			else :
				content[i] = "</p>\n"
			p = not p
		if content[i][0] == "#":
			content[i] = ""

		content[i] = re.sub("\*\*(((?!\*\*).)*)\*\*","<b>\\1</b>",content[i])	#Pour le gras
		content[i] = re.sub("~~(((?!~~).)*)~~","<i>\\1</i>",content[i])			#Pour l'italique
		content[i] = re.sub("__(((?!__).)*)__","<u>\\1</u>",content[i])			#Pour souligner
		content[i] = re.sub("\$\$(((?!\$\$).)*)\$\$","<u>\\1</u>",content[i])	#Pour important
		content[i] = re.sub("====","<hr>",content[i])							#Pour ligne de separation

	for line in content:
		print(line,end="")

def main():
	if len(sys.argv) < 2:
		print("Not enough argument")
		return
	for name in sys.argv[1:]:
		convert(name)

main()
