#!/usr/bin/python3

import re
import sys

def main():
	for line in sys.stdin:
		print(re.sub(sys.argv[1],sys.argv[2],line),end="")


main()
