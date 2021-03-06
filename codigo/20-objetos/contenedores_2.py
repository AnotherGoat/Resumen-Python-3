import random

class ListaImprecisa:
    def __init__(self, contenido):
        self.contenido = contenido

    def __getitem__(self, indice):
        return self.contenido[indice + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.contenido) * 2)

lista_imprecisa = ListaImprecisa(["A", "B", "C", "D", "E"])

# Los resultados son aleatorios, haciendo que la lista sea imprecisa
print(len(lista_imprecisa))
print(len(lista_imprecisa))
print(len(lista_imprecisa))
print(lista_imprecisa[2])
print(lista_imprecisa[2])
print(lista_imprecisa[2])