from empleados.administrador import Administrador
from empleados.conserje import Conserje
from empleados.guardia import Guardia
from empleados.veterinario import Veterinario

from transportes.bicicleta import Bicicleta
from transportes.cuadraciclo import Cuadraciclo
from transportes.patineta import Patineta

from animales.leon import Leon
from animales.tiburon import Tiburon
from animales.aguila import Aguila
from animales.iguana import Iguana
from animales.rana import Rana


empleados_registrados = []
transportes_registrados = []
animales_registrados = []


def registrar_empleado():

    print("\n--- Registro de empleados ---")
    print("1. Administrador")
    print("2. Guardia")
    print("3. Conserje")
    print("4. Veterinario")

    tipo = input("Seleccione el tipo: ")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    if tipo == "1":
        nuevo = Administrador(nombre, edad)

    elif tipo == "2":
        nuevo = Guardia(nombre, edad)

    elif tipo == "3":
        nuevo = Conserje(nombre, edad)

    elif tipo == "4":
        nuevo = Veterinario(nombre, edad)

    else:
        print("Tipo no válido")
        return

    empleados_registrados.append(nuevo)
    print("Empleado agregado")


def ver_empleados():

    print("\nLista de empleados")

    if len(empleados_registrados) == 0:
        print("No hay empleados registrados")

    for e in empleados_registrados:
        print(e)


def registrar_transporte():

    print("\n--- Registro de transportes ---")
    print("1. Bicicleta")
    print("2. Cuadraciclo")
    print("3. Patineta")

    tipo = input("Seleccione transporte: ")
    marca = input("Marca: ")

    if tipo == "1":
        nuevo = Bicicleta(marca)

    elif tipo == "2":
        nuevo = Cuadraciclo(marca)

    elif tipo == "3":
        nuevo = Patineta(marca)

    else:
        print("Transporte inválido")
        return

    transportes_registrados.append(nuevo)
    print("Transporte guardado")


def ver_transportes():

    print("\nTransportes registrados")

    if len(transportes_registrados) == 0:
        print("No hay transportes")

    for t in transportes_registrados:
        print(t)


def registrar_animal():

    print("\n--- Registro de animales ---")
    print("1. Leon")
    print("2. Tiburon")
    print("3. Aguila")
    print("4. Iguana")
    print("5. Rana")

    tipo = input("Seleccione el animal: ")
    nombre = input("Nombre del animal: ")

    if tipo == "1":
        nuevo = Leon(nombre)

    elif tipo == "2":
        nuevo = Tiburon(nombre)

    elif tipo == "3":
        nuevo = Aguila(nombre)

    elif tipo == "4":
        nuevo = Iguana(nombre)

    elif tipo == "5":
        nuevo = Rana(nombre)

    else:
        print("Animal inválido")
        return

    animales_registrados.append(nuevo)
    print("Animal agregado")


def ver_animales():

    print("\nAnimales registrados")

    if len(animales_registrados) == 0:
        print("No hay animales")

    for a in animales_registrados:
        print(a)


def menu():

    while True:

        print("\n===== SISTEMA DEL ZOOLOGICO =====")
        print("1. Registrar empleado")
        print("2. Ver empleados")
        print("3. Registrar transporte")
        print("4. Ver transportes")
        print("5. Registrar animal")
        print("6. Ver animales")

        print("\npresione 'finalizar' si desea salir")

        opcion = input("Seleccione una opcion: ")

        if opcion.lower() == "finalizar":
            break

        elif opcion == "1":
            registrar_empleado()

        elif opcion == "2":
            ver_empleados()

        elif opcion == "3":
            registrar_transporte()

        elif opcion == "4":
            ver_transportes()

        elif opcion == "5":
            registrar_animal()

        elif opcion == "6":
            ver_animales()

        else:
            print("Opción no válida")


menu()
