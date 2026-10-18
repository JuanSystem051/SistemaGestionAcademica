from programa_academico import ProgramaAcademico
from asignatura import Asignatura
from estudiante import Estudiante
from docente import Docente
from administrativo import Administrativo

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
# VALIDACIONES
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

print("\n===== PERSONAS DEL SISTEMA =====")

personas = [
    estudiante1,
    estudiante2,
    docente1,
    docente2,
    administrativo1,
    administrativo2
]

for persona in personas:

    print("\n---------------------------")

    persona.mostrar_informacion()
    persona.realizar_actividad_principal()