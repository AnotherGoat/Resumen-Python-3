def saludar(nombre=None):
    if nombre is not None:
        print("Hola, " + nombre)
    else:
        print("Hola")

saludar()  # Hola
saludar("Juan")  # Hola, Juan