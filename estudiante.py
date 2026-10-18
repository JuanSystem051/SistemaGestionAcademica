from persona import Persona


class Estudiante(Persona):
    """Persona matriculada en un programa académico (hereda de Persona)."""

    def __init__(self, identificacion, nombre, correo,
                 codigo_estudiantil, programa, semestre, promedio):
        super().__init__(identificacion, nombre, correo)
        self.__codigo_estudiantil = codigo_estudiantil
        self.__programa = programa
        if not self.set_semestre(semestre):
            raise ValueError("El semestre debe ser mayor que cero.")
        if not self.set_promedio(promedio):
            raise ValueError("El promedio debe estar entre 0.0 y 5.0.")

    def get_codigo_estudiantil(self):
        return self.__codigo_estudiantil

    def get_programa(self):
        return self.__programa

    def get_semestre(self):
        return self.__semestre

    def get_promedio(self):
        return self.__promedio

    def set_semestre(self, semestre):
        """Actualiza el semestre si es > 0. Retorna True si se modificó."""
        if isinstance(semestre, int) and semestre > 0:
            self.__semestre = semestre
            return True
        print("Error: El semestre debe ser un entero mayor que cero.")
        return False

    def set_promedio(self, promedio):
        """Actualiza el promedio si está entre 0.0 y 5.0."""
        if isinstance(promedio, (int, float)) and 0 <= promedio <= 5:
            self.__promedio = promedio
            return True
        print("Error: El promedio debe estar entre 0.0 y 5.0.")
        return False

    def mostrar_informacion(self):
        """Sobrescribe: datos generales + datos del estudiante."""
        super().mostrar_informacion()
        print(f"Código Estudiantil: {self.__codigo_estudiantil}")
        print(f"Programa: {self.__programa.get_nombre()}")
        print(f"Semestre: {self.__semestre}")
        print(f"Promedio: {self.__promedio}")

    def realizar_actividad_principal(self):
        """Sobrescribe: informa programa y semestre que cursa."""
        print(
            f"El estudiante cursa el programa {self.__programa.get_nombre()} "
            f"en el semestre {self.__semestre}."
        )