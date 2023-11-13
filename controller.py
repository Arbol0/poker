from bd import get_db

l = """
        CREATE TABLE partida (
        id INTEGER PRIMARY KEY,
        ronda INTEGER NOT NULL
        ); """

r = """
        CREATE TABLE jugador (
        id INTEGER PRIMARY KEY,
        nombre VARCHAR(25) NOT NULL,
        dinero INTEGER NOT NULL,
        partida_FK INTEGER NULL,
        FOREIGN KEY(partida_FK) REFERENCES partida(id)
        ); """


def insert_partida(partida):
    bd = get_db()
    cursor = bd.cursor()
    statement = 'INSERT INTO partida (ronda) VALUES(:ronda)'
    cursor.executemany(statement, partida)
    bd.commit()


def max_id_partida():
    bd = get_db()
    cursor = bd.cursor()
    statement = 'SELECT MAX(id) FROM partida;'
    cursor.execute(statement)
    row = cursor.fetchone()
    bd.commit()
    return row[0]



def insert_jugador(jugador):
    bd = get_db()
    cursor = bd.cursor()
    statement = 'INSERT INTO jugador(nombre, dinero, partida_FK) VALUES(:nombre, :dinero, :partida_FK)'
    cursor.executemany(statement, jugador)
    bd.commit()


def max_id_jugador():
    bd = get_db()
    cursor = bd.cursor()
    statement = 'SELECT MAX(id) FROM jugador;'
    cursor.execute(statement)
    row = cursor.fetchone()
    bd.commit()
    return row[0]

