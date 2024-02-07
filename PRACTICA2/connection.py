import psycopg2

# dades per a connectar-se a la bbdd
conn = psycopg2.connect(
    database="postgres",
    user="postgresuser",
    password="password",
    host="localhost",
    port="5432"
)

# cursor() es el metode que fa la prova de connexio
connection = conn.cursor()

print(connection)