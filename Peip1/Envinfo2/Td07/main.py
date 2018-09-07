#!/usr/bin/python3

import sys

class Picture(object):
	def __init__(self, pic="NULL"):
		if pic == "NULL":
			self.depth = 0
			self.width = 0
			self.height = 0
			self.p = []

		else :
			self.convert(pic)

	def convert(self,pic):
		"convertie et attribue image"
		f = open(pic,"r")
		s = f.readlines()
		f.close()
		temp = []
		i = 0
		for elt in s:
			a = elt[0:-1].split()
			if elt[0] != "#":
				for value in a:
					temp.append(value)
		if temp[0] != "P3":
			print("ERROR not the good format")


		self.depth = int(temp[3])
		self.width = int(temp[1])
		self.height = int(temp[2])

		temp = temp[4:]
		self.p = []
		for i in range(0,len(temp),3):
			t = []
			for j in range(3):
				t.append(int(temp[i+j]))
			self.p.append(t)


	def swap(self,co,sw):
		"change la couleur co en sw"
		for i in range(len(self.p)):
			if self.p[i] == co:
				self.p[i] = sw

	def negatif(self):
		"transforme l'image en son negatif"
		for i in range(len(self.p)):
			t = []
			for v in self.p[i]:
				t.append(self.depth - v)
			self.p[i] = t

	def B_and_W(self):
		"met l'image en noir et blanc"
		for i in range(len(self.p)):
			c = 0
			for j in range(3):
				c += self.p[i][j]
			c = int(c/3)
			self.p[i] = (c,c,c)

	def sepia(self):
		"met l'image en sepia"
		for i in range(len(self.p)):
			R = int(0.393*self.p[i][0] + 0.769*self.p[i][1] + 0.189*self.p[i][2])
			G = int(0.349*self.p[i][0] + 0.686*self.p[i][1] + 0.168*self.p[i][2])
			B = int(0.272*self.p[i][0] + 0.534*self.p[i][1] + 0.131*self.p[i][2])
			if R >= self.depth:
				R = self.depth

			if G >= self.depth:
				G = self.depth

			if B >= self.depth:
				B = self.depth

			self.p[i] = (R, G, B)

	def reverse(self):
		n = len(self.p)-1
		for i in range((n+1)//2):
			self.p[i],self.p[n-i] = self.p[n-i],self.p[i]


	def output(self,f):
		"sort l'image au format P3"
		f = open(f,"w")
		f.write("P3\n")
		f.write("{} {} {}\n".format(self.width,self.height,self.depth))
		print(self.p[0])
		for RGB in self.p:
			for v in RGB:
				f.write(str(v)+" ")
			f.write("\n")
		f.close()


def main():
	if len(sys.argv) < 3:
		print("Not enough argument")
		return

	name = sys.argv[2]
	out = sys.argv[3]
	pic = Picture(name)

	if sys.argv[1] == "-s":
		if len(sys.argv) < 6:
			print("Not enough argument for a swap")
			return
		co = sys.argv[4].split()
		sw = sys.argv[5].split()
		for i in range(3):
			co[i] = int(co[i])
			sw[i] = int(sw[i])
		pic.swap(co,sw)

	if sys.argv[1] == "-n":
		pic.negatif()

	elif sys.argv[1] == "-g":
		pic.B_and_W()

	elif sys.argv[1] == "-se":
		pic.sepia()

	elif sys.argv[1] == "-r":
		pic.reverse()

	pic.output(out)

main()
