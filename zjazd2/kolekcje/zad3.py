lista = [1,-100,50,-50,0]

liczby_dodatnie = 0
liczby_ujemne = 0

for liczba in lista:
    if liczba>0:
        liczby_dodatnie += 1
    elif liczba <0:
        liczby_ujemne += 1

print(f'Ujemne: {liczby_ujemne}, dodatnie: {liczby_dodatnie}')

