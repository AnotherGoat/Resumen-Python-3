fido = Perro("Fido", "blanco")

print(fido.patas)  # 4
print(Perro.patas)  # 4

Perro.patas = 5

print(fido.patas)  # 5
print(Perro.patas)  # 5