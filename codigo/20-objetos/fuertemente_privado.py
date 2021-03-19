class Spam:
    __egg = 7

    def mostrar_egg(self):
        print(self.__egg)
    
s = Spam()

s.mostrar_egg()
print(s._Spam__egg)
print(s.__egg)