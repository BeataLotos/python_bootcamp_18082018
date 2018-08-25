print('Hey')
print()
print('What\'s your name?')
print()
print('Write your name, please...')
text = input()
print()
print (f'Hello {text}! Nice to meet you. I\'m Python')

print('Podaj promien kola, to policze pole tego kola')
PI=3.14
r = float(input()) # lub int jesli jest liczba calkowita 
pole_kola = PI * r * r
print(f'Pole kola wynosi: {pole_kola}')


S = 'Ala ma kota'
print(S[5]) # liczy od 0:end
print(S[2:5]) #od 2 do 5 bez 5 
# 7 % 4 daje reszte z dzielenia 7 / 4 
# w Pythonie nie ma ograniczenia na wielkosc liczb 
# float nie jest używane do liczenia np. pieniedzy bo nie zachowuje calkowitej precyzji. Uzywa sie bibliotek 
# float w Pythonie jest double w C++  


print('Podaj cene za kg...')
cena = float(input())
print('Podaj wage...')
waga = float(input())
naleznosc = float(cena*waga)
print(f'Naleznosc:') 
