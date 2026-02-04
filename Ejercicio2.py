import mysql.connector

class Pokemon:
    def __init__(self, nombre, id, peso, altura, tipo):
        self.nombre = nombre
        self.id = id
        self.peso = peso
        self.altura = altura
        self.tipo = tipo

    def mostrar(self):
        print(f"{self.nombre} #{self.id}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}m")
        print(f"Tipos: {self.tipo}\n")

def pokemonsEntre(num1, num2):
    max=151
    min=1
    if num1<min:
        for i in range(min-num1):
            print(f"El pokemon con codigo {i-min} no existe en la base de datos")
    print()
    try:
        db = mysql.connector.connect(user="daw2", password="LaElipa", host="localhost", database="dwes3")
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM pokemon WHERE numero_pokedex>={num1} and numero_pokedex<={num2}")
        for fila in cursor.fetchall():
            valores = list(fila)
            tipo = []
            cursor.execute(f"SELECT tipo.nombre from tipo, pokemon_tipo WHERE pokemon_tipo.numero_pokedex={valores[0]} AND pokemon_tipo.id_tipo=tipo.id_tipo")
            for (fila,) in cursor.fetchall():
                tipo.append(fila)
            poke=Pokemon(valores[1],valores[0],valores[2],valores[3]," ,".join(tipo))
            poke.mostrar()
        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        print(err)
    if num2>max:
        for i in range(num2-max):
            print(f"El pokemon con codigo {max+i+1} no existe en la base de datos")
    print()


pokemonsEntre(num1=1, num2=151)