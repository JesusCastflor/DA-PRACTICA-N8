from estudiante import Estudiante

estudiante1 = Estudiante("Carlos", 19, "2023-003")
estudiante2 = Estudiante("Laura", 21, "2023-004")

lista_estudiantes = [estudiante1, estudiante2]

for estudiante in lista_estudiantes:
    estudiante.ingresarDatos()
    estudiante.matricular()
    estudiante.pagarPension()

for estudiante in lista_estudiantes:
    estudiante.imprimirDatos()
