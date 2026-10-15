
import sqlite3
from pathlib import Path

# Ruta de la base de datos
RUTA_DB = Path(__file__).resolve().parent / "documentos.db"


def crear_base_datos():
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    # Crear tabla para controlar la documentación
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_completo TEXT NOT NULL,
            dui TEXT UNIQUE NOT NULL,
            estado_dui TEXT NOT NULL DEFAULT 'Pendiente',
            estado_antecedentes TEXT NOT NULL DEFAULT 'Pendiente',
            estado_carnet_junta TEXT NOT NULL DEFAULT 'Pendiente',
            observaciones TEXT DEFAULT '',
            fecha_registro TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente.")
    print("Tabla documentos lista para recibir información.")


if __name__ == "__main__":
    crear_base_datos()
