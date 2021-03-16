while True:
    try:
        num = int(input('Ingrese un número: '))
    except ValueError:
        print('Debes escribir un número')
        continue

    break

print('Entrada válida')