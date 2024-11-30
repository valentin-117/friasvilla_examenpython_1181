print("")
print("Frias Villa Angel Valentin 3 W")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')

    def es_mayor_de_edad(self):
        return 'es mayor de edad' if self.edad >= 18 else 'no es mayor de edad'

def main():
    nombre = input('Introduce tu nombre: ')
    edad = int(input('Introduce tu edad: '))

    persona = Persona(nombre, edad)

    persona.mostrar_datos()

    print(f'{persona.nombre} {persona.es_mayor_de_edad()}.')
if __name__ == '__main__':
    main()
