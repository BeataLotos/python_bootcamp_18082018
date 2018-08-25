# Program sprawdzający znajomość tabliczki mnożenia

from random import randint

ZAKRES = 10
x = randint(1,ZAKRES) # losuje liczby od do włącznie 

y = randint(1,ZAKRES)
i = 0
db_wynik = x * y

while True:
    wynik = int(input(f'Podaj iloczyn {x} oraz {y}: '))
    i +=1
    if wynik == db_wynik:
        break
    
print(f'Gratulacje! W póbie {i} udało się podać odpowiedni wynik')