liczba1 = int(input('Podaj pozycję gracza X (od 0 do 100): '))
liczba2 = int(input('Podaj pozycję gracza Y (od 0 do 100): '))

if 0 < liczba1 < 9:
     x = 'x lewy'
elif 9 < liczba1 > 91: 
    x = 'x środek'
elif 91 < liczba1 < 100:
    x = 'x prawy'
    
elif 0 < liczba2 <9:
    y = 'y góra'
elif 9 < liczba2 > 91: 
    y = 'y środek'
elif 91 < liczba2 < 100:
    y = 'y prawy'
    
    
else:
    print ('Poza zasięgiem') 
print(f('Gracz znajduje się w {x},{y}')    