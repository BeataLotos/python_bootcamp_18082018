while True:
    liczba = float(input('Podaj liczbę, sprawdzam podzielność przez 7: '))
    if liczba % 7 == 0:
        break
            
print(f'Koniec. Liczba {liczba} jest podzielna przez 7')