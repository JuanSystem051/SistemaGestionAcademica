from persona import Persona

class Estudiante(Persona):

    def __init__(self, identificacion, nombre, correo,
                 codigo_estudiantil, programa, semestre, promedio):

        super().__init__(identificacion, nombre, correo)

        self.codigo_estudiantil = codigo_estudiantil
        self.programa = programa
        self.semestre = semestre
        self.promedio = promedio

    def mostrar_informacion(self):
        super().mostrar_informacion()

        print(f"Código Estudiantil: {self.codigo_estudiantil}")
        print(f"Programa: {self.programa.get_nombre()}")
        print(f"Semestre: {self.semestre}")
        print(f"Promedio: {self.promedio}")

    def realizar_actividad_principal(self):
        print(
            f"El estudiante cursa el programa "
            f"{self.programa.get_nombre()} "
            f"en el semestre {self.semestre}."
        )