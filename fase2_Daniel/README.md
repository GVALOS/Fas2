### Mantenimientos de Modificación y Eliminación (Daniel Brizuela)

#### Rutas Implementadas:
- `/empleados/editar/<int:id>` (`GET` y `POST`):
  - **GET**: Consulta la base de datos buscando el registro correspondiente al ID mediante `SELECT * FROM documentos WHERE id = ?` y precarga los datos actuales dentro del formulario de la plantilla `templates/editar.html`.
  - **POST**: Valida la presencialidad de los datos enviados por el usuario y actualiza los registros mediante la sentencia SQL parametrizada `UPDATE documentos SET nombre = ?, dui = ?, estado_dui = ?, estado_antecedentes = ?, estado_carnet_junta = ? WHERE id = ?`.
- `/empleados/eliminar/<int:id>` (`POST`):
  - Recibe el ID del registro y ejecuta la eliminación del expediente de forma segura mediante la sentencia `DELETE FROM documentos WHERE id = ?`.

#### Componentes de Interfaz Asociados:
1. **`templates/editar.html`**: Formulario web con los campos del empleado precargados, enlazado a la hoja de estilos externa (`style.css`), que permite modificar los estados de los documentos.
2. **Botones de Acción en `templates/empleados.html`**: Se integró una columna de acciones en la tabla principal con un enlace/botón de **Editar** y un formulario con botón de **Eliminar** para cada registro de la lista.

#### Medidas de Seguridad Aplicadas:
1. **Prevención de Inyección SQL**: Todas las consultas SQL (`SELECT`, `UPDATE`, `DELETE`) utilizan parametrización mediante el signo de interrogación (`?`), evitando por completo la concatenación directa de variables escritas por el usuario.
2. **Uso Estricto de la Cláusula WHERE**: Tanto la sentencia `UPDATE` como la sentencia `DELETE` incluyen explícitamente `WHERE id = ?` para asegurar que las operaciones afecten únicamente al registro seleccionado y prevenir alteraciones o borrados masivos en la tabla.
3. **Confirmación de Acción del Usuario**: Se implementó una alerta de confirmación vía JavaScript (`onsubmit="return confirm(...)"`) en el botón de eliminar para evitar borrados accidentales antes de procesar la petición POST.