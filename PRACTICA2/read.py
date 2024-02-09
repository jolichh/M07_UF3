# importar connexio del fitxer connection.py
from connection import *

# CReadUD

# busca un user especifico por el id
def get_user(user_id):
    
    select_query = "SELECT * FROM USERS WHERE user_id = %s;"

    connection.execute(select_query, (user_id))
    users = connection.fetchall()

    print("DATOS DEL USER:")
    for user in users:
        print(user)


def get_all():
    select_query = "SELECT * FROM USERS;"

    connection.execute(select_query)
    users = connection.fetchall()

    print("DATOS DE LA TABLA USERS:")
    for user in users:
        print(user)


#prueba 
get_all()