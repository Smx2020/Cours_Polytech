#!/usr/bin/python3

import sys
import os

def build_URL(adresse):
	out = "http://www.google.com/maps/place/"
	for i in range(len(adresse)):
		out = out + adresse[i]
		if i != len(adresse) - 1:
			out = out + "+"
	return(out)

def main():
	URL = "firefox " + build_URL(sys.argv[1:])
	os.system(URL)

main()
