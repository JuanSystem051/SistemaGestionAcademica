class Horario:
    """Representa el horario (día, horas y salón) en que se desarrolla un grupo académico."""

    def __init__(self, dia, hora_inicio, hora_finalizacion, salon):
        """Inicializa el horario validando que sus campos no estén vacíos."""
        if not self.set_dia(dia):
            raise ValueError("El día no puede estar vacío.")
        if not self.set_hora_inicio(hora_inicio):
            raise ValueError("La hora de inicio no puede estar vacía.")
        if not self.set_hora_finalizacion(hora_finalizacion):
            raise ValueError("La hora de finalización no puede estar vacía.")
        if not self.set_salon(salon):
            raise ValueError("El salón no puede estar vacío.")

    def get_dia(self):
        return self.__dia

    def get_hora_inicio(self):
        return self.__hora_inicio

    def get_hora_finalizacion(self):
        return self.__hora_finalizacion

    def get_salon(self):
        return self.__salon

    def set_dia(self, dia):
        """Actualiza el día si no es vacío. Retorna True si se modificó."""
        if isinstance(dia, str) and dia.strip():
            self.__dia = dia.strip()
            return True
        print("Error: El día no puede estar vacío.")
        return False

    def set_hora_inicio(self, hora_inicio):
        """Actualiza la hora de inicio si no es vacía. Retorna True si se modificó."""
        if isinstance(hora_inicio, str) and hora_inicio.strip():
            self.__hora_inicio = hora_inicio.strip()
            return True
        print("Error: La hora de inicio no puede estar vacía.")
        return False

    def set_hora_finalizacion(self, hora_finalizacion):
        """Actualiza la hora de finalización si no es vacía. Retorna True si se modificó."""
        if isinstance(hora_finalizacion, str) and hora_finalizacion.strip():
            self.__hora_finalizacion = hora_finalizacion.strip()
            return True
        print("Error: La hora de finalización no puede estar vacía.")
        return False

    def set_salon(self, salon):
        """Actualiza el salón si no es vacío. Retorna True si se modificó."""
        if isinstance(salon, str) and salon.strip():
            self.__salon = salon.strip()
            return True
        print("Error: El salón no puede estar vacío.")
        return False

    def mostrar_informacion(self):
        """Muestra el detalle del horario."""
        print(
            f"Horario: {self.__dia} de {self.__hora_inicio} a {self.__hora_finalizacion} "
            f"- Salón: {self.__salon}"
        )
