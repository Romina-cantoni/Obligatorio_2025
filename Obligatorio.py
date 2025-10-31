import mysql.connector

def obligatorio(documento):
    conexion = mysql.connector.connect(
        user='root',
        password='rootpassword',
        host='127.0.0.1',
        database='Gestion_Salas_UCU',
        auth_plugin='mysql_native_password'
    )
    cursor = conexion.cursor()

    query = "select * from Gestion_Salas_UCU.facultad where nombre = '{}'".format(documento)
    print(query)
    cursor.execute(query)
    for (id_facultad, nombre) in cursor:
        print("id_facultad: {} - nombre: {}".format(id_facultad, nombre))

    cursor.close()
    conexion.close()

if __name__ == "__main__":
    obligatorio("Ingenieria")
