class A:
    def metodo1(self):
        print("Método de A")

class B(A):
    def metodo2(self):
        print("Método de B")

class C(B):
    def metodo3(self):
        print("Método de C")

c = C()

c.metodo1()  # A
c.metodo2()  # B
c.metodo3()  # C