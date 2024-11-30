print("")
print("Frias Villa Angel Valentin 3 W")
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Nota del alumno: {self.nota}")

    def resultado(self):
        if self.nota >= 5:
            print(f"{self.nombre} que tirazopapi,perfecto tu nota es: {self.nota}.")
        else:
            print(f"{self.nombre} yama, su nota es {self.nota}.")

alumno1 = Alumno("pepe pecas", 7.5)

alumno1.imprimir()
alumno1.resultado()
