# importar connexio del fitxer connection.py
from connection import *

#CRUpdateD
def update(name,surname,age,email):
    update_query = '''
                    UPDATE USERS
                    SET user_name =  %s, user_surname = %s, user_age = %s, user_email= %s
                    WHERE user_id = ;
    '''
    connection.execute(update_query, (name,surname,age,email))

    conn.commit()


def update_demo():
    update_query = '''
                    UPDATE USERS
                    SET user_name = 'updatedd', user_surname = 'asd', user_age = 11, user_email= 'as@as.cv'
                    WHERE user_id = 1;
    '''
    connection.execute(update_query)

    conn.commit()

    print("Usuario modificado")

#update_demo()