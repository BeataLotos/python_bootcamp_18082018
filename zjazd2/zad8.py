text = "Ala <ma> kota"

start = text.find("<")
stop = text.find(">")

print(text[start+1:stop])
print(stop-start-1)

# ------------- 2gie rozwiązanie

w_nawiasach = False
liczba_znakow = 0

for i in text:
    if i == "<":
        w_nawiasach = True
    elif i == ">":
        w_nawiasach = False
    elif w_nawiasach: # true or false
        liczba_znakow += 1

print(f"Pomiedzy nawiasami {liczba_znakow}")
