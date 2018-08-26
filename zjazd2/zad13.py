

a = [x/10  for x in range(11)]
print(a)


b = {(x, x**2, x**3) for x in range(-10,11)}
print(b)

napisy = ['aa','bb']
c = {x: len(x) for x in napisy}
print(c)


# ------------

def hello_world(name="world"): # dzieki temu jesli nie wpiszemy argumentu, funkcja sie zwroci z "world"
    print(f"Hello world, here is: {name}")

# wywoływanie funkcji: hello_world("Adam")