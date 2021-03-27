x = 1  # variable global

def funcion():
    y = 2  # variable local

    global z # declaración de variable global
    z = 3  # asignación de variable global

funcion()
print(z)