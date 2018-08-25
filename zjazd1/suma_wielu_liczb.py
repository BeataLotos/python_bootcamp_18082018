i = 0
suma = 0

while True:
    liczba =input('Podaj liczbę lub zakoncz program poprzez "end": ')
    if liczba == 'end':
        break
    liczba = float(liczba) # parsowanie = zamiana postaci tekstowej na liczbową 
    suma += liczba
    i += 1
    
print(f'Suma wynosi: {suma}')
print(f'Podałeś: {i} liczb')
if i != 0:
    print(f'Średnia liczb: {suma/i}')