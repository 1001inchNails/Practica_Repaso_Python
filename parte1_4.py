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