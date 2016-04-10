def dodawanie (a,b):
	return a + b
	
try:
	l1 = int(input())
	l2 = int(input())

	print (dodawanie(l1, l2))
except:
	print("Program zakonczyl sie nieoczekiwanym bledem")
	print("Mozesz go zglosci pod adresem pomoc@autor.pl")