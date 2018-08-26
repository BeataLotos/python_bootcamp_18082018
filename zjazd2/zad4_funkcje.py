def formatuj(*napisy, cena):
    return "\n".join(napisy)



def test_formatuj_napis_bez_znaczników():
    assert formatuj("Hey") == "Hey"

def test_formatuj_wiele_napisów_bez_znaczników():
    assert formatuj("Hello world","I'm here") == "Hello world\nI'm here"

def test_formatuj_napis_ze_znacznikiem():
    assert formatuj("koszt {cena} PLN","kwota {cena} brutto") == "koszt {cena} PLN\nkwota {cena} brutto"
    assert formatuj("koszt $cena PLN", "kwota {cena} brutto") == "koszt {cena} PLN\nkwota {cena} brutto"