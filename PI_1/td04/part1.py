def affine(a,b,x):
	"renvoie la valeur de la courbe affine de coeff a et b au point x"
	return(a*x+b)

####	Exercice_1

# La commande print(affine(1,1,1)) renvoie 1*1+1 = 2

####	Exercice_2

# La commande print(affine(affine(1,1,1),1,1)) renvoie (1*1+1)*1+1 = 3

####	Exercice_3

def conv_temp(value, norme = "Fahrenheit"):
	"convertie les temperatures entre Celsius et Fahrenheit"
	if norme == "Celsius" :
		return(affine(1.8, 32, value))
	elif norme == "Fahrenheit":
		return(affine(1/1.8,0,affine(1, value, -32)))
	else :
		print("Unite non reconnue")
		return(1)

####	Exercice_4

def surfaceAPeindre(L,l,h):
	"Donne la surface a peindre en fonction de la longueur,largeur et la hauteur"
	return(h*(2*L + 2*l))

def nombrePot(L,l,h,po_couv):
	"Donne le nombre de pot necessaire pour peindre une salle de longueur,largeur et hauteur definie"
	return(int(surfaceAPeindre(L,l,h)/po_couv) + 1.0)

print("deco and co")

h = float(input("hauteur de la pièce (en m)? "))
L = float(input("longueur de la pièce  (en m)? "))
l = float(input("longueur de la pièce  (en m)? "))
po_couv = float(input("pouvoir couvrant de votre peinture (en m2)? "))

print("vous allez peindre ", surfaceAPeindre(L,l,h), " m2")
print("il vous faut ", nombrePot(L,l,h,po_couv), " pots")

####	Exercice_5

go = True
print("deco and co")

while go:
	h = float(input("hauteur de la pièce (en m)? "))
	n = input("nom de la pièce ")
	L = float(input("longueur de la pièce  (en m)? "))
	l = float(input("longueur de la pièce  (en m)? "))
	po_couv = float(input("pouvoir couvrant de votre peinture (en m2)? "))

	print("vous allez peindre ", surfaceAPeindre(L,l,h), " m2")
	print("il vous faut ", nombrePot(L,l,h,po_couv), " pots pour la", n)

	go = (True if input("autre pièce ? (o/n)") == "o" else False)
