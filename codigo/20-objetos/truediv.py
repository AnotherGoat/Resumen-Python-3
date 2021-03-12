class CadenaEspecial:
    def __init__(self, contenido):
        self.contenido = contenido

    def __truediv__(self, otro):
        linea = "=" * len(otro.contenido)
        return "\n".join([self.contenido, linea, otro.contenido])

palabra1 = CadenaEspecial("hola")
palabra2 = CadenaEspecial("mundo")

print(palabra1 / palabra2)