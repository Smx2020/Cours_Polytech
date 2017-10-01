prix = int(input("prix ? "))   #1
print(("trop cher\nj'achète pas" if prix > 1001 else ("j'achète\nmême si c'est pas donné" if prix > 100 else "j'achète\nc'est donné!" )))
print("fin des achats")   #

etudiant = input("Nom Prenom Sport FC :")
nom, prenom, sport, FC = etudiant.split()
print("Entrainement de {} {} :".format(prenom, nom))
if sport == "aucun" :
	if FC > 70:
		print("\tva falloir vous y mettre ...")
	else :
		print("\tbon coeur, entrainement inutile")
elif sport == "endurance" or sport == "combat" or sport == "collectif" :
	print("entrainez-vous à la fréquence max de ",int(FC) * (1.5 if sport == "collectif" else (1.2 if sport == "endurance" else 2)) )
else:
	print("je ne connais pas ce sport")

#	[5]	(1<3 or (5<2 and 8>1) )  True

#	[6]		a	|	b	|	and	|	or

#			F	|	F	|	F	|	F
#			F	|	T	|	F	|	T
#			T	|	F	|	F	|	T
#			T	|	T	|	T	|	T

#	[7]		a and b		<=>		not( not(a) or not(b))

####	Probleme

def calendrier(mois):
	if mois == 2:
		print("Il y a 29 jours les années bissextiles et 28 jours sinon")
	if mois < 8 and mois > 0:
		print("Il y a {} jours dans le mois {}".format(30 + mois % 2, mois))
	elif mois < 13 and mois > 0:
		print("Il y a {} jours dans le mois {}".format(30 + (mois + 1) % 2, mois))
	else :
		print("Erreur mois non compris entre 1 et 12")
