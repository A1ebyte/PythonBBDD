import mysql.connector

try:
    #nos conectamos
    db = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes3")
    cursor = db.cursor()

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
    #endregion

    #region UPDATE
    cursor.execute("UPDATE pokemon SET nombre='MOHAMED' WHERE nombre='Mew'")
    print(cursor.rowcount, "filas afectadas")
    cursor.execute("SELECT * FROM pokemon")

    #para hacer el cambio hay que hacer esto
    db.commit()

    print(cursor.fetchall()[-1])
    #endregion

    #region DELETE

    #endregion

    #region INSERT

    #endregion

    #nos desconectamos
    cursor.close()
    db.close()
except mysql.connector.Error as err:
    print(err)