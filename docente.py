from persona import Persona


class Docente(Persona):
    """Persona que orienta clases en la universidad (hereda de Persona)."""

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, facultad, tipo_contratacion, horas):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = numero_empleado
        self.__facultad = facultad
        self.__tipo_contratacion = tipo_contratacion
        if not self.set_horas(horas):
            raise ValueError("Las horas semanales deben ser mayores que cero.")

    def get_numero_empleado(self):
        return self.__numero_empleado

    def get_facultad(self):
        return self.__facultad

    def get_tipo_contratacion(self):
        return self.__tipo_contratacion

    def get_horas(self):
        return self.__horas

    def set_horas(self, horas):
        """Actualiza las horas semanales si son > 0."""
        if isinstance(horas, (int, float)) and horas > 0:
            self.__horas = horas
            return True
        print("Error: Las horas semanales deben ser mayores que cero.")
        return False

    def mostrar_informacion(self):
        """Sobrescribe: datos generales + datos del docente."""
        super().mostrar_informacion()
        print(f"Número de empleado: {self.__numero_empleado}")
        print(f"Facultad: {self.__facultad}")
        print(f"Tipo de contratación: {self.__tipo_contratacion}")
        print(f"Horas semanales: {self.__horas}")

    def realizar_actividad_principal(self):
        """Sobrescribe: informa la facultad donde orienta clases."""
        print(f"El docente orienta clases en la facultad de {self.__facultad}.")