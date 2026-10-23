import sqlite3
from pathlib import Path

def crear_base_datos():
    db_path = Path(__file__).resolve().parent / "documentos.db"
    
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    
    # Se agrega la columna 'perfil' para ajustar el checklist según el puesto del empleado
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            dui TEXT NOT NULL,
            perfil TEXT NOT NULL DEFAULT 'General',
            estado_dui TEXT NOT NULL,
            estado_antecedentes TEXT NOT NULL,
            estado_carnet_junta TEXT NOT NULL
        )
    ''')
    
    registros_ejemplo = [
        ('Ana María Gómez', '02345678-9', 'Administrativo', 'Entregado', 'Entregado', 'Pendiente'),
        ('Carlos Alberto Pérez', '03456789-0', 'Médico', 'Pendiente', 'Entregado', 'Entregado'),
        ('María José Martínez', '04567891-2', 'Enfermería', 'Entregado', 'Pendiente', 'Pendiente'),
        ('Luis Fernando Ramírez', '05678912-3', 'Administrativo', 'Vencido', 'Vencido', 'Entregado'),
        ('Sofia Alejandra Rivas', '06789123-4', 'Médico', 'Entregado', 'Entregado', 'Entregado'),
        ('Jorge Enrique Castillo', '07891234-5', 'Enfermería', 'Pendiente', 'Pendiente', 'Vencido')
    ]
    
    cursor.execute("SELECT COUNT(*) FROM documentos")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO documentos (nombre, dui, perfil, estado_dui, estado_antecedentes, estado_carnet_junta)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', registros_ejemplo)
        print("Registros de ejemplo insertados correctamente.")
    
    conexion.commit()
    conexion.close()
    print("Base de datos creada con éxito.")

if __name__ == '__main__':
    crear_base_datos()
