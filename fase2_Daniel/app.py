import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Función centralizada de conexión (Parte de Gabriel Ávalos)
def conectar():
    conexion = sqlite3.connect("documentos.db")
    conexion.row_factory = sqlite3.Row
    return conexion

# Ruta de consulta / listado (Parte de Gabriel Ávalos)
@app.route('/empleados')
def listar_empleados():
    conexion = conectar()
    try:
        empleados = conexion.execute('SELECT * FROM documentos ORDER BY id DESC').fetchall()
    finally:
        conexion.close()
    return render_template('empleados.html', empleados=empleados)

# Ruta de registro (Parte de Pedro Valle)
@app.route('/empleados/nuevo', methods=['GET', 'POST'])
def nuevo_empleado():
    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        dui = request.form.get('dui', '').strip()
        estado_dui = request.form.get('estado_dui', '').strip()
        estado_antecedentes = request.form.get('estado_antecedentes', '').strip()
        estado_carnet_junta = request.form.get('estado_carnet_junta', '').strip()

        if not nombre or not dui or not estado_dui or not estado_antecedentes or not estado_carnet_junta:
            error = "Todos los campos son obligatorios."
            return render_template('nuevo.html', error=error)

        conexion = conectar()
        try:
            conexion.execute('''
                INSERT INTO documentos (nombre, dui, estado_dui, estado_antecedentes, estado_carnet_junta)
                VALUES (?, ?, ?, ?, ?)
            ''', (nombre, dui, estado_dui, estado_antecedentes, estado_carnet_junta))
            conexion.commit()
        finally:
            conexion.close()
        
        return redirect('/empleados')

    return render_template('nuevo.html', error=error)

#Mi Parte:(Modificación y Eliminación)

@app.route('/empleados/editar/<int:id>', methods=['GET', 'POST'])
def editar_empleado(id):
    conexion = conectar()
    error = None

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        dui = request.form.get('dui', '').strip()
        estado_dui = request.form.get('estado_dui', '').strip()
        estado_antecedentes = request.form.get('estado_antecedentes', '').strip()
        estado_carnet_junta = request.form.get('estado_carnet_junta', '').strip()

        if not nombre or not dui or not estado_dui or not estado_antecedentes or not estado_carnet_junta:
            error = "Todos los campos son obligatorios para actualizar el registro."
            empleado = conexion.execute('SELECT * FROM documentos WHERE id = ?', (id,)).fetchone()
            conexion.close()
            return render_template('editar.html', empleado=empleado, error=error)

        try:
            conexion.execute('''
                UPDATE documentos 
                SET nombre = ?, dui = ?, estado_dui = ?, estado_antecedentes = ?, estado_carnet_junta = ?
                WHERE id = ?
            ''', (nombre, dui, estado_dui, estado_antecedentes, estado_carnet_junta, id))
            conexion.commit()
            conexion.close()
            return redirect('/empleados')
        except sqlite3.Error as e:
            error = f"Error al actualizar: {e}"
            empleado = conexion.execute('SELECT * FROM documentos WHERE id = ?', (id,)).fetchone()
            conexion.close()
            return render_template('editar.html', empleado=empleado, error=error)

    empleado = conexion.execute('SELECT * FROM documentos WHERE id = ?', (id,)).fetchone()
    conexion.close()

    if empleado is None:
        return "Registro no encontrado", 404

    return render_template('editar.html', empleado=empleado, error=error)


@app.route('/empleados/eliminar/<int:id>', methods=['POST'])
def eliminar_empleado(id):
    conexion = conectar()
    try:
        conexion.execute('DELETE FROM documentos WHERE id = ?', (id,))
        conexion.commit()
    finally:
        conexion.close()

    return redirect('/empleados')

if __name__ == '__main__':
    app.run(debug=True)