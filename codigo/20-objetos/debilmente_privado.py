class Cola:
    def __init__(self, contenido):
        self._lista_oculta = list(contenido)
    
    def agregar(self, valor):
        self._lista_oculta.insert(0, valor)
    
    def quitar(self):
        return self._lista_oculta.pop()
    
    def __repr__(self):
        return "Cola({})".format(self._lista_oculta)

cola = Cola([1, 2, 3])
print(cola)

cola.agregar(0)
print(cola)

cola.quitar()
print(cola)

# nada evita que se pueda acceder al atributo débilmente privado
print(cola._lista_oculta)