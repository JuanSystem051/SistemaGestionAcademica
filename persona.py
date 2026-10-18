class Persona:
    """Clase base que representa a una persona vinculada a la universidad."""

    def __init__(self, identificacion, nombre, correo):
        """Inicializa la persona. Lanza ValueError si el correo es vacío."""
        self.__identificacion = identificacion
        self.__nombre = nombre
        if not self.set_correo(correo):
            raise ValueError("El correo no puede estar vacío.")

    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        """Actualiza el correo si no es vacío. Retorna True si se modificó."""
        if isinstance(correo, str) and correo.strip():
            self.__correo = correo.strip()
            return True
        print("Error: El correo no puede estar vacío.")
        return False

    def mostrar_informacion(self):
        """Muestra los datos generales de la persona."""
        print(f"Identificación: {self.__identificacion}")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")

    def realizar_actividad_principal(self):
        """Debe ser sobrescrito por cada tipo de persona."""
        raise NotImplementedError(
            "Las subclases deben implementar realizar_actividad_principal()."
        )