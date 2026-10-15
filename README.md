### Descripción

La base de datos `documentos.db` está diseñada para gestionar la documentación del personal de un hospital. Su función principal es almacenar los datos de identificación de cada persona y controlar el estado de sus documentos administrativos: DUI, antecedentes y carné de la Junta de Vigilancia.

La base de datos utiliza SQLite y se inicializa con cinco registros de ejemplo mediante `crear_bd.py`.

### Tabla principal: `documentos`

La base de datos contiene una tabla denominada `documentos`, encargada de almacenar la información de cada expediente.

**Estructura de los campos**

| Campo | Tipo de dato | Descripción |
|---|---|---|
| `id` | INTEGER | Identificador único generado automáticamente. |
| `nombre_completo` | TEXT | Nombre completo de la persona registrada. |
| `dui` | TEXT | Número del Documento Único de Identidad. |
| `estado_dui` | TEXT | Estado de la documentación del DUI. |
| `estado_antecedentes` | TEXT | Estado de los antecedentes. |
| `estado_carnet_junta` | TEXT | Estado del carné de la Junta de Vigilancia. |
| `observaciones` | TEXT | Comentarios adicionales sobre el expediente. |
| `fecha_registro` | TEXT | Fecha y hora de creación del registro. |

### Restricciones y valores predeterminados

- El campo `id` identifica de manera única cada registro y aumenta automáticamente.
- El campo `dui` tiene una restricción `UNIQUE` para impedir números repetidos.
-Los campos `estado_dui`, `estado_antecedentes` y `estado_carnet_junta` tienen el valor predeterminado `Pendiente`.
- El campo `fecha_registro` utiliza `CURRENT_TIMESTAMP` para establecer automáticamente la fecha y hora cuando se crea un registro.

### Estados de la documentación

Los campos de estado permiten identificar la situación de cada documento.

- **Pendiente:** el documento está pendiente de presentación o verificación.
- **Entregado:** el documento ha sido presentado.



### Inicialización — Pedro Reyes

La base de datos se crea mediante el script `crear_bd.py`, utilizando el módulo `sqlite3` de Python.

La instrucción `CREATE TABLE IF NOT EXISTS` permite crear la tabla si todavía no existe, sin eliminar los registros almacenados previamente.

El script utiliza `INSERT OR IGNORE INTO` para cargar cinco registros iniciales, evitando duplicaciones por DUI.

### Conexión y consulta — Gabriel Avalos

El archivo `app.py` configura la aplicación Flask y establece la conexión con `documentos.db` mediante la función `conectar()`.

La conexión utiliza `sqlite3.Row` para permitir el acceso a los campos por sus nombres.

La ruta `/empleados` ejecuta la consulta `SELECT * FROM documentos ORDER BY id DESC`, obteniendo los registros y ordenándolos por su identificador de forma descendente.

La función `render_template()` envía los resultados a `templates/empleados.html`, donde se muestran en una tabla con los ocho campos de cada empleado. El archivo HTML enlaza la hoja de estilos externa `static/style.css`.

### Ejecución

Para ejecutar el proyecto, se deben utilizar los siguientes comandos desde la terminal, dentro de la carpeta principal:

1-Instalar Flask:
    pip install flask
2-Crear la base de datos y cargar los registros iniciales:
    python crear_bd.py
3-Iniciar el servidor Flask:
    python app.py

Abrir la página de consulta en el navegador:

http://127.0.0.1:5000/empleados