
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
    # Agregar cinco registros de ejemplo
    registros_ejemplo = [
        ("Pedri Reyes", "00000001-1", "Entregado", "Entregado", "Entregado"),
        ("Gabrielson Hernández", "00000002-2", "Entregado", "Pendiente", "Pendiente"),
        ("Pietro Del Valle", "00000003-3", "Entregado", "Entregado", "Pendiente"),
        ("Rodrigo Burgaleta", "00000004-4", "Pendiente", "Pendiente", "Pendiente"),
        ("Dan Orihuela", "00000005-5", "Entregado", "Entregado", "Entregado")
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO documentos (
            nombre_completo,
            dui,
            estado_dui,
            estado_antecedentes,
            estado_carnet_junta
        )
        VALUES (?, ?, ?, ?, ?)
    """, registros_ejemplo)
    
    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente.")
    print("Tabla documentos lista para recibir información.")


if __name__ == "__main__":
    crear_base_datos()
