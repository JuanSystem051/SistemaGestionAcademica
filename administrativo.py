from persona import Persona

class Administrativo(Persona):

    def __init__(self, identificacion, nombre, correo,
                 numero_empleado, dependencia,
                 cargo, jornada):

        super().__init__(identificacion, nombre, correo)

        self.numero_empleado = numero_empleado
        self.dependencia = dependencia
        self.cargo = cargo
        self.jornada = jornada

    def mostrar_informacion(self):
        super().mostrar_informacion()

        print(f"Número de empleado: {self.numero_empleado}")
        print(f"Dependencia: {self.dependencia}")
        print(f"Cargo: {self.cargo}")
        print(f"Jornada: {self.jornada}")

    def realizar_actividad_principal(self):
        print(
            f"El administrativo desempeña el cargo de "
            f"{self.cargo} en la dependencia {self.dependencia}."
        )