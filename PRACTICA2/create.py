# importar connexio del fitxer connection.py
from connection import *

# CreateRUD
def insert_user(name,surname,age,email):
    sql = '''
            INSERT INTO USERS (user_name, user_surname, user_age, user_email)
            VALUES (%s,%s,%s,%s)
    )'''
    connection.execute(sql, (name,surname,age,email))

    conn.commit()

# funcion demostrativa que no recibe parametros
def insert_demo():
    sql = '''
            INSERT INTO USERS (user_name, user_surname, user_age, user_email)
            VALUES ('demo1_name', 'Lopx', 23, 'jhon@doe.com')
            RETURNING user_id;
    '''
    connection.execute(sql)

    user_id = connection.fetchone()
    conn.commit()

    print("Usuari creat amb id:", user_id)

#insert_demo()