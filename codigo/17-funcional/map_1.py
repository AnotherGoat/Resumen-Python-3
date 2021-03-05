def sumar5(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
resultado = list(map(sumar5, nums))
print(resultado)  # [16, 27, 38, 49, 60]