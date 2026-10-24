from asignatura import Asignatura
from docente import Docente
from estudiante import Estudiante
from horario import Horario
from excepciones import (
    EstudianteYaMatriculadoError,
    CapacidadMaximaAlcanzadaError,
    EstudianteNoMatriculadoError,
)


class GrupoAcademico:
    """Representa un grupo ofertado para una asignatura, con docente, horario y estudiantes."""

    def __init__(self, codigo, asignatura, docente, capacidad_maxima, horario):
        """Inicializa el grupo recibiendo objetos de Asignatura, Docente y Horario."""
        self.__codigo = codigo

        if not isinstance(asignatura, Asignatura):
            raise TypeError("La asignatura debe ser un objeto de la clase Asignatura.")
        self.__asignatura = asignatura

        if not isinstance(docente, Docente):
            raise TypeError("El docente debe ser un objeto de la clase Docente.")
        self.__docente = docente

        if not self.set_capacidad_maxima(capacidad_maxima):
            raise ValueError("La capacidad máxima debe ser un entero mayor que cero.")

        if not isinstance(horario, Horario):
            raise TypeError("El horario debe ser un objeto de la clase Horario.")
        # Relación de composición: el grupo contiene y gestiona su propio objeto Horario
        self.__horario = Horario(
            horario.get_dia(),
            horario.get_hora_inicio(),
            horario.get_hora_finalizacion(),
            horario.get_salon(),
        )

        self.__estudiantes_matriculados = []

    def get_codigo(self):
        return self.__codigo

    def get_asignatura(self):
        return self.__asignatura

    def get_docente(self):
        return self.__docente

    def get_capacidad_maxima(self):
        return self.__capacidad_maxima

    def get_estudiantes_matriculados(self):
        return list(self.__estudiantes_matriculados)

    def get_horario(self):
        return self.__horario

    def set_capacidad_maxima(self, capacidad_maxima):
        """Actualiza la capacidad máxima si es un entero > 0."""
        if isinstance(capacidad_maxima, int) and capacidad_maxima > 0:
            self.__capacidad_maxima = capacidad_maxima
            return True
        print("Error: La capacidad máxima debe ser un entero mayor que cero.")
        return False

    def mostrar_informacion_grupo(self):
        """Muestra los datos del grupo académico, incluyendo asignatura, docente y horario."""
        print(f"Código del grupo: {self.__codigo}")
        print(
            f"Asignatura: {self.__asignatura.get_nombre()} "
            f"({self.__asignatura.get_codigo()})"
        )
        print(f"Docente responsable: {self.__docente.get_nombre()}")
        print(
            f"Cupos ocupados: {len(self.__estudiantes_matriculados)}/"
            f"{self.__capacidad_maxima}"
        )
        self.__horario.mostrar_informacion()

    def matricular_estudiante(self, estudiante):
        """
        Matricula un objeto Estudiante en el grupo.
        Lanza EstudianteYaMatriculadoError si ya está inscrito.
        Lanza CapacidadMaximaAlcanzadaError si no hay cupos disponibles.
        """
        if not isinstance(estudiante, Estudiante):
            raise TypeError("Solo se pueden matricular objetos de la clase Estudiante.")

        for inscrito in self.__estudiantes_matriculados:
            if inscrito.get_codigo_estudiantil() == estudiante.get_codigo_estudiantil():
                raise EstudianteYaMatriculadoError(
                    f"Error de matrícula: El estudiante {estudiante.get_nombre()} "
                    f"({estudiante.get_codigo_estudiantil()}) ya está matriculado "
                    f"en el grupo {self.__codigo}."
                )

        if len(self.__estudiantes_matriculados) >= self.__capacidad_maxima:
            raise CapacidadMaximaAlcanzadaError(
                f"Error de cupo: El grupo {self.__codigo} "
                f"({self.__asignatura.get_nombre()}) alcanzó su capacidad máxima "
                f"de {self.__capacidad_maxima} estudiante(s)."
            )

        self.__estudiantes_matriculados.append(estudiante)
        print(
            f"Matrícula exitosa: {estudiante.get_nombre()} "
            f"({estudiante.get_codigo_estudiantil()}) inscrito en el grupo {self.__codigo}."
        )

    def retirar_estudiante(self, codigo_estudiantil):
        """
        Retira a un estudiante del grupo usando su código estudiantil.
        Lanza EstudianteNoMatriculadoError si no se encuentra inscrito.
        """
        for estudiante in self.__estudiantes_matriculados:
            if estudiante.get_codigo_estudiantil() == codigo_estudiantil:
                self.__estudiantes_matriculados.remove(estudiante)
                print(
                    f"Retiro exitoso: El estudiante {estudiante.get_nombre()} "
                    f"({codigo_estudiantil}) fue retirado del grupo {self.__codigo}."
                )
                return

        raise EstudianteNoMatriculadoError(
            f"Error de retiro: El estudiante con código '{codigo_estudiantil}' "
            f"no está matriculado en el grupo {self.__codigo}."
        )

    def mostrar_estudiantes(self):
        """Muestra la lista de estudiantes matriculados actualmente en el grupo."""
        print(
            f"Estudiantes matriculados en {self.__codigo} "
            f"({self.__asignatura.get_nombre()}):"
        )
        if not self.__estudiantes_matriculados:
            print("  - No hay estudiantes matriculados en este grupo.")
            return

        for indice, estudiante in enumerate(self.__estudiantes_matriculados, start=1):
            print(
                f"  {indice}. {estudiante.get_codigo_estudiantil()} - "
                f"{estudiante.get_nombre()} ({estudiante.get_programa().get_nombre()})"
            )
