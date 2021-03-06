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

c.metodo1()  # Método de A
c.metodo2()  # Método de B
c.metodo3()  # Método de C