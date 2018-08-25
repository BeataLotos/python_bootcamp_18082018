samogloski = 'aeaiou'
text = input("podaj napis: ")
liczba = 0

for i in text:
    if i.lower() in samogloski:
        liczba +=1

print(f'w napisie jest {liczba} samogłosek')

