from flask import Flask, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)


RUTA_DB = Path(__file__).resolve().parent / "documentos.db"


#Conectando con Base de Datos
def conectar():
    conexion = sqlite3.connect(RUTA_DB)
    conexion.row_factory = sqlite3.Row
    return conexion


  #Consultando datos registrados

@app.route("/empleados")
def listar_empleados():
    conexion = conectar()

    try:
        empleados = conexion.execute("""
            SELECT *
            FROM documentos
            ORDER BY id DESC
        """).fetchall()

    finally:
        conexion.close()

    return render_template(
        "empleados.html",
        empleados=empleados
    )


# Verificando el __name__ para correr

if __name__ == "__main__":
    app.run(debug=True)
