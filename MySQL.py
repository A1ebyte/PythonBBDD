import mysql.connector

try:
    #nos conectamos, si database no existe da error
    db = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes3")
    cursor = db.cursor()

    #region DataBase
    #Para crear una Base de Datos
    #cursor.execute("CREATE DATABASE mydatabase")

    #Para confirmar que exista la BBDD
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)

    #Para crear Tablas
    #cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    #deben tener primaryKey
    #cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    #para confirmar que exiten las tablas
    cursor.execute("SHOW TABLES")

    for x in cursor:
        print(x)

    #para alterar Tablas
    #cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    #endregion

    #region SELECT
    #hacer un query SELECT 1
    cursor.execute("SELECT * FROM pokemon")
    for fila in cursor:
        print(", ".join(str(n) for n in fila))

    print("-"*40)

    #hacer un query SELECT 2
    cursor.execute("SELECT * FROM pokemon")
    resultados = cursor.fetchall()
    print("\n".join(str(n) for n in resultados))

    print("-"*40)

    #hacer un query SELECT 3
    cursor.execute("SELECT nombre, numero_pokedex FROM pokemon")
    for (pokemon, ID) in cursor:
        print(ID, pokemon, sep=" | ")
    print("-" * 40)
    #endregion

    #region UPDATE
    cursor.execute("UPDATE pokemon SET nombre='MOHAMED' WHERE nombre='Mew'")
    print(cursor.rowcount, "filas afectadas")
    cursor.execute("SELECT * FROM pokemon")

    #para hacer el cambio hay que hacer esto
    db.commit()
    print("-" * 40)
    print(cursor.fetchall()[-1])
    print("-" * 40)
    #endregion

    #region DELETE
    cursor.execute("DELETE FROM pokemon WHERE nombre='MOHAMED'")
    mydb.commit()
    print(cursor.rowcount, "filas borradas")
    print("-" * 40)

    #endregion

    #region INSERT
    cursor.execute("INSERT INTO pokemon (name, numero_pokedex) VALUES ('Mohamed', 001))")
    print(cursor.rowcount, "filas afectadas")
    print("-" * 40)
    cursor.execute("SELECT * FROM pokemon")

    # para hacer el cambio hay que hacer esto
    db.commit()
    print("-" * 40)
    #endregion

    #Para limitar usar limit
    #mycursor.execute("SELECT * FROM customers LIMIT 5")
    #Para ordenar Order by
    #sql = "SELECT * FROM customers ORDER BY name"
    #para borrar la tabla
    #sql = "DROP TABLE customers"

    #nos desconectamos
    cursor.close()
    db.close()
except mysql.connector.Error as err:
    print(err)