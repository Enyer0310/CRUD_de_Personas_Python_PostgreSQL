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

    # Utilizar sentencia SQL
    sql = 'DELETE FROM personas WHERE id=%s'

    # Solicitar dato al usuario
    idpersona = input('Ingrese el ID del registro a eliminar: ')

    # Utilizar el metodo execute
    cursor.execute(sql, (idpersona,))

    # Guardar cambios
    conexion.commit()

    # Conteo de registros eliminados
    registro_eliminado = cursor.rowcount

    # Mensaje al usuario
    print(f'Registros eliminados: {registro_eliminado}')

except psycopg2.Error as error:
    print("Error al trabajar con la base de datos:", error)

finally:
    # Cerrar conexiones
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conexion' in locals() and conexion is not None:
        conexion.close()
