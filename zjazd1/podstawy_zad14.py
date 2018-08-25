min = max = None

while True:
    liczba = input('Podaj liczbę lub zakoncz program poprzez "end": ')
    if liczba == 'end':
        break
    try:
        liczba = float(liczba)
        if max is None or liczba > max:
            max = liczba
        if min is None or liczba < min:
            min = liczba
    except Exception:    
        pass
        
        
print(f'Maksymalna liczba spośród podanych wynosi: {max} , minimalna wynosi: {min}')