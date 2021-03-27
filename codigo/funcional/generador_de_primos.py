from math import sqrt

def es_primo(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def generar_primos():
    n = 2

    while True:
        if es_primo(n):
            yield n
        n += 1

for i in generar_primos():
    print(i)