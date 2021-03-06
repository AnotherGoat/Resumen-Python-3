class A:
    valor = 1

a = A()
print(a.valor) # 1

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
# B
b.metodo_super()
# A