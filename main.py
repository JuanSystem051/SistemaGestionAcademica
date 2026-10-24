from persona import Persona
from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo
from horario import Horario
from grupo_academico import GrupoAcademico
from excepciones import (
    EstudianteYaMatriculadoError,
    CapacidadMaximaAlcanzadaError,
    EstudianteNoMatriculadoError,
    AsignaturaNoEncontradaError,
    ProgramaAcademicoNoEncontradoError,
)

# =====================================
# PRUEBA 1: CLASE ABSTRACTA PERSONA
# =====================================

print("\n===== PRUEBA DE CLASE ABSTRACTA (PERSONA) =====")
try:
    persona_invalida = Persona("0000", "Usuario Genérico", "usuario@umanizales.edu.co")
except TypeError as error:
    print(f"No es posible instanciar directamente la clase abstracta Persona: {error}")

# =====================================
# CREACIÓN DE PROGRAMAS ACADÉMICOS
# =====================================

sistemas = ProgramaAcademico(
    "ING01",
    "Ingeniería de Sistemas",
    "Facultad de Ingeniería",
    10
)

administracion = ProgramaAcademico(
    "ADM01",
    "Administración de Empresas",
    "Facultad de Ciencias Económicas",
    8
)

programas_sistema = [sistemas, administracion]

# =====================================
# CREACIÓN DE ASIGNATURAS
# =====================================

poo = Asignatura(
    "POO101",
    "Programación Orientada a Objetos",
    4,
    sistemas
)

base_datos = Asignatura(
    "BD102",
    "Bases de Datos",
    3,
    sistemas
)

asignaturas_sistema = [poo, base_datos]

# =====================================
# CREACIÓN DE ESTUDIANTES
# =====================================

estudiante1 = Estudiante(
    "1001",
    "Ana López",
    "analopez@umanizales.edu.co",
    "EST001",
    sistemas,
    3,
    4.5
)

estudiante2 = Estudiante(
    "1002",
    "Carlos Ruiz",
    "carlosruiz@umanizales.edu.co",
    "EST002",
    administracion,
    5,
    4.2
)

estudiante3 = Estudiante(
    "1003",
    "Sofía Martínez",
    "sofiamartinez@umanizales.edu.co",
    "EST003",
    sistemas,
    3,
    4.7
)

# =====================================
# CREACIÓN DE DOCENTES
# =====================================

docente1 = Docente(
    "2001",
    "Pedro Gómez",
    "pedrogomez@umanizales.edu.co",
    "DOC001",
    "Ingeniería",
    "Tiempo Completo",
    40
)

docente2 = Docente(
    "2002",
    "Laura Pérez",
    "lauraperez@umanizales.edu.co",
    "DOC002",
    "Ciencias Económicas",
    "Cátedra",
    20
)

# =====================================
# CREACIÓN DE ADMINISTRATIVOS
# =====================================

administrativo1 = Administrativo(
    "3001",
    "María Torres",
    "mariatorres@umanizales.edu.co",
    "ADM001",
    "Registro Académico",
    "Coordinadora",
    "Diurna"
)

administrativo2 = Administrativo(
    "3002",
    "Juan Castro",
    "juancastro@umanizales.edu.co",
    "ADM002",
    "Bienestar Universitario",
    "Auxiliar",
    "Nocturna"
)

# =====================================
# MOSTRAR INFORMACIÓN DE PROGRAMAS
# =====================================

print("\n===== PROGRAMAS ACADÉMICOS =====")
sistemas.mostrar_informacion()

print()
administracion.mostrar_informacion()

# =====================================
# MOSTRAR INFORMACIÓN DE ASIGNATURAS
# =====================================

print("\n===== ASIGNATURAS =====")
poo.mostrar_informacion()

print()
base_datos.mostrar_informacion()

# =====================================
# VALIDACIONES DE ENCAPSULAMIENTO
# =====================================

print("\n===== MODIFICACIONES VÁLIDAS =====")

estudiante1.set_correo("ana.lopez@umanizales.edu.co")
sistemas.set_numero_semestres(9)
poo.set_creditos(5)
estudiante1.set_semestre(4)
print(f"Nuevo correo: {estudiante1.get_correo()}")
print(f"Nuevos semestres: {sistemas.get_numero_semestres()}")
print(f"Nuevos créditos: {poo.get_creditos()}")
print(f"Nuevo semestre: {estudiante1.get_semestre()}")

print("\n===== INTENTOS DE VALORES INVÁLIDOS =====")

estudiante1.set_correo("")
sistemas.set_numero_semestres(0)
poo.set_creditos(-1)
estudiante1.set_promedio(7)
docente1.set_horas(0)

# =====================================
# POLIMORFISMO
# =====================================

print("\n===== PERSONAS DEL SISTEMA (POLIMORFISMO) =====")

personas = [
    estudiante1,
    estudiante2,
    estudiante3,
    docente1,
    docente2,
    administrativo1,
    administrativo2
]

for persona in personas:
    print("\n---------------------------")
    persona.mostrar_informacion()
    persona.realizar_actividad_principal()

# =====================================
# CREACIÓN DE HORARIOS Y GRUPOS ACADÉMICOS
# =====================================

print("\n===== CREACIÓN DE HORARIOS Y GRUPOS ACADÉMICOS =====")

horario_poo = Horario("Lunes y Miércoles", "08:00", "10:00", "Salón B-201")
horario_bd = Horario("Martes y Jueves", "14:00", "16:00", "Laboratorio C-105")

grupo_poo_01 = GrupoAcademico("GRP-POO-01", poo, docente1, 2, horario_poo)
grupo_bd_01 = GrupoAcademico("GRP-BD-01", base_datos, docente1, 3, horario_bd)

grupo_poo_01.mostrar_informacion_grupo()
print()
grupo_bd_01.mostrar_informacion_grupo()

# =====================================
# MATRÍCULA CORRECTA DE ESTUDIANTES
# =====================================

print("\n===== MATRÍCULA DE ESTUDIANTES =====")

try:
    grupo_poo_01.matricular_estudiante(estudiante1)
    grupo_poo_01.matricular_estudiante(estudiante2)
    grupo_bd_01.matricular_estudiante(estudiante1)
    grupo_bd_01.matricular_estudiante(estudiante3)
except (EstudianteYaMatriculadoError, CapacidadMaximaAlcanzadaError) as error:
    print(error)

print()
grupo_poo_01.mostrar_informacion_grupo()
grupo_poo_01.mostrar_estudiantes()

print()
grupo_bd_01.mostrar_informacion_grupo()
grupo_bd_01.mostrar_estudiantes()

# =====================================
# EXCEPCIÓN: ESTUDIANTE DUPLICADO
# =====================================

print("\n===== PRUEBA: MATRÍCULA DE ESTUDIANTE DUPLICADO =====")
try:
    grupo_poo_01.matricular_estudiante(estudiante1)
except EstudianteYaMatriculadoError as error:
    print(error)

# =====================================
# EXCEPCIÓN: SUPERAR CAPACIDAD MÁXIMA
# =====================================

print("\n===== PRUEBA: SUPERAR CAPACIDAD MÁXIMA DEL GRUPO =====")
try:
    grupo_poo_01.matricular_estudiante(estudiante3)
except CapacidadMaximaAlcanzadaError as error:
    print(error)

# =====================================
# RETIRO CORRECTO DE UN ESTUDIANTE
# =====================================

print("\n===== RETIRO CORRECTO DE ESTUDIANTE =====")
try:
    grupo_poo_01.retirar_estudiante("EST002")
    grupo_poo_01.mostrar_estudiantes()
except EstudianteNoMatriculadoError as error:
    print(error)

# =====================================
# EXCEPCIÓN: RETIRO DE ESTUDIANTE INEXISTENTE
# =====================================

print("\n===== PRUEBA: RETIRO DE ESTUDIANTE NO MATRICULADO =====")
try:
    grupo_poo_01.retirar_estudiante("EST999")
except EstudianteNoMatriculadoError as error:
    print(error)

# =====================================
# BÚSQUEDA DE ASIGNATURA (EXISTENTE E INEXISTENTE)
# =====================================

print("\n===== PRUEBA: BÚSQUEDA DE ASIGNATURA =====")
try:
    asignatura_encontrada = Asignatura.buscar_asignatura(asignaturas_sistema, "POO101")
    print(f"Asignatura encontrada: {asignatura_encontrada.get_nombre()}")
    Asignatura.buscar_asignatura(asignaturas_sistema, "FIS999")
except AsignaturaNoEncontradaError as error:
    print(error)

# =====================================
# BÚSQUEDA DE PROGRAMA (EXISTENTE E INEXISTENTE)
# =====================================

print("\n===== PRUEBA: BÚSQUEDA DE PROGRAMA ACADÉMICO =====")
try:
    programa_encontrado = ProgramaAcademico.buscar_programa(programas_sistema, "ING01")
    print(f"Programa encontrado: {programa_encontrado.get_nombre()}")
    ProgramaAcademico.buscar_programa(programas_sistema, "MED99")
except ProgramaAcademicoNoEncontradoError as error:
    print(error)

print("\n===== FIN DE LA EJECUCIÓN: EL SISTEMA CONTINUÓ NORMALMENTE =====")
