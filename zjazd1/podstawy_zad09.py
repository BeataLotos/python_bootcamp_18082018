import datetime
rok_urodzenia = int(input('Podaj rok urodzenia: '))
rok_bieżący = datetime.datetime.today().year # poziom modułu i poziom klasy 
wiek = rok_bieżący - rok_urodzenia

if wiek >= 18:
   print('Jesteś pełnoletni/a!')  
else:
	print('Jesteś niepełnoletni/a!')	

	
liczba = int(input('Podaj rok urodzenia: '))
if liczba <=2000:
    print('Jesteś pełnoletni/a!')
else:
	print('Jesteś niepełnoletni/a!')	
