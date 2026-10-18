class Persona:

    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo

    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        if correo.strip():
            self.__correo = correo
        else:
            print("Error: El correo no puede estar vacío.")

    def mostrar_informacion(self):
        print(f"Identificación: {self.__identificacion}")
        print(f"Nombre: {self.__nombre}")
        print(f"Correo: {self.__correo}")

    def realizar_actividad_principal(self):
        pass