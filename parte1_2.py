'''
2. Estructuras de Control:
o Escribe un programa que pida al usuario ingresar un número y determine si es positivo, negativo o cero.
o Crea un bucle for que imprima los números del 1 al 10.
'''
try:
    opcion = float(input("Introduzca un numero\n>"))
    if opcion == 0:
        print("Igual a cero")
    elif opcion > 0:
        print("Positivo")
    else:
        print("Negativo")
except TypeError as e:
    print(e)
    
for i in range (10):
    print(i+1, end = " ")