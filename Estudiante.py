class Estudiante:
    contadorEstudiantes = 0
    def __new__(cls, *args, **kwargs):
        print("Se ha creado un estudiante nuevo...")
        return super().__new__(cls)
        

    def __init__(self, nombre, edad, matricula):
        self._nombre = nombre 
        self._edad = edad 
        self.matricula = matricula
        self.matriculado = False
        self.pago_pension = False
        Estudiante.aumentarContador()
    def __del__(self):
        print(f"Se elimino al estudiante {self.nombre}")



    def ingresarDatos(self):
        self.nombre = input("Nombre del estudiante: ")
        self.edad = input("Edad del estudiante: ")
        self.matricula = input("Número de matrícula: ")

    def imprimirDatos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.matricula)
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
    @classmethod
    def obtener_contador_estudiantes(cls):
        return cls.contadorEstudiantes
    @classmethod 
    def print_contador_estudiantes(cls):
        print(f"Num. de estudiantes: {cls.contadorEstudiantes}")
    @classmethod
    def aumentarContador(cls):
        cls.contadorEstudiantes = cls.contadorEstudiantes + 1

    @staticmethod
    def info():
        print("Esta clase es la clase estudiante, representa y contiene la informacion necesaria para la matriculacion de un estudiante.")
    @staticmethod
    def printNumEstudiantes():
        Estudiante.print_contador_estudiantes()