# aqui executa tot el CRUD
import psycopg2
from connection import *
from create_table import *
from create import *
from read import *
from update import *
from delete import *

x = input("Quieres ver una demo de como funciona el CRUD en la tabla de User? (y/n) >>> ")

if x == 'y':
    try:
        #demos que funcionan de prueba, no necesitan parametros
        crear_tabla()
        insert_demo()
        get_all()
        update_demo()
        delete_demo()

    except (Exception, psycopg2.Error) as error:
        print("ERROR:", error)

    finally:
        connection.close()
        conn.close()

