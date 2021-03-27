pares = {
    1: "manzana",
    "naranja": [2, 3, 4],
    True: False,
    None: "True"
}

print(pares.get("naranja"))
print(pares.get(42))
print(pares.get(12345, "no encontrado"))