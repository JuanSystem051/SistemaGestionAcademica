# Sistema de Gestión Académica

**Integrantes:**
* Legna Liliana Ferreira Rosas
* Juan David Perdomo Rojas

**Asignatura:** Programación I  
**Universidad:** Universidad de Manizales

---

## Descripción General
Sistema en Python desarrollado bajo los principios de la Programación Orientada a Objetos (POO) que gestiona personas vinculadas a la universidad (estudiantes, docentes y administrativos), programas académicos, asignaturas, horarios y oferta de grupos académicos con procesos de matrícula y retiro.

El proyecto corresponde a un único sistema evolutivo que integra la **Actividad Colaborativa N°1** (clases, constructores, encapsulamiento, herencia, sobrescritura y polimorfismo) y la **Actividad Colaborativa N°2** (clases abstractas, relación de composición y control de excepciones personalizadas).

---

## Estructura de Archivos

* `main.py`: Programa principal. Ejecuta todas las pruebas del sistema: imposibilidad de instanciar `Persona`, creación de objetos, validaciones de encapsulamiento, recorrido polimórfico, gestión de grupos académicos, matrículas, retiros y manejo de excepciones personalizadas.
* `persona.py`: Clase base abstracta `Persona` (`ABC`).
* `estudiante.py`: Clase `Estudiante` (hereda de `Persona`).
* `docente.py`: Clase `Docente` (hereda de `Persona`).
* `administrativo.py`: Clase `Administrativo` (hereda de `Persona`).
* `programa_academico.py`: Clase `ProgramaAcademico` con búsqueda por código.
* `asignatura.py`: Clase `Asignatura` con búsqueda por código.
* `horario.py`: Clase `Horario` que modela día, hora de inicio, hora de finalización y salón.
* `grupo_academico.py`: Clase `GrupoAcademico` que organiza la oferta académica y el proceso de matrícula.
* `excepciones.py`: Clases de excepciones personalizadas del dominio académico.

---

## Ejecución
Requiere Python 3. Desde la carpeta del proyecto ejecutar:

```bash
python main.py
```

---

## Conceptos de POO Aplicados

### 1. Encapsulamiento
Todos los atributos de las clases son privados (`__`) y se consultan o modifican mediante métodos `get` y `set`. Los métodos `set` validan los datos antes de asignarlos (correos y textos no vacíos, semestres/créditos/horas/cupos mayores que cero y promedio entre `0.0` y `5.0`).

### 2. Herencia y Clases Abstractas
En el dominio universitario no tiene sentido registrar una persona genérica sin definir su rol específico. Por ello, `Persona` se declara como una **clase abstracta** (`class Persona(ABC)`) y define `realizar_actividad_principal()` con el decorador `@abstractmethod`. Esto impide instanciar directamente objetos de tipo `Persona` y obliga a las subclases `Estudiante`, `Docente` y `Administrativo` a implementar su propio comportamiento especializado.

### 3. Sobrescritura y Polimorfismo
Cada subclase de `Persona` sobrescribe `mostrar_informacion()` (invocando `super().mostrar_informacion()` y añadiendo sus atributos particulares) y `realizar_actividad_principal()`. En `main.py` se recorre una única lista heterogénea `personas` con un ciclo `for`, sin condicionales por tipo, ejecutando polimórficamente el comportamiento correspondiente a cada objeto.

### 4. Relación de Composición (`GrupoAcademico` y `Horario`)
Un `GrupoAcademico` **contiene** un objeto `Horario` que define los días, horas de inicio y finalización, y el salón donde se desarrolla el curso:
* **¿Por qué el grupo académico contiene un horario?** Porque el horario hace parte estructural de la organización de un grupo ofertado (relación *"tiene un"* / *parte-todo*): cada grupo posee su propia programación horaria expresada como un objeto con atributos propios (`dia`, `hora_inicio`, `hora_finalizacion`, `salon`), evitando representarla como una simple cadena de texto aislada. Además, el constructor de `GrupoAcademico` instancia y encapsula internamente su propio objeto `Horario`, de modo que el ciclo de vida del horario queda ligado al grupo.
* **¿Por qué esta relación NO corresponde a herencia?** La herencia modela relaciones de tipo *"es un"* (generalización/especialización), como `Estudiante` *es una* `Persona`. Un `GrupoAcademico` **no es un** `Horario`, ni un `Horario` es un tipo de `GrupoAcademico`; son conceptos de distinta naturaleza donde el horario actúa como un componente interno que describe cuándo y dónde funciona el grupo.

### 5. Excepciones Personalizadas
El módulo `excepciones.py` define cinco excepciones propias que heredan de `Exception`:
* `EstudianteYaMatriculadoError`: Lanzada en `GrupoAcademico.matricular_estudiante()` cuando el estudiante ya está inscrito en el grupo.
* `CapacidadMaximaAlcanzadaError`: Lanzada en `GrupoAcademico.matricular_estudiante()` cuando el grupo alcanzó su cupo máximo.
* `EstudianteNoMatriculadoError`: Lanzada en `GrupoAcademico.retirar_estudiante()` cuando el código estudiantil no figura entre los matriculados del grupo.
* `AsignaturaNoEncontradaError`: Lanzada en `Asignatura.buscar_asignatura()` cuando el código buscado no existe.
* `ProgramaAcademicoNoEncontradoError`: Lanzada en `ProgramaAcademico.buscar_programa()` cuando el código buscado no existe.

Todas las excepciones son capturadas en `main.py` mediante bloques `try / except`, mostrando mensajes claros y permitiendo que el programa continúe su ejecución normal.

---

## Declaración de Uso de IA
Los estudiantes utilizaron una herramienta de IA como apoyo para la revisión de código, estructuración documental, identificación de oportunidades de mejora y fortalecimiento de la comprensión práctica de los conceptos de clases abstractas, composición y manejo de excepciones en Python, por lo cual los integrantes del equipo comprenden la sintaxis del código, su diseño y su funcionamiento.
