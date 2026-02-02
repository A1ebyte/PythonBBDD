import mysql.connector

# Algunos ejemplos extras de acceso a bases de datos desde python
# Usamos la base de datos pokemondb
# Por claridad, cada ejemplo está en un bloque try/excep diferente

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    sql = "SELECT nombre, peso, altura FROM pokemon WHERE peso > 200"
    cursor.execute(sql)

    for fila in cursor:
        print(fila)

    sql = "UPDATE pokemon SET peso=350 WHERE peso > 250"
    cursor.execute(sql)
    # el metodo rowcount nos devuelve, en updates y deletes, el número de filas involucradas
    # en select no lo hace con 'nonbuffered' cursors que son los que estamos viendo
    # existe la opción de usar buffered cursors, pero no los vamos a ver
    print("La instrucción involucra a", cursor.rowcount, "filas de la base de datos")
    # recuerda que si no ejecutamos un commit no se guardan los cambios
    # en este ejemplo está comentado y no se guardan
    #connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    # Podemos parametrizar el select igual que con los statement de JDBC
    sql = "SELECT nombre, peso, altura FROM pokemon WHERE peso > %s AND nombre = %s"
    datos = (250,'Snorlax')
    # cada elemento de la tupla datos se sustituye en orden por el %s del query
    cursor.execute(sql, datos)

    for fila in cursor:
        print(fila)

    # También podemos lanzar múltiples querys (no válido con SELECT)
    sql = "INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES (%s, %s, %s, %s)"
    datos = [(200, 'Pepe Potamo', 50, 30), (201, 'Inés Perado', 33, 600), (202,'Benito Camelas', 412, 30)]
    # En este caso, cada tupla se corresponde con un query diferente
    # Fíjate que usamos executemany y no execute
    cursor.executemany(sql, datos)
    print("La instrucción involucra a", cursor.rowcount, "filas de la base de datos")

    cursor.execute("SELECT * FROM pokemon WHERE numero_pokedex >=200")
    for fila in cursor:
        print(fila)

    # tampoco guardamos los cambios, que no queremos cargarnos una base de datos tan bonita :-)
    #connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()
    # Activamos la posibilidad de ver los warnings
    # En este ejemplo no provocamos ninguno, así que al final no veremos nada...
    cursor.get_warnings = True

    sql = "SELECT numero_pokedex, nombre FROM pokemon where numero_pokedex <=10"
    cursor.execute(sql)
    # Con fetchmany podemos indicar cuantas filas leer
    dosFilas = cursor.fetchmany(size=2)
    # y luego leer las restantes a partir de donde nos hemos quedado
    restantes = cursor.fetchall()
    print(dosFilas)
    print(restantes)

    # volvemos a ejecutar la query
    cursor.execute(sql)
    # y ahora vamos a ver otra funcion de leer una a una las filas de la query
    fila = cursor.fetchone()
    # fetchone sería igual que fila =cursor.fetchmany(size=1)
    # y luego iteramos con un bucle
    while fila is not None:
        print(fila)
        fila = cursor.fetchone()

    # si hubiera warnings los veríamos aquí
    print(cursor._warnings)

    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)