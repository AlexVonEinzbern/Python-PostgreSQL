import psycopg2
from pprint import pprint

class DataBaseConnection:

	def __init__(self):
		
		#Hacemos la conexion de nuestro programa de python con la base de datos.
		#Usamos un try y except en caso de que el programa por algun motivo no se pudo conectar a nuestra base de datos.
		try:
			self.connection = psycopg2.connect("dbname=empresa user=empresa password=123456789 host=localhost")
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()
		except:
			pprint('No se puede conectar con la base de datos.')
	

	#Vamos a crear una tabla llamada "productos" en la base de datos "empresa"
	#La tabla "productos" tendra como valores a id (llave primaria), nombre (string) y valor (decimal)

	def create_table(self):
		create_table_command = "CREATE TABLE productos(id integer NOT NULL PRIMARY KEY, nombre varchar(100), valor DECIMAL)"
		self.cursor.execute(create_table_command)


	#Vamos a ingresar un valor a la tabla "productos"
	
	def insert_new_record(self):
		new_record = ("1234567","Freno","1637237")
		insert_command = "INSERT INTO productos(id, nombre, valor) VALUES('"+ new_record[0] + "','" + new_record[1] + "','" + new_record[2] + "')"
		pprint(insert_command)
		self.cursor.execute(insert_commnad)

	#Vamos a hacer una consulta de toda la tabla.

	def query_all(self):
		self.cursor.execute("SELECT * FROM productos")
		row = self.cursor.fetchall()
		for i in row:
			pprint("Cada producto : {0}".format(i))

if  __name__ == '__main__':
	
	#Creamos el objeto database_connection.
	database_connection = DataBaseConnection()

	#Usamos el objeto database_connection para crear la tabla.
	database_connection.create_table()

	#Usamos el objeto database_connection para añadir un valor a la tabla.
	#database_connection.insert_new_record()
		
	#Usamos el objeto database_connection para hacer una consulta a toda la tabla.
	#database_connection.query_all()
