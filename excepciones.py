class EstudianteYaMatriculadoError(Exception):
    """Excepción lanzada cuando se intenta matricular a un estudiante que ya pertenece al grupo."""
    pass


class CapacidadMaximaAlcanzadaError(Exception):
    """Excepción lanzada cuando se intenta matricular a un estudiante en un grupo sin cupos disponibles."""
    pass


class EstudianteNoMatriculadoError(Exception):
    """Excepción lanzada cuando se intenta retirar a un estudiante que no está inscrito en el grupo."""
    pass


class AsignaturaNoEncontradaError(Exception):
    """Excepción lanzada cuando se busca una asignatura cuyo código no existe en el sistema."""
    pass


class ProgramaAcademicoNoEncontradoError(Exception):
    """Excepción lanzada cuando se busca un programa académico cuyo código no existe en el sistema."""
    pass
