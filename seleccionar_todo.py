import psycopg2

# Conexión a la base de datos
conexion = psycopg2.connect(user='postgres',
                            password='admin', 
                            host='127.0.0.1',
                            port='5432',
                            database='db_personas')

#Utilizar cursor
cursor=conexion.cursor()

#crear la sentencia sql
sql='SELECT * FROM personas'

#uso del metodo execute
cursor.execute(sql)

#mostrar el resultado
registro=cursor.fetchall()

#mostrar añ usuario
for fila in registro:
    print(fila)

#cerrar conexiones
cursor.close()
conexion.close()