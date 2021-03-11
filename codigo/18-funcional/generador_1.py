def cuenta_regresiva():
    i = 5
    while i > 0:  # condición de salida
        yield i
        i -= 1

for i in cuenta_regresiva():
    print(i)