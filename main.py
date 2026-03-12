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


lista_empleados = []
lista_transportes = []
lista_animales = []


def registrar_empleado():

    print("\n--- Registro de empleados ---")
    print("1 Administrador")
    print("2 Guardia")
    print("3 Conserje")
    print("4 Veterinario")

    tipo = input("Seleccione el tipo de empleado: ")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    if tipo == "1":
        persona = Administrador(nombre, edad)

    elif tipo == "2":
        persona = Guardia(nombre, edad)

    elif tipo == "3":
        persona = Conserje(nombre, edad)

    elif tipo == "4":
        persona = Veterinario(nombre, edad)

    else:
        print("Tipo inválido")
        return

    lista_empleados.append(persona)
    print("Empleado agregado correctamente")


def mostrar_empleados():

    print("\nLista de empleados")
    for emp in lista_empleados:
        print(emp)


def registrar_transporte():

    print("\n--- Registro de transportes ---")
    print("1 Bicicleta")
    print("2 Cuadraciclo")
    print("3 Patineta")

    tipo = input("Seleccione transporte: ")

    marca = input("Marca del transporte: ")

    if tipo == "1":
        vehiculo = Bicicleta(marca)

    elif tipo == "2":
        vehiculo = Cuadraciclo(marca)

    elif tipo == "3":
        vehiculo = Patineta(marca)

    else:
        print("Opción inválida")
        return

    lista_transportes.append(vehiculo)
    print("Transporte agregado")


def mostrar_transportes():

    print("\nTransportes disponibles")
    for t in lista_transportes:
        print(t)


def registrar_animal():

    print("\n--- Registro de animales ---")
    print("1 Leon")
    print("2 Tiburon")
    print("3 Aguila")
    print("4 Iguana")
    print("5 Rana")

    tipo = input("Seleccione el animal: ")

    nombre = input("Nombre del animal: ")

    if tipo == "1":
        animal = Leon(nombre)

    elif tipo == "2":
        animal = Tiburon(nombre)

    elif tipo == "3":
        animal = Aguila(nombre)

    elif tipo == "4":
        animal = Iguana(nombre)

    elif tipo == "5":
        animal = Rana(nombre)

    else:
        print("Opción inválida")
        return

    lista_animales.append(animal)
    print("Animal registrado")


def mostrar_animales():

    print("\nAnimales registrados")
    for a in lista_animales:
        print(a)


def iniciar_programa():

    while True:

        print("\n===== SISTEMA DEL ZOOLOGICO =====")
        print("1 Registrar empleado")
        print("2 Ver empleados")
        print("3 Registrar transporte")
        print("4 Ver transportes")
        print("5 Registrar animal")
        print("6 Ver animales")
        print("7 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empleado()

        elif opcion == "2":
            mostrar_empleados()

        elif opcion == "3":
            registrar_transporte()

        elif opcion == "4":
            mostrar_transportes()

        elif opcion == "5":
            registrar_animal()

        elif opcion == "6":
            mostrar_animales()

        elif opcion == "7":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida")


iniciar_programa()
