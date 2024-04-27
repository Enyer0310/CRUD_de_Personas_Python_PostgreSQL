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

    # Crear tabla personas si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        apellido VARCHAR(100),
        edad INT
    )
    """)
    #Creamos sentencia sql
    sql='INSERT INTO personas (nombre,apellido,edad) VALUES(%s,%s,%s)'

    #Creamos inputs para solicitud de usuario
    nombre=input('Ingresar Nombre: ')
    apellido=input('Ingresar Apellido: ')
    edad=input('Ingresar Edad: ')

    #Recoleccion de datos
    datos=(nombre,apellido,edad)

    #Hacer uso del metodo execute
    cursor.execute(sql,datos)

    # Confirmar la transacción para guardar registro
    conexion.commit()


    #Registro insertados
    registros=cursor.rowcount

    #Mostrar un mensaje
    print(f'Registro insertado correctamente: {registros}')

    # Realizar la consulta
    cursor.execute("SELECT * FROM personas")

    # Obtener los registros
    registros = cursor.fetchall()
    
except psycopg2.Error as error:
    print("Error al trabajar con la base de datos:", error)

finally:
    # Cerrar cursor y conexión
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conexion' in locals() and conexion is not None:
        conexion.close()
