"""3. Haz un programa que pida por teclado el nombre, el peso y la altura e introduzca un nuevo
pokemon en la pokedex. El código debería de ser consecutivo al último que haya en la base de
datos."""

import mysql.connector

try:
    db = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes3")
    cursor = db.cursor()

    nombre = input("Nombre: ")
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))

    # Obtener el mayor número de pokédex
    cursor.execute("SELECT MAX(numero_pokedex) FROM pokemon")
    max_codigo = cursor.fetchone()[0]
    nuevo_codigo = max_codigo + 1

    # Insertar el nuevo Pokémon
    sql = f"INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES ({nuevo_codigo}, {nombre}, {peso}, {altura})"
    cursor.execute(sql)
    conn.commit()

    print("Pokémon insertado con código:", nuevo_codigo)

    cursor.close()
    db.close()
except mysql.connector.Error as err:
    print(err)