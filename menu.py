from estudiante import Estudiante

def menu():
    print("Menú:")
    print("1. Ingresar datos del estudiante")
    print("2. Matricular al estudiante")
    print("3. Pagar pensión del estudiante")
    print("4. Mostrar información del estudiante")
    print("0. Salir")

    estudiante = Estudiante("", 0, "")

    while True:
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante.ingresarDatos()
        elif opcion == "2":
            estudiante.matricular()
        elif opcion == "3":
            estudiante.pagarPension()
        elif opcion == "4":
            estudiante.imprimirDatos()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
