x = input()
y = input()

try:
    print("Resultado de la división: " + str(x / y))
except ZeroDivisionError:
    print("Error: Se intentó dividir por 0")
except (ValueError, TypeError):
    print("Error: Valor o tipo no válido")
except:
    print("Ocurrió un error inesperado")