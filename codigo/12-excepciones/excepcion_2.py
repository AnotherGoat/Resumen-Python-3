x = int(input())
y = int(input())

try:
    print("Resultado de la división: " + str(x / y))
except ZeroDivisionError:
    print("Error: Se intentó dividir por 0")