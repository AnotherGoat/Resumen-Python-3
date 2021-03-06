class CadenaEspecial:
    def __init__(self, contenido):
        self.contenido = contenido

    def __gt__(self, otro):
        for i in range(len(otro.contenido) + 1):
            resultado = otro.contenido[:i] + ">" + self.contenido
            resultado += ">" + otro.contenido[i:]
            print(resultado)

palabra1 = CadenaEspecial("hola")
palabra2 = CadenaEspecial("mundo")

palabra1 > palabra2
# >hola>mundo
# m>hola>undo
# mu>hola>ndo
# mun>hola>do
# mund>hola>o
# mundo>hola>