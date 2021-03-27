def infinitos_sietes():
    while True:
        yield 7

for i in infinitos_sietes():
    print(i)