class A(C):
    def metodo1(self):
        print("Método de A")

class B(A):
    def metodo2(self):
        print("Método de B")

class C(B):
    def metodo3(self):
        print("Método de C")