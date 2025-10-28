import csv # para parte6

def parte1 ():
    '''
    1. Variables y Tipos de Datos:
    o Crea una variable llamada nombre_empresa y asígnale el valor "TechSolutions".
    o Crea una variable llamada año_fundacion y asígnale el valor 2010.
    o Imprime el tipo de dato de ambas variables.
    '''

    nombre_empresa = "TechSolutions"
    anho_fundacion = 2010

    print(type(nombre_empresa))
    print(type(anho_fundacion))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def parte2 ():
    '''
    2. Estructuras de Control:
    o Escribe un programa que pida al usuario ingresar un número y determine si es positivo, negativo o cero.
    o Crea un bucle for que imprima los números del 1 al 10.
    '''
    try:
        opcion = float(input("Introduzca un numero\n>")) # input es string por defecto, convertimos a float directamente
        if opcion == 0:
            print("Igual a cero")
        elif opcion > 0:
            print("Positivo")
        else:
            print("Negativo")

    except TypeError as e:  # por si nos escapa un valor no numerico en el input
        print(e)
        
    for i in range (10):
        print(i+1, end = " ") # para printear en la misma linea con separacion " "

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def parte3 ():
    '''
    3. Funciones:
    o Define una función llamada calcular_iva que tome como parámetro el precio de un producto y devuelva el precio con el IVA (21%) incluido.
    o Llama a la función con un precio de 100 y muestra el resultado.
    '''

    def calcular_iva (precio):
        precioConIva = precio + ((precio*21)/100)
        return precioConIva

    print(calcular_iva(100))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def parte4 ():
    '''
    4. Listas y Diccionarios:
    o Crea una lista llamada empleados con los nombres "Ana", "Carlos", "María" y "Luis".
    o Añade un nuevo empleado llamado "Pedro" a la lista.
    o Crea un diccionario llamado info_empleado con las claves nombre, edad y departamento, y asígnales valores correspondientes.
    o Imprime el valor asociado a la clave departamento.
    '''
    empleados = ["Ana", "Carlos", "Maria", "Luis"]
    empleados.append("Pedro")
    print(empleados)

    info_empleado = {"nombre": "Ana", "edad": 50, "departamento": "IT"}
    print(info_empleado.get("departamento"))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def parte5 (ejecutarEjemplos):
    '''
    5. Programación Orientada a Objetos:
    o Define una clase llamada Producto con los atributos nombre, precio y cantidad.
    o Crea un método llamado calcular_total que devuelva el precio total del producto (precio * cantidad).
    o Crea métodos para aumentar/disminuir la cantidad.

    o Crea una instancia de la clase Producto y llama al método calcular_total.
    o Crea una instancia de la clase Producto y llama al método aumentar_cantidad.
    o Crea una instancia de la clase Producto y llama al método disminuir_cantidad.
    '''

    class Producto (object):
        
        def __init__(self, nombre, precio, cantidad):
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
        
        def calcular_total (self):
            total = self.precio * self.cantidad
            return total
        
        def __str__(self): # para poder printear los objetos
            return f"Nombre: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}"
        
        def aumentarCantidad (self, cantidad):
            self.cantidad = self.cantidad + cantidad
            
        def disminuirCantidad (self, cantidad):
            self.cantidad = self.cantidad - cantidad
        
        def mostrarCantidad (self):
            return self.cantidad

    if ejecutarEjemplos == True: # si le mandamos True ejecuta el codigo del ejercicio, en caso contrario retorna la clase, la cual usamos en la parte 6
                                 # de esta manera no ejecuta todo el codigo al meter Producto en una variable
        producto1 = Producto ("producto 01", 100, 1000)
        print(producto1.calcular_total())

        producto2 = Producto ("producto 02", 100, 1000)
        producto2.aumentarCantidad(200)
        print(producto2.mostrarCantidad())

        producto3 = Producto ("producto 03", 100, 1000)
        producto3.disminuirCantidad(200)
        print(producto3.mostrarCantidad())
    else:
        return Producto

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def parte6 ():
    '''
    6. Manejo de Archivos:
    o Crea un archivo de texto llamado empleados.txt y escribe en él los nombres de los empleados de la lista empleados.
    o Lee el archivo empleados.txt e imprime su contenido.
    o Lee un archivo CSV que contenga datos de productos (nombre, precio, cantidad) y crea una lista de objetos Producto a partir de esos datos.
    '''

    Producto = parte5(False) # pues lo dicho, metiendolo con false cojemos la clase sin ejecutar el resto del codigo

    empleados = ["Ana", "Carlos", "Maria", "Luis"]

    try:
        file = open ("empleados.txt", "x") # crea archivo
        with open ("empleados.txt", "a") as ffile:  # mete empleados en lista
            for empleado in empleados:
                ffile.write (empleado + "\n")
    except:
        print ("El archivo ya existe\n")

    file = open ("empleados.txt")
    print (file.read()) # abre e printea archivo completo

    listaProductos = []

    with open("productos.csv", 'r') as file:    # abrimos en modo lectura
            reader = csv.reader(file)           # preparamos reader 
            filas = list(reader)                # creamos lista con todas las filas en el reader
            tamanho = len(filas)                # numero total de filas
            for i in range (1, tamanho):        # empezando con 1 nos saltamos el header ([0])
                nombre = filas[i][0]            # [i] es la fila, y [0] [1] [2] son el nombre, precio y cantidad respectivamente
                precio = float(filas[i][1])
                cantidad = int(filas[i][2])
                listaProductos.append(Producto(nombre,precio,cantidad)) # metemos cada producto en la lista
                
    # muestras
    for item in listaProductos:
        print(item)

    listaProductos[0].aumentarCantidad(320)
    print("\nCantidad producto01: ",listaProductos[0].mostrarCantidad())

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Tests
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#parte1()
#parte2()
#parte3()
#parte4()
#parte5(True)
#parte6()