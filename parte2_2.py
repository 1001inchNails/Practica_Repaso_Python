'''
6. Manejo de Archivos:
o Crea un archivo de texto llamado empleados.txt y escribe en él los nombres de los empleados de la lista empleados.
o Lee el archivo empleados.txt e imprime su contenido.
o Lee un archivo CSV que contenga datos de productos (nombre, precio, cantidad) y crea una lista de objetos Producto a partir de esos datos.
'''

import csv
from parte2_1 import Producto

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

reader = csv.reader (csvFile)

tamanhoCSV = sum(1 for row in reader)

listaProductos = []

with open("productos.csv", 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for i in range (1, tamanhoCSV): # empezando con 1 nos saltamos el header ([0])
            nombre = rows[i][0]
            precio = float(rows[i][1])
            cantidad = int(rows[i][2])
            listaProductos.append(Producto(nombre,precio,cantidad))

for item in listaProductos:
     print(item)

listaProductos[0].aumentarCantidad(320)
print("\nCantidad producto01: ",listaProductos[0].mostrarCantidad())