liczba1 = int(input('Podaj pierwsza liczbe: '))
liczba2 = int(input('Podaj drugą liczbe: '))
operacja = input('Podaj rodzaj operacji spośród dostępnych: +,-,*,/ ')
zmienna = ['+','-','*',/


if operacja == '+':
	wynik1 = liczba1+liczba2
	print(f'Wynik:{wynik1}')
elif operacja =='-':
	wynik2 = liczba1-liczba2
	print(f'Wynik:{wynik2}')
elif operacja =='/':
	wynik3 = liczba1/liczba2
	print(f'Wynik:{wynik3}')
elif operacja =='*':
	wynik4 = liczba1/liczba2
	print(f'Wynik:{wynik4}')
else:
	wynik:None
if wynik is not None:
		print(f'Wynik: {wynik}')
else:
	print(f'Nieobsługiwana operacja:{operacja}. Dostępne operacje:(+,-,/,*)')

