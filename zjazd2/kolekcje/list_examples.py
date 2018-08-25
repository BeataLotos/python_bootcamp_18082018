imiona = ['Robert', 'Kamil', 'Ada', 'Beata']

print(type(imiona))
print('Typ obiektu`imiona`')
print(len('imiona'))
print('Ada' in imiona)

# dla kazdej zmiennej i w 'imiona' wypisz ją
for i in imiona:
    print(i)

# wybranie pierwszego imienia z listy
print('Pierwsze imie:', imiona[0])
print('Ostatnie imie:', imiona[-1])
print('Imiona od indexu 0 do 3:', imiona[0:3])

print('Pierwszy index imienia Kamil = ', imiona.index('Kamil'))
print('Ilośc imienia Kamil = ', imiona.count('Kamil'))

# ---------------------------------------------------------------
# operacje na liście
# dir wywołuje możliwe działania na liście
print(dir(imiona))
print(imiona)
imiona.append('Rafał')
print(imiona)
imiona.remove('Rafał')
print(imiona)
imiona += ['Ala', "Ada"]
print(imiona)