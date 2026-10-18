class ProgramaAcademico:

    def __init__(self, codigo, nombre, facultad, numero_semestres):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__facultad = facultad
        self.set_numero_semestres(numero_semestres)

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_facultad(self):
        return self.__facultad

    def get_numero_semestres(self):
        return self.__numero_semestres

    def set_numero_semestres(self, numero):
        if numero > 0:
            self.__numero_semestres = numero
        else:
            print("Error: El número de semestres debe ser mayor que cero.")

    def mostrar_informacion(self):
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Facultad: {self.__facultad}")
        print(f"Semestres: {self.__numero_semestres}")