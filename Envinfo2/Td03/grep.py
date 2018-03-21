#!/usr/bin/python3

import re
import sys

def main():
	for line in sys.stdin:
		if re.search(sys.argv[1],line):
			print(line,end="")

main()
