print("")
print("Frias Villa Angel Valentin 3 W")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)
    
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    
    def mostrar_informacion(self):
        """Muestra el lado mayor y el tipo de triángulo."""
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")

def main():
    # pide al usuario los lados del triángulo 
    lado1 = float(input("Introduce el valor del primer lado: "))
    lado2 = float(input("Introduce el valor del segundo lado: "))
    lado3 = float(input("Introduce el valor del tercer lado: "))
    
    # crea el objeto Triangulo
    triangulo = Triangulo(lado1, lado2, lado3)
    triangulo.mostrar_informacion()

if __name__ == "__main__":
    main()
