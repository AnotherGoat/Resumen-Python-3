try:
    print(1)
    print(1 / 0)
except ZeroDivisionError:
    print(variable_desconocida)
finally:
    print("Este mensaje siempre se mostrará")

print("Este mensaje no se mostrará")