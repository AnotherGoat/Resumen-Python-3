nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print('Todos los números son mayores que 5')

if any([i % 2 == 0 for i in nums]):
    print('Al menos un número es par')