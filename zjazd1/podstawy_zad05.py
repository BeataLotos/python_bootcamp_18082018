A =(input('Miasto wyjazdu...'))
B=(input('Miasto przyjazdu...'))
dystans = float(input(f'Dystans{A}-{B} :')) 
cena = float(input('Cena paliwa: '))
spalanie = float(input('Spalanie na 100 km.: ')
wynik = dystans * cena * spalanie /100
print(f'Koszt przejazdu{A}-{B} to {wynik} PLN') 
