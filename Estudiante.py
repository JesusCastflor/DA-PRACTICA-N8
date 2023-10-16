class Estudiante:
    contadorEstudiantes = 0
    def __init__(self, nombre, edad, matricula):
        self._nombre = nombre 
        self._edad = edad 
        self.matricula = matricula
        self.matriculado = False
        self.pago_pension = False



    def ingresarDatos(self):
        self.nombre = input("Nombre del estudiante: ")
        self.edad = input("Edad del estudiante: ")
        self.matricula = input("Número de matrícula: ")

    def imprimirDatos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Número de Matrícula:", self.matricula)
        if self.matriculado:
            print("Matriculado: Sí")
        else:
            print("Matriculado: No")
        if self.pago_pension:
            print("Pensión Pagada: Sí")
        else:
            print("Pensión Pagada: No")

    def matricular(self):
        self.matriculado = True

    def pagarPension(self):
        self.pago_pension = True
    
    @property
    def edad(self):
        return self._edad  

    @edad.setter
    def edad(self, nuevo):
        self._edad = nuevo

    @property
    def nombre(self):
        return self._nombre  

    @nombre.setter
    def nombre(self, nuevo):
        self._nombre = nuevo  