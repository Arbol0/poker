import sqlite3 as sql
DATBASE_NAME = "database.db"


def get_db():
    conn = sql
    try:
        conn = sql.connect(DATBASE_NAME)
    except Exception as e:
        print('Error en la conexion')
    return conn
