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

    # crear sentencia sql
    sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'

    # Consulta de datos a usuario
    idpersona = input('Ingrese Id de la persona a editar: ')
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    edad = input('Ingrese edad: ')

    # recolección de datos
    datos = (nombre, apellido, edad, idpersona)

    # utilizar el metodo execute
    cursor.execute(sql, datos)

    # Guardar modificacion
    conexion.commit()

    # Contar el numero de actualizaciones
    actualizacion = cursor.rowcount

    # mostrar mensaje al usuario
    print(f'Registro actualizado: {actualizacion}')

except psycopg2.Error as error:
    print("Error al trabajar con la base de datos:", error)

finally:
    # Cerrar conexiones
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conexion' in locals() and conexion is not None:
        conexion.close()
