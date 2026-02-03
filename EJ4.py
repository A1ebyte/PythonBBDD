""""""

import mysql.connector

try:
    db = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes3")
    cursor = db.cursor()

    codigo = int(input("Código del Pokémon a eliminar: "))
    sql=f"DELETE FROM pokemon WHERE numero_pokedex = {codigo}"
    cursor.execute(sql)
    db.commit()

    if cursor.rowcount > 0:
        print("Pokémon eliminado correctamente")
    else:
        print("No existe ningún Pokémon con ese código")

    cursor.close()
    db.close()
except mysql.connector.Error as err:
    print(err)