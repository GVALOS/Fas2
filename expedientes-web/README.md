Documentación del Módulo de Registro y Validación de Expedientes

1. Descripción

El Módulo de Registro y Validación de Expedientes es la funcionalidad desarrollada para la captura de nuevos registros en el sistema web de gestión documental hospitalaria. Su función principal es recibir los datos ingresados por el usuario mediante un formulario web, validar la presencia de la información obligatoria y registrar los expedientes de forma segura en la base de datos documentos.db.

Este módulo está compuesto por la ruta /empleados/nuevo implementada en Flask (app.py) y la plantilla HTML correspondiente (templates/nuevo.html).

2. Componentes del Módulo

2.1 Ruta y Lógica Backend (app.py)

La función nuevo_empleado() gestiona las peticiones GET y POST para la ruta /empleados/nuevo:

Petición GET: Carga e interactúa con el formulario en blanco para el registro.

Petición POST: Procesa los datos del formulario, realiza la validación de presencia de datos y los inserta en SQLite mediante consultas parametrizadas.

2.2 Formulario e Interfaz Frontend (templates/nuevo.html)

La vista del usuario incluye los siguientes elementos de captura:

Nombre Completo: Campo de texto obligatorio.

DUI: Campo de texto obligatorio con formato de identidad.

Estado DUI: Menú desplegable (Entregado / Pendiente).

Estado Antecedentes: Menú desplegable (Entregado / Pendiente).

Estado Carnet Junta: Menú desplegable (Entregado / Pendiente).

Observaciones: Campo de texto opcional.

3. Validaciones y Control de Errores

Campos Obligatorios: El backend valida que los campos nombre_completo, dui, estado_dui, estado_antecedentes y estado_carnet_junta no contengan cadenas vacías o solo espacios en blanco (strip()).

Preservación de Datos: En caso de error de validación o fallo en el registro, los datos ingresados previamente se conservan en el formulario para evitar que el usuario vuelva a escribirlos.

Manejo de Excepciones: Captura posibles errores de base de datos (por ejemplo, restricción de DUI duplicado) y los despliega como mensajes de alerta legibles en la pantalla.

Consultas Seguras: La inserción de datos se ejecuta utilizando comodines ? para prevenir vulnerabilidades de inyección SQL.

4. Flujo de Datos

El usuario accede a la dirección /empleados/nuevo.

Completa los datos requeridos y presiona el botón "Guardar Registro".

La solicitud POST es enviada al servidor Flask.

El servidor valida la integridad de los datos:

Si faltan datos o se produce un error: Retorna a la pantalla nuevo.html mostrando un mensaje de error explicativo.

Si los datos son válidos: Inserta la información en la tabla documentos, guarda los cambios mediante commit() y redirige al usuario a la vista principal (/empleados).

5. Consideraciones Tecnológicas

Integración con Flask: Utiliza los métodos request.form.get() para la lectura de parámetros y render_template() / redirect() para la navegación.

Persistencia en SQLite: Se conecta a la base de datos utilizando la función auxiliar conectar(), asegurando el cierre de la conexión al finalizar la operación.

Compatibilidad con Plantillas: Hace uso del motor Jinja2 para la inyección condicional de alertas y renderizado de valores previos.

6. Conclusión

El Módulo de Registro y Validación garantiza una entrada de datos ordenada y confiable dentro del sistema. Su implementación previene la inserción de registros incompletos o corruptos y ofrece una interfaz intuitiva que facilita la labor del personal administrativo en la gestión de expedientes.
