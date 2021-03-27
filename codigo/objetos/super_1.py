class A:
    def metodo(self):
        print("A")

class B(A):
    def metodo(self):
        print("B")

    def metodo_super(self):
        super().metodo()

b = B()

b.metodo()
b.metodo_super()