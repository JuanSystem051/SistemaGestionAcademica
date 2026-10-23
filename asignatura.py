from excepciones import AsignaturaNoEncontradaError


class Asignatura:
    """Representa una asignatura perteneciente a un programa académico."""

    def __init__(self, codigo, nombre, creditos, programa):
        """Inicializa la asignatura. Lanza ValueError si los créditos son inválidos."""
        self.__codigo = codigo
        self.__nombre = nombre
        self.__programa = programa
        if not self.set_creditos(creditos):
            raise ValueError("Los créditos deben ser mayores que cero.")

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_creditos(self):
        return self.__creditos

    def get_programa(self):
        return self.__programa

    def set_creditos(self, creditos):
        """Actualiza los créditos si son > 0. Retorna True si se modificó."""
        if isinstance(creditos, (int, float)) and creditos > 0:
            self.__creditos = creditos
            return True
        print("Error: Los créditos deben ser mayores que cero.")
        return False

    def mostrar_informacion(self):
        """Muestra la información de la asignatura."""
        print(f"Código: {self.__codigo}")
        print(f"Nombre: {self.__nombre}")
        print(f"Créditos: {self.__creditos}")
        print(f"Programa: {self.__programa.get_nombre()}")

    @staticmethod
    def buscar_asignatura(lista_asignaturas, codigo):
        """Busca una asignatura por su código. Lanza AsignaturaNoEncontradaError si no existe."""
        for asignatura in lista_asignaturas:
            if asignatura.get_codigo() == codigo:
                return asignatura
        raise AsignaturaNoEncontradaError(
            f"Error: La asignatura con código '{codigo}' no existe en el sistema."
        )
