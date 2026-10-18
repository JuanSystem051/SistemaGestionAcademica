class Asignatura:

    def __init__(self, codigo, nombre, creditos, programa):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__programa = programa
        self.set_creditos(creditos)

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_creditos(self):
        return self.__creditos

    def get_programa(self):
        return self.__programa

    def set_creditos(self, creditos):
        if creditos > 0:
            self.__creditos = creditos
        else:
            print("Error: Los créditos deben ser mayores que cero.")

    def mostrar_informacion(self):
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Créditos: {self.__creditos}")
        print(f"Programa: {self.__programa.get_nombre()}")