from persona import Persona

class Docente(Persona):

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, facultad,
                 tipo_contratacion, horas):

        super().__init__(identificacion, nombre, correo)

        self.numero_empleado = numero_empleado
        self.facultad = facultad
        self.tipo_contratacion = tipo_contratacion
        self.horas = horas

    def mostrar_informacion(self):
        super().mostrar_informacion()

        print(f"Número de empleado: {self.numero_empleado}")
        print(f"Facultad: {self.facultad}")
        print(f"Tipo de contratación: {self.tipo_contratacion}")
        print(f"Horas semanales: {self.horas}")

    def realizar_actividad_principal(self):
        print(
            f"El docente orienta clases en la facultad de "
            f"{self.facultad}."
        )