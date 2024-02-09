# importar connexio del fitxer connection.py
from connection import *

#CRUpdateD
def update(user_id,name,surname,age,email):
    update_query = '''
                    UPDATE USERS
                    SET user_name =  %s, user_surname = %s, user_age = %s, user_email= %s
                    WHERE user_id = %s;
    '''
    connection.execute(update_query, (name,surname,age,email,user_id))

    conn.commit()


def update_demo():
    update_query = '''
                    UPDATE USERS
                    SET user_name = 'updaaateed', user_surname = 'asd', user_age = 11, user_email= 'as@as.cv'
                    WHERE user_id = 16;
    '''
    connection.execute(update_query)

    conn.commit()

    print("Usuario modificado")

update_demo()