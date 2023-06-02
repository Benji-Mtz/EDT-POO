# Clase Abstracta que es el molde para que hereden otras clases
class Shape():
    def __init__(self, x, y, height, width) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
    def draw(self):
        pass
    
class Circle(Shape):
    def __init__(self, x, y, radius = 2) -> None:
        super().__init__(x, y, radius, radius)
        self.radius = radius
    def draw(self):
        print(f"Imprimiendo la forma de un circulo x:{self.x}, y:{self.y} y radio: {self.radius}")

class Triangule(Shape):
    def __init__(self, x, y, base, height) -> None:
        super().__init__(x, y, height, base)
        self.base = base
        self.height = height
    def draw(self):
        print(f"Imprimiendo la forma de un triangulo x:{self.x}, y:{self.y} con base: {self.base} y altura: {self.height}")
        
class Rectangle(Shape):
    def __init__(self, x, y, height, width) -> None:
        super().__init__(x, y, height, width)
    def draw(self):
        print(f"Imprimiendo un rectangulo con sus medidas {self.x} {self.y} un ancho {self.width} y un alto {self.height}")
        
circulo = Circle(50,50,25)
triangulo = Triangule(100,100,50,150)
rectangulo = Rectangle(300,200,200,100)

circulo.draw()
triangulo.draw()
rectangulo.draw()
