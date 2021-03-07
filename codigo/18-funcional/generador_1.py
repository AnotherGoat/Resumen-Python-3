def cuenta_regresiva():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in cuenta_regresiva():
    print(i)
# muestra los números del 5 al 1