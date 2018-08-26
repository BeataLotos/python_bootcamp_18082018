napis = input('Podaj napis :')


liczniki = {}
for litera in napis:
    if litera in liczniki:
        liczniki[litera] +=1
    else:
        liczniki[litera] =1

print(liczniki)


# lub
for litera in napis.lower():
    liczniki[litera] = liczniki.get(1,0) + 1

for litera in liczniki:
    print(f' Litera {litera} wystąpiła {liczniki[litera]} razy')



zbior1  = {1,2,3}
set
1 in zbior1
zbior1.add(4) -> zbior1  = {1,2,3,4} # w zbiorze każdy element może wystąpić tylko raz, nie ma kolejności w zbiorze

zbior1 | zbior2  -> elementy w zbiorze1 lub 2
zbior1 & zbior2 -> elementy wspolne zbiorow