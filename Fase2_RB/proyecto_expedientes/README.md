Sistema de Expedientes Digitales

Hospital de Diagnóstico · Proyecto académico — Fase 2

1. Descripción del proyecto
El sistema permite registrar, consultar, editar y eliminar empleados, así como verificar el estado de tres documentos administrativos: DUI, antecedentes y carné de la Junta de Vigilancia. 

2. Funcionamiento del sistema
Flask gestiona las rutas y procesa los datos enviados por los formularios HTML. SQLite almacena la información en documentos.db, mientras que static/style.css controla la presentación visual de las páginas.

El archivo app.py contiene las funciones principales. Por su parte, crear_bd.py crea la tabla documentos e inserta seis registros de ejemplo si la tabla está vacía. Las vistas HTML se encuentran en templates/.

Operaciones disponibles
La aplicación implementa creación de expedientes, consulta de empleados, actualización de datos y eliminación de registros.

3. Resumen y clasificación documental
La ruta /resumen recorre los registros mediante un ciclo for y emplea condiciones if/elif/else y contadores para clasificar los expedientes según los documentos con estado Entregado.

- Completo: tres documentos entregados.
- Incompleto: uno o dos documentos entregados.
- Sin documentos: ningún documento entregado.

4. Instalación y ejecución
Requisitos
Se requiere Python y la biblioteca Flask.

python -m pip install flask
python crear_bd.py
python app.py

- Listado de empleados: http://127.0.0.1:5000/empleados
- Registro de empleados: http://127.0.0.1:5000/empleados/nuevo
- Resumen documental: http://127.0.0.1:5000/resumen
La ruta raíz / no está definida, por lo que http://127.0.0.1:5000/ muestra un error 404. 

5. Base de datos y estructura de archivos
La base de datos documentos.db contiene la tabla documentos, con los campos id, nombre, dui, estado_dui, estado_antecedentes y estado_carnet_junta. Los estados posibles son Entregado, Pendiente y Vencido.

Los archivos principales son app.py (lógica y rutas), crear_bd.py (creación y carga inicial de la base de datos), templates/empleados.html, templates/nuevo.html, templates/editar.html, templates/resumen.html (vistas) y static/style.css (estilos).

6. Pruebas de funcionamiento
Se contemplan siete pruebas funcionales: consulta del listado, registro válido, registro con campo obligatorio vacío, edición válida, edición con campo obligatorio vacío, eliminación y verificación del resumen documental.
Las evidencias se presentan en un PDF independiente, indicando para cada prueba los datos de entrada, el resultado esperado, el resultado obtenido, la URL completa y una captura de pantalla. Los resultados deben documentarse conforme a las pruebas realmente ejecutadas.

7. Trabajo colaborativo y repositorio

Pedro Reyes: Responsable de diseñar y crear la base de datos SQLite, implementar el archivo crear_bd.py para generar la tabla documentos e insertar los registros iniciales mediante SQL. 

Gabriel Avalos: Implementación de la conexión entre Flask y SQLite. Creación de la ruta /empleados para consultar los registros mediante SQL y desarrollo de visualización en una plantilla HTML. 

Pedro Valle:
Responsable de implementar la ruta /empleados/nuevo, desarrollar el formulario HTML para registrar empleados y procesar los datos mediante Flask.

Daniel Brisuela:
Responsable de implementar las rutas para editar y eliminar empleados, desarrollar los formularios necesarios y ejecutar las consultas SQL para modificar o eliminar registros de la base de datos. 

Rodrigo Burgos:
Responsable de implementar la ruta /resumen, desarrollar la clasificación de documentos mediante ciclos, condiciones y contadores, y presentar los resultados en una plantilla HTML. Asimismo, contribución al diseño visual mediante CSS.
