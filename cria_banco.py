import _sqlite3

connection = _sqlite3.connect('banco.db')
cursor = connection.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
 nome text, estrelas real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES ('alpha', 'alpha hotel', 4.3, 600.50, 'Blumenau')"

seleciona_hoteis = "SELECT * FROM hoteis"

cursor.execute(criar_tabela)
cursor.execute(cria_hotel)
cursor.execute(seleciona_hoteis)

connection.commit()
connection.close()
