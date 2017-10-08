####	Exercice_1

def nb_day(y, m):
	"Show the number of day in the month"
	if m == 2 :
		return(29 if y % 4 == 0 and y % 100 != 0 else 28)
	if m < 8 :
		return(30 + (m) % 2)
	if m >= 8 :
		return(30 + (m + 1) % 2)

def check_date(d, m, y):
	"Check if the date is valid"
	if y > 2018 or y < 1600 :
		return("l'annee")
	if m > 12 or m < 1 :
		return("le mois")
	if d > nb_day(y, m):
		return("le jour")
	return(0)

def get_tomorow(cal):
	msg = check_date(cal[0], cal[1], cal[2])
	if msg != 0 :
		print("Il y a une erreur sur ", msg)
	else :
		go = True
		i = 0
		while go :
			cal[i] += 1
			msg = check_date(cal[0], cal[1], cal[2])
			if msg == 0 :
				go = False
			else :
				cal[i] = 1
				i += 1
			if i == 3 :
				go = False
				print('ERRROR')

		return(cal)

calendar = input("Donner la date : ")
day, month, year = calendar.split('/')
cal = [int(day), int(month), int(year)]
cal = get_tomorow(cal)
print("{}/{}/{}".format(cal[0], cal[1], cal[2]))

arr = input("Donner la date d'arrive : ")
dep = input("Donner la date de depart : ")
day, month, year = arr.split('/')
arr = [int(day), int(month), int(year)]
day, month, year = dep.split('/')
dep = [int(day), int(month), int(year)]

i = 0
while arr[0] != dep[0] or arr[1] != dep[1] or arr[2] != dep[2] :
	arr = get_tomorow(arr)
	i += 1
print(i)
