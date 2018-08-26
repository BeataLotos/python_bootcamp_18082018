liczby = set()

while True:
    komenda = input("Podaj liczbę lub napisz `f` zeby przejść dalej: ")
    if liczby == 'f':
        break
    else:
        liczba = int(komenda)
        liczby.add(liczba)

print(f'Wprowadzono {len(liczby)} uniaklnych liczb')

# error