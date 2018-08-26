def policz_znaki(napis, start="<", end=">"):
    if start == end:
        raise ValueError("parametry start i end nie moga być takie same")
    ile_znakow = 0
    poziom = 0
    for litera in napis:
        if litera == start:
            poziom += 1
            continue
        elif litera == end:
            poziom -= 1
            continue
        ile_znakow += poziom
    return ile_znakow

# testy wykonują soie tylko kiedy uzywamy pytest. Skrypty przy uzyciu python. Trzeba to zmienic w "configurations"
    assert policz_znaki('') == 0

def test_policz_znaki_gdy_brak_nawiasów(): # testy wykonują soie tylko kiedy uzywamy pytest. Skrypty przy uzyciu python. Trzeba to zmienic w "configurations"
    assert policz_znaki('Ala ma kota') == 0

def test_policz_znaki_z_nawiasami_jeden_poziom(): # testy wykonują soie tylko kiedy uzywamy pytest. Skrypty przy uzyciu python. Trzeba to zmienic w "configurations"
    assert policz_znaki('Ala <ma> kota') == 2
    assert policz_znaki("ala <kota> ") == 4
    assert policz_znaki('ala [kota [a kot]] ma [ale]','[,]') == 18