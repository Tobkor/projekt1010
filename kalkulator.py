def dodawanie (a,b):
	return a + b
	
def get_info():
	print("Program kalkulator. Autor: Tobiasz")

get_info()

try:
	l1 = int(input())
	l2 = int(input())

	print (dodawanie(l1, l2))
except:
	print("Program zakonczyl sie nieoczekiwanym bledem")
	print("Mozesz go zglosci pod adresem pomoc@autor.pl")
