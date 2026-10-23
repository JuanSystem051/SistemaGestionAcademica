from excepciones import ProgramaAcademicoNoEncontradoError


class ProgramaAcademico:
    """Representa un programa académico de la universidad."""

    def __init__(self, codigo, nombre, facultad, numero_semestres):
        """Inicializa el programa. Lanza ValueError si los semestres son inválidos."""
        self.__codigo = codigo
        self.__nombre = nombre
        self.__facultad = facultad
        if not self.set_numero_semestres(numero_semestres):
            raise ValueError("El número de semestres debe ser mayor que cero.")

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_facultad(self):
        return self.__facultad

    def get_numero_semestres(self):
        return self.__numero_semestres

    def set_numero_semestres(self, numero):
        """Actualiza los semestres si son > 0. Retorna True si se modificó."""
        if isinstance(numero, (int, float)) and numero > 0:
            self.__numero_semestres = numero
            return True
        print("Error: El número de semestres debe ser mayor que cero.")
        return False

    def mostrar_informacion(self):
        """Muestra los datos principales del programa."""
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Facultad: {self.__facultad}")
        print(f"Semestres: {self.__numero_semestres}")

    @staticmethod
    def buscar_programa(lista_programas, codigo):
        """Busca un programa por su código. Lanza ProgramaAcademicoNoEncontradoError si no existe."""
        for programa in lista_programas:
            if programa.get_codigo() == codigo:
                return programa
        raise ProgramaAcademicoNoEncontradoError(
            f"Error: El programa académico con código '{codigo}' no existe en el sistema."
        )
