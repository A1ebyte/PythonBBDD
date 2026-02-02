"""2. Haz un programa que cambie a mayúsculas (por ejemplo SNORLAX en lugar de Snorlax) los
nombres de todos los pokemon de mas de 200 de peso. Informa por pantalla el número de
registros modificados"""

import mysql.connector

try:
    db = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes3")
    cursor = db.cursor()
    cursor.execute("UPDATE pokemon SET nombre = UPPER(nombre) WHERE peso > 200")
    conn.commit()
    print("Registros modificados:", cursor.rowcount)

    """
    cursor.execute("SELECT numero_pokedex, nombre FROM pokemon WHERE peso > 200")
    for codigo, nombre in cursor.fetchall():
        cursor.execute(f"UPDATE pokemon SET nombre = {nombre.upper()} WHERE numero_pokedex = {codigo}")
    conn.commit()
    """

    cursor.close()
    db.close()
except mysql.connector.Error as err:
    print(err)