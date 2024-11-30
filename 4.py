print("")
print("Frias Villa Angel Valentin 3 W")
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return "Error: División por cero"
        else:
            return self.num1 / self.num2
    def mostrar_resultados(self):
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")
def main():
    # Solicitar los dos números enteros al usuario
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    
    # Crea una instancia de la clase Calculadora con los números ingresados
    calculadora = Calculadora(num1, num2)
    
    # muestra los resultados de las operaciones
    calculadora.mostrar_resultados()

# funcion principal
if __name__ == "__main__":
    main()
