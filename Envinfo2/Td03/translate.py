#!/usr/bin/python3

import re
import os
import sys
import time

arg =  "-q -O index.html -U 'Mozilla/5.0 (X11; U; Linux i686; rv:1.8.1.6) Gecko/20070802 SeaMonkey/1.1.4'"

def get_url(text):
	text = re.sub(" ", "%20", text)
	url = "http://translate.google.com/translate_t?text={}&langpair=en|fr".format(text)
	print(url)
	return(url)

def main():
	a = 0
	if len(sys.argv) == 1:
		print("Not enough argument")
		return
	elif len(sys.argv) > 2:
		print("Too much argument")
		return

	url = get_url(sys.argv[1])

	if os.path.exists("index.html"):
		os.remove("index.html")
	print("wget {} {}".format(arg,url))
	os.system("wget {} {}".format(arg,url))

	time.sleep(0.5)
	#f = open("index.html","r")
	#for line in f:
	#	if re.search("TRANSLATED_TEXT='.*'",line):
	#		print(line[:-1])
main()
