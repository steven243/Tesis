import os

''' 
	clase : main.py
	ruta : <archivo principal>
'''
rutaArchivo = os.getcwd() + '/UTILERIAS/' # ruta de los archivos
nombreArchivoCrenciales = '1234.txt' # archivo de coneciones a la BD

pacienteBD = 'paciente'
ortodoncistaBD = 'ortodoncista'
areaBD = 'area'

columna1_PA = 'id'
columna2_PA = 'nombre'
columna3_PA = 'apPaterno'
columna4_PA = 'apMaterno'
columna5_PA = 'area'
columna6_PA = 'telefono'

campos = 'QLineEdit {\
     border: 2px solid gray;\
     border-radius: 10px;\
     padding: 0 8px;\
     selection-background-color: darkgray;\
 }'

