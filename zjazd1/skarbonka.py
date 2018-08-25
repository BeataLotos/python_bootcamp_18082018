skarbonka = 20 
print(f'Początkowa wartość skarbonki wynosi {skarbonka} PLN')

while skarbonka<100:
    wplata = float(input('Podaj wpłatę w PLN: '))
    skarbonka += wplata
    print(f'Aktualna wartość skarbonki wynosi {skarbonka}')

print(f'Osiągnąłeś swój cel: 100 PLN, uzbierałeś {skarbonka} PLN')







