# Resumen con lógica, estilos CSS y documentación Rodrigo Burgos

# Ruta de resumen (`/resumen`)
- Se creó la ruta `/resumen` en `app.py`.
- La ruta recorre todos los registros de la base de datos con un bucle `for`.
- Cada expediente se clasifica con `if/elif/else` según cuántos documentos tiene entregados:
  - **Completo:** los 3 documentos entregados.
  - **Incompleto:** 1 o 2 documentos entregados.
  - **Sin documentos:** ninguno entregado.
- Cada clasificación tiene su propio contador. También se muestran el total de expedientes y el porcentaje de completos.
- Los resultados se muestran en la plantilla `templates/resumen.html`.

# Hoja de estilos 
- Todas las páginas usan la misma hoja de estilos externa, para que el sitio tenga una sola identidad visual.
- Cada clasificación del resumen tiene un color distinto: verde para completo, ámbar para incompleto y rojo para sin documentos.


