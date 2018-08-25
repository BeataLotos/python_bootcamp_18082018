list(range(100))
podzielne = 0

for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        podzielne += 1
        print(f'Liczby podzielne to: {i}')
print(f'Ilość podzielnych liczb: {podzielne}')

# ctr alt L -> spr. uroku kodu (pep8)
