# importar connexio del fitxer connection.py
from connection import *

def crear_tabla():
    # evitar error por duplicaciones de tabla
    sql = '''CREATE TABLE IF NOT EXISTS USERS(
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(255) NOT NULL,
                    user_surname VARCHAR(255) NOT NULL,
                    user_age BIGINT NOT NULL,
                    user_email VARCHAR(255) NOT NULL

    )'''

    print(sql)

    # execute() envia la query
    connection.execute(sql)
    print(connection)

    #commit de la query
    conn.commit()

    #cerrar todo
    #connection.close()
    #conn.close()
#crear_tabla()