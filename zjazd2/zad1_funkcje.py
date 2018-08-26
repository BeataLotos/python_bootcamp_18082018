#def liczby_pierwsze():
#    liczba = input('Podaj liczbę: ')
#    if liczba % liczba == 0 and liczba % 1 == 0:
#        print("{liczba} jest liczbą pierwszą ")
#    else:
#        print("{liczba} NIE jest liczbą pierwszą ")

# ------ testowanie TDT test driven developement

def czy_jest_pierwsza(n):
   for dzielnik in range (2,n):
       if n % dzielnik == 0:
           return False
   return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej(): # małe znaki w przypadku funkcji
   assert czy_jest_pierwsza(3)
   assert czy_jest_pierwsza(7)


def test_czy_jest_pierwsza_dla_liczby_niepierwszej(): # małe znaki w przypadku funkcji
   assert not czy_jest_pierwsza(4)
   assert not czy_jest_pierwsza(122)



#def czy_wieksza_niz_jakas n(liczba, n=2):
#    if n > n:
#        return True
#    return False