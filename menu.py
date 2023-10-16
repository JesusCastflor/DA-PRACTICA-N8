from Estudiante import Estudiante

def menu():
    print("Menú:")
    print("1. Ingresar datos del estudiante")
    print("2. Matricular al estudiante")
    print("3. Pagar pensión del estudiante")
    print("4. Mostrar información del estudiante")
    print("5. Cambiar datos del estudiante")
    print("6. Ver numero actual de estudiantes")
    print("7. Informacion de la clase Estudiante")

    print("0. Salir")

    estudiante = Estudiante("", 0, "")

    while True:
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            estudiante.ingresarDatos()
        elif opcion == "2":
            estudiante.matricular()
            print("Estudiante Matriculado")
        elif opcion == "3":
            estudiante.pagarPension()
            print("Estudiante Pagó pension")
        elif opcion == "4":
            estudiante.imprimirDatos()
        elif opcion == "5":
            print("Nuevo Nombre:")
            nuevo_nombre = input()
            estudiante.nombre = nuevo_nombre
            print("Nueva edad:")
            nueva_edad = input()
            estudiante.edad = int(nueva_edad)
        elif opcion == "6":
            Estudiante.print_contador_estudiantes()
        elif opcion == "7":
            Estudiante.info()
            Estudiante.printNumEstudiantes()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
