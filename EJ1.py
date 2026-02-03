"""1. Haz un programa que liste por consola los nombres (sólo los nombres) de todos los
pokemons de mas de 1.5 de altura"""
import mysql.connector

try:
    db = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes3")
    cursor = db.cursor()
    cursor.execute("SELECT nombre FROM pokemon WHERE altura > 1.5")

    for (nombre,) in cursor.fetchall():
        print(nombre)

    """
    pokemons = [nombre for nombre in cursor.fetchall()]
    print(*pokemons, sep="\n")
    """

    cursor.close()
    db.close()
except mysql.connector.Error as err:
    print(err)