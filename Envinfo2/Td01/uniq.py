#!/usr/bin/python3
import sys

def uniq(src):
	i = 0
	while i < len(src):
		c = 1
		while i+c < len(src) and src[i] == src[i+c] :
			c += 1
		print(c,src[i],end="")
		i += c

def main():
	if len(sys.argv) == 1:
		return
	elif len(sys.argv) > 2:
		print("Too much argument")
		return
	source = []
	f = open(sys.argv[1],"r")
	for line in f:
		source.append(line)
	f.close()
	uniq(source)
main()
