

####	Exercice_1.1

def power(x,n):
	if n == 1:
		return(x)
	return(x*power(x,n-1))

####	Exercice_1.2

def occurence(S,c):
	if S == "" :
		return(0)
	elif S[0] == c:
		return(1 + occurence(S[1:],c))
	else :
		return(occurence(S[1:],c))

####	Exercice_1.3
def maxi(x,y):
	if x > y:
		return(x)
	return(y)

def maximum(L):
	if len(L) == 2:
		return(maxi(L[0],L[1]))
	return(maxi(L[0],maximum(L[1:])))

####	Exercice_1.4


def palindrome(S):
	if len(S) < 2:
		return(True)
	print(S)
	if S[0] == S[len(S)-1]:
		return(palindrome(S[1:len(S)-1]))
	else :
		return(False)

####	Exercice_2.1
####	Exercice_2.2

fibico = {}

def fibonacci(n):
	if n == 0:
		return(0)
	elif n == 1:
		return(1)
	return(fibonacci(n-2)+fibonacci(n-1))

def fibonacci_dico(n):
	if n == 0:
		return(0)
	elif n == 1:
		return(1)
	if n in fibico:
		return(fibico[n])

	fibico[n] = fibonacci_dico(n-1)+fibonacci_dico(n-2)
	return(fibico[n])
