liczby = []
while len(liczby) < 10:
    nowa_liczba = input("Podaj liczbę lub napisz `k` zeby zakonczyc: ")
    if nowa_liczba == 'k':
        break
    else:
        nowa_liczba = int(nowa_liczba)
        liczby.append(nowa_liczba)


srednia = sum(liczby) / len(liczby)
print(f'Średnia z liczb {liczby} to: {srednia} ')



