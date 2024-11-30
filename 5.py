print("")
print("Frias Villa Angel Valentin 3 W")
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        self.contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email})

    def lista_contactos(self):
        if self.contactos:
            for c in self.contactos: print(f"{c['nombre']} - {c['telefono']} - {c['email']}")
        else:
            print("No hay contactos.")

    def buscar_contacto(self):
        nombre = input("Buscar: ")
        for c in self.contactos:
            if c['nombre'].lower() == nombre.lower():
                print(f"{c['nombre']} - {c['telefono']} - {c['email']}")
                return
        print("Contacto no encontrado.")

    def editar_contacto(self):
        nombre = input("Editar: ")
        for c in self.contactos:
            if c['nombre'].lower() == nombre.lower():
                c['nombre'] = input(f"Nuevo nombre ({c['nombre']}): ") or c['nombre']
                c['telefono'] = input(f"Nuevo teléfono ({c['telefono']}): ") or c['telefono']
                c['email'] = input(f"Nuevo email ({c['email']}): ") or c['email']
                return
        print("Contacto no encontrado.")

    def menu(self):
        while True:
            print("\n1. Añadir\n2. Ver\n3. Buscar\n4. Editar\n5. Salir")
            opcion = input("Elige opción: ")
            if opcion == '1': self.añadir_contacto()
            elif opcion == '2': self.lista_contactos()
            elif opcion == '3': self.buscar_contacto()
            elif opcion == '4': self.editar_contacto()
            elif opcion == '5': break

agenda = Agenda()
agenda.menu()
