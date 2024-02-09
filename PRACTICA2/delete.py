# importar connexio del fitxer connection.py
from connection import *

def delete_user(user_id):
    delete_query = "DELETE FROM USERS WHERE user_id = %s;"

    #pasarle la query junto a la variable del parametro
    connection.execute(delete_query, (user_id))

    conn.commit()

# funcion demostrativa sin recibir parametros
def delete_demo():
    delete_query = "DELETE FROM USERS WHERE user_id = 16;"
    #delete_query = "DELETE FROM USERS;"
    connection.execute(delete_query)

    conn.commit()

    print("Eliminado usuario con id: 16")
    
delete_demo()