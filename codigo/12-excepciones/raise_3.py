password = input("Ingresa tu contraseña: ")

if len(password < 8):
    raise ValueError("La contraseña debe tener 8 o más caracteres")