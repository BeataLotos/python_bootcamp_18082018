# funkcja która definiuje pusty set
def wiecej_niz(napis, liczba_wystapien):

    for litera in napis:
        if napis.count(litera) > liczba_wystapien:
            wynik.add(litera)


    return set()

# test

def test_wiecej_niz_dla_pustego_napisu(): #testy muszą się zaczynac od slowa 'test'. W ciele funkcji musi miec 'assert'
   assert wiecej_niz('', 1) == set() # assert sprawdza czy True czy False


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('aaa', 2) == {a}
    #assert wiecej_niz('aaa bbb ccc', 2) == {a, b}

# error

# zmiana funkcji

# test - OK



#----
'aaaa'.count('a')