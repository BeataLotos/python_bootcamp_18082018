from random import randint

ZAKRES = 10
x = randint(0,ZAKRES) # losuje liczby od do włącznie 
y = randint(0,ZAKRES)

point_x = x
point_y = y
x = randint(0,ZAKRES) # losuje liczby od do włącznie 
y = randint(0,ZAKRES)

gracz_x = x
gracz_y = y
print(f'Jesteś w punkcie {gracz_x},{gracz_y}. Znajdź skarb w point {point_x},{point_y}')
ruch = 0

while True:
        X = int(input(f'Podaj ruch w X: '))
        Y = int(input(f'Podaj ruch w Y: '))
        gracz_X = x+X
        gracz_Y = y+Y
        ruch += 1 
        if point_x == gracz_X and point_y == gracz_Y:
            print(f'Brawo! Liczba ruchów do odnalezienia skarbu: {ruch}')
            break
        if 0 > gracz_X  or gracz_X > 10 or 0 > gracz_Y or gracz_Y > 10:
            print('Jesteś poza planszą. Game over')    
            break
           
        else:
            if gracz_X>point_x:
                print('Zmniejsz X')
            if gracz_Y>point_y:
                print('Zmniejsz Y')
            if gracz_X<point_x:
                print('Zwiększ X')
            if gracz_Y<point_y:
                print('Zwiększ Y')
            if gracz_X == point_x: 
                print('X db')
            if gracz_Y == point_y: 
                print('Y db')
        if ruch > 2:
            goto ? 