import psycopg2

try:
    # Conexión a la base de datos
    conexion = psycopg2.connect(user='postgres',
                                password='admin', 
                                host='127.0.0.1',
                                port='5432',
                                database='db_personas')

    # Utilizar cursor
    cursor = conexion.cursor()

    # Crear la sentencia SQL
    sql = 'SELECT * FROM personas WHERE id=%s'

    # Solicitar datos al usuario
    idpersona = input('Ingrese el id del registro a mostrar: ')

    # Uso del metodo execute
    cursor.execute(sql, (idpersona,))  # Se pasa el ID como una tupla

    # Mostrar resultado
    registro = cursor.fetchone()

    # Mostrar en consola al usuario
    print(registro)

except psycopg2.Error as error:
    print("Error al trabajar con la base de datos:", error)

finally:
    # Cerrar conexiones
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conexion' in locals() and conexion is not None:
        conexion.close()
