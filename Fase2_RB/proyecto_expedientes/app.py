import os
import re
import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
RUTA_BD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "documentos.db")

def conectar():
    conexion = sqlite3.connect(RUTA_BD)
    conexion.row_factory = sqlite3.Row
    return conexion

# Expresión regular para validar el DUI de El Salvador
PATRON_DUI = re.compile(r'^\d{8}-\d{1}$')

@app.route('/empleados')
def listar_empleados():
    conexion = conectar()
    try:
        empleados = conexion.execute('SELECT * FROM documentos ORDER BY id DESC').fetchall()
    finally:
        conexion.close()
    return render_template('empleados.html', empleados=empleados)

@app.route('/empleados/nuevo', methods=['GET', 'POST'])
def nuevo_empleado():
    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        dui = request.form.get('dui', '').strip()
        perfil = request.form.get('perfil', 'General').strip()
        estado_dui = request.form.get('estado_dui', '').strip()
        estado_antecedentes = request.form.get('estado_antecedentes', '').strip()
        estado_carnet_junta = request.form.get('estado_carnet_junta', '').strip()
        
        if not nombre or not dui or not estado_dui or not estado_antecedentes or not estado_carnet_junta:
            error = "Todos los campos son obligatorios."
            return render_template('nuevo.html', error=error)
        
        # Validación estricta del formato DUI
        if not PATRON_DUI.match(dui):
            error = "El formato del DUI es inválido. Debe ser de la forma 00000000-0."
            return render_template('nuevo.html', error=error)

        conexion = conectar()
        try:
            conexion.execute('''
                INSERT INTO documentos (nombre, dui, perfil, estado_dui, estado_antecedentes, estado_carnet_junta)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nombre, dui, perfil, estado_dui, estado_antecedentes, estado_carnet_junta))
            conexion.commit()
        finally:
            conexion.close()
        
        return redirect('/empleados')
    return render_template('nuevo.html', error=error)

@app.route('/empleados/editar/<int:id>', methods=['GET', 'POST'])
def editar_empleado(id):
    conexion = conectar()
    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        dui = request.form.get('dui', '').strip()
        perfil = request.form.get('perfil', 'General').strip()
        estado_dui = request.form.get('estado_dui', '').strip()
        estado_antecedentes = request.form.get('estado_antecedentes', '').strip()
        estado_carnet_junta = request.form.get('estado_carnet_junta', '').strip()
        
        if not nombre or not dui or not estado_dui or not estado_antecedentes or not estado_carnet_junta:
            error = "Todos los campos son obligatorios para actualizar el registro."
            empleado = conexion.execute('SELECT * FROM documentos WHERE id = ?', (id,)).fetchone()
            conexion.close()
            return render_template('editar.html', empleado=empleado, error=error)
            
        if not PATRON_DUI.match(dui):
            error = "El formato del DUI es inválido. Debe ser de la forma 00000000-0."
            empleado = conexion.execute('SELECT * FROM documentos WHERE id = ?', (id,)).fetchone()
            conexion.close()
            return render_template('editar.html', empleado=empleado, error=error)

        try:
            conexion.execute('''
                UPDATE documentos 
                SET nombre = ?, dui = ?, perfil = ?, estado_dui = ?, estado_antecedentes = ?, estado_carnet_junta = ?
                WHERE id = ?
            ''', (nombre, dui, perfil, estado_dui, estado_antecedentes, estado_carnet_junta, id))
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

@app.route('/resumen')
def resumen():
    conexion = conectar()
    try:
        registros = conexion.execute('SELECT * FROM documentos ORDER BY id').fetchall()
    finally:
        conexion.close()
        
    completos = 0
    incompletos = 0
    sin_documentos = 0
    detalle = []
    
    for registro in registros:
        entregados = 0
        for campo in ('estado_dui', 'estado_antecedentes', 'estado_carnet_junta'):
            if registro[campo].strip().lower() == 'entregado':
                entregados += 1
                
        if entregados == 3:
            estado = 'Completo'
            clase = 'completo'
            completos += 1
        elif entregados > 0:
            estado = 'Incompleto'
            clase = 'incompleto'
            incompletos += 1
        else:
            estado = 'Sin documentos'
            clase = 'sin-documentos'
            sin_documentos += 1
            
        detalle.append({
            'id': registro['id'],
            'nombre': registro['nombre'],
            'dui': registro['dui'],
            'perfil': registro['perfil'],
            'entregados': entregados,
            'estado': estado,
            'clase': clase,
        })
        
    total = len(registros)
    porcentaje_completos = round(completos / total * 100) if total > 0 else 0
    
    return render_template(
        'resumen.html',
        detalle=detalle,
        total=total,
        completos=completos,
        incompletos=incompletos,
        sin_documentos=sin_documentos,
        porcentaje_completos=porcentaje_completos,
    )

if __name__ == '__main__':
    app.run(debug=True)
