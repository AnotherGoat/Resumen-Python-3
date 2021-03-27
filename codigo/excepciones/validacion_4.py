while True:
    try:
        edad = int(input('Ingrese su edad: '))
    except ValueError:
        print('Debes escribir un número')
        continue

    if edad < 0:
        print('Debes escribir un número positivo')
        continue
    else:
        break

print('Entrada válida')