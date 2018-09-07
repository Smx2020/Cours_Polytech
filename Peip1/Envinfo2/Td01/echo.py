#!/usr/bin/python3
import sys

def print_reverse(l):
	if len(l) == 0:
		return
	print_reverse(l[1:])
	print(l[0])

def main():
	if len(sys.argv) == 1:
		return
	elif sys.argv[1] == "-r":
		print_reverse(sys.argv[2:])
	else :
		for arg in sys.argv[1:] :
			print(arg,end=" ")


# Appeler la fonction main
main()
