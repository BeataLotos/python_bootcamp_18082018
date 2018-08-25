i = 1
sum = 0
days_week = 7
while i <= days_week:
    temp = float(input('Podaj temperaturę: '))
    i += 1
    sum += temp

print(f'Średnia temperatura tygodnia wynosi {sum/days_week}')

i = 1
sum = 0
for i in range(7):  # tu są wartosci od 0 do 6
    temp = float(input(f'Podaj temperaturę w dniu {i+1}: '))
    i += 1
    sum += temp

print(f'Średnia temperatura tygodnia wynosi {sum/7}')
