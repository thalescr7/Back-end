class Forma():
    def area(self):
        pass

class Quadrado(Forma):

    def __int__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
    Quadrado = Quadrado(12)

    print(Quadrado.area())

    class circulo(Forma):
        def __init__(self,raio):
            self.raio = raio

    def area(self):
        return 3.14 * self.raio
    circulo = circulo(12)
    print(circulo.area)
         

