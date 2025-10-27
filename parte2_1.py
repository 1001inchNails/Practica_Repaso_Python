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
    
    def aumentarCantidad (self, cantidad):
        self.cantidad = self.cantidad + cantidad
        
    def disminuirCantidad (self, cantidad):
        self.cantidad = self.cantidad - cantidad
    
    def mostrarCantidad (self):
        return self.cantidad
        
producto1 = Producto ("producto 01", 100, 1000)
print(producto1.calcular_total())

producto2 = Producto ("producto 02", 100, 1000)
producto2.aumentarCantidad(200)
print(producto2.mostrarCantidad())

producto3 = Producto ("producto 03", 100, 1000)
producto3.disminuirCantidad(200)
print(producto3.mostrarCantidad())