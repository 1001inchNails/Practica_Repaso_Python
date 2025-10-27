'''
6. Manejo de Archivos:
o Crea un archivo de texto llamado empleados.txt y escribe en él los nombres de los empleados de la lista empleados.
o Lee el archivo empleados.txt e imprime su contenido.
o Lee un archivo CSV que contenga datos de productos (nombre, precio, cantidad) y crea una lista de objetos Producto a partir de esos datos.
'''

import csv
from io import StringIO

class Producto (object):
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

empleados = ["Ana", "Carlos", "Maria", "Luis"]

try:
    file = open ("empleados.txt", "x")
    with open ("empleados.txt", "a") as ffile:
        for empleado in empleados:
            ffile.write (empleado + "\n")
except:
    print ("El archivo ya existe\n")

file = open ("empleados.txt")
print (file.read())



csvFile = open ("productos.csv")
reader = csv.DictReader (csvFile)

columnNames = reader.fieldnames

reader = csv.reader (csvFile)
tamanhoCSV = sum(1 for row in reader)

for i in range (1, tamanhoCSV):
    nombreClase = "producto" + i

csvr = csv.reader(csvFile)
csvr = list(csvr)
print (csvr)  