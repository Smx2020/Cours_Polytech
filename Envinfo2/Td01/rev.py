#!/usr/bin/python3
import os,sys

def reverse(txt):
	if len(txt) == 0:
		return
	reverse(txt[1:])
	if txt[0] != "\n":
		print(txt[0],end = "")

def rev(txt):
	reverse(txt)
	print("")

def main():
	if len(sys.argv) == 1:
		return
	elif len(sys.argv) > 2:
		print("Too much argument")
		return
	f = open(sys.argv[1],"r")
	for line in f:
		rev(line)
	f.close()

main()
