# Documentación de la Base de Datos `documentos.db`

## 1. Descripción

La base de datos `documentos.db` está diseñada para gestionar la documentación del personal de un hospital. Su función principal es almacenar los datos de identificación de cada persona y controlar el estado de sus documentos administrativos: DUI, antecedentes y carné de la Junta de Vigilancia.

La base de datos utiliza SQLite y comienza vacía, preparada para recibir nuevos registros.

## 2. Tabla principal: `documentos`

La base de datos contiene una tabla denominada `documentos`, encargada de almacenar la información de cada expediente.

### Estructura de los campos

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

## 3. Restricciones y valores predeterminados

- **Clave primaria:** el campo `id` identifica de manera única cada registro y aumenta automáticamente.
- **Campos obligatorios:** `nombre_completo`, `dui` y los tres campos de estado no pueden quedar vacíos.
- **DUI único:** el campo `dui` tiene una restricción `UNIQUE` para impedir la duplicación de números de identidad.
- **Estados iniciales:** los campos `estado_dui`, `estado_antecedentes` y `estado_carnet_junta` tienen el valor predeterminado `Pendiente`.
- **Observaciones:** el campo `observaciones` comienza con una cadena vacía si no se proporciona información.
- **Fecha de registro:** el campo `fecha_registro` utiliza `CURRENT_TIMESTAMP` para establecer automáticamente la fecha y hora cuando se crea un registro sin especificar ese campo.

## 4. Estados de la documentación

Los campos de estado permiten identificar la situación de cada documento.

- **Pendiente:** el documento está pendiente de presentación o verificación.
- **Completo:** el documento ha sido presentado y verificado.
- **Vencido:** el documento requiere renovación, cuando corresponda.

Estos estados son valores de referencia; la estructura actual de la tabla no limita las entradas exclusivamente a estas opciones.

## 5. Inicialización

La base de datos se crea mediante el script `crear_bd.py`, utilizando el módulo `sqlite3` de Python.

La instrucción `CREATE TABLE IF NOT EXISTS` permite crear la tabla si todavía no existe, sin eliminar los registros almacenados previamente.

La base de datos no incluye registros de ejemplo y queda disponible para almacenar información nueva.

## 6. Consideraciones

- El campo `dui` se almacena como texto para conservar su formato.
- La base de datos registra el estado de los documentos, pero no almacena sus archivos digitales.
- La fecha de registro corresponde al momento de creación del registro, no necesariamente a la fecha de actualización.
- La información almacenada debe protegerse, ya que contiene datos personales y de identificación.

## 7. Conclusión

La base de datos `documentos.db` proporciona una estructura organizada para registrar y controlar la documentación del personal hospitalario. Su diseño permite identificar a cada persona, consultar el estado de sus documentos y agregar observaciones para facilitar el seguimiento administrativo de los expedientes.
