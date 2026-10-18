**Sistema de Gestión Académica**

**Integrantes:**

* Legna Liliana Ferreira Rosas
* Juan David Perdomo Rojas

**Asignatura:** Programación I
**Universidad:** Universidad de Manizales

**Descripción general:**
Sistema en Python, desarrollado con Programación Orientada a Objetos, que gestiona estudiantes, docentes, administrativos, programas académicos y asignaturas. Es un único proyecto que integra todas las fases de la actividad.

**Estructura de archivos:**

* main.py: programa principal. Crea los objetos, demuestra las validaciones y el polimorfismo.
* persona.py: clase base Persona.
* estudiante.py: clase Estudiante (hereda de Persona).
* docente.py: clase Docente (hereda de Persona).
* administrativo.py: clase Administrativo (hereda de Persona).
* programa\_academico.py: clase ProgramaAcademico.
* asignatura.py: clase Asignatura.

**Ejecución:**
Requiere Python 3. Desde la carpeta del proyecto ejecutar:

&#x20;   python main.py



**Encapsulamiento:**
Todos los atributos son privados y se consultan o modifican mediante métodos get y set. Los métodos set validan los datos: el correo no puede ser vacío, los semestres, créditos y horas deben ser mayores que cero y el promedio debe estar entre 0 y 5. Si el valor no es válido se informa el error y el dato no se modifica.

**Herencia:**
Estudiante, Docente y Administrativo heredan de Persona, que contiene la información común (identificación, nombre y correo). Cada subclase llama a super().**init**() y agrega sus atributos propios.

**Sobrescritura:**
Cada subclase redefine mostrar\_informacion(), que muestra los datos generales mediante super() y agrega los propios, y realizar\_actividad\_principal(), que produce un resultado distinto para cada tipo de persona.

**Polimorfismo:**
En main.py se crea una única lista con dos estudiantes, dos docentes y dos administrativos. Se recorre con un solo ciclo for que invoca mostrar\_informacion() y realizar\_actividad\_principal(), sin condicionales por tipo. Python ejecuta automáticamente la versión que corresponde a cada objeto.

**Declaración de uso de IA**

Los estudiantes utilizaron una herramienta de IA para la revisión de código, oportunidades de mejora y capacidad de comprensión del código mediante aprendizaje en la práctica, por lo cual, los integrantes del grupo comprenden la sintaxis del código y su funcionamiento

