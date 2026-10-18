from persona import Persona


class Administrativo(Persona):
    """Persona del personal administrativo (hereda de Persona)."""

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = numero_empleado
        self.__dependencia = dependencia
        self.__cargo = cargo
        self.__jornada = jornada

    def get_numero_empleado(self):
        return self.__numero_empleado

    def get_dependencia(self):
        return self.__dependencia

    def get_cargo(self):
        return self.__cargo

    def get_jornada(self):
        return self.__jornada

    def set_cargo(self, cargo):
        """Actualiza el cargo si no es vacío."""
        if isinstance(cargo, str) and cargo.strip():
            self.__cargo = cargo.strip()
            return True
        print("Error: El cargo no puede estar vacío.")
        return False

    def mostrar_informacion(self):
        """Sobrescribe: datos generales + datos del administrativo."""
        super().mostrar_informacion()
        print(f"Número de empleado: {self.__numero_empleado}")
        print(f"Dependencia: {self.__dependencia}")
        print(f"Cargo: {self.__cargo}")
        print(f"Jornada: {self.__jornada}")

    def realizar_actividad_principal(self):
        """Sobrescribe: informa cargo y dependencia."""
        print(
            f"El administrativo desempeña el cargo de {self.__cargo} "
            f"en la dependencia {self.__dependencia}."
        )