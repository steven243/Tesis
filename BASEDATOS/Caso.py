from CONEXION.BDCone import BDCone

class Caso():
	def __init__(self, con):
		''' Campos de la tabla '''
		self.nombreTabla = 'casos'
		self.id = 0 
		self.nombre = ''
		self.apPaterno = ''
		self.apMaterno = ''
		self.telefono = ''
		self.ortodoncista = ''
		self.casoActual = ''
		self.rutaImagen = ''
		self.db = BDCone(con) # instanciamos la conexion
	
	def leer(self, columna):
		query = 'SELECT '+columna+' FROM '+self.nombreTabla+' ORDER BY '+columna+' ASC'
		return self.db.ejecutar(query)

	def obtenerId(self, nombre):
		query = 'SELECT id FROM '+self.nombreTabla+' WHERE nombre="'+nombre+'"'
		return self.db.ejecutar(query)