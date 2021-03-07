pares = {
    1: "manzana",
    "naranja": [2, 3, 4],
    True: False,
    None: "True"
}

print(pares.get("naranja"))  # [2, 3, 4]
print(pares.get(42))  # None
print(pares.get(12345, "no encontrado"))  # no encontrado