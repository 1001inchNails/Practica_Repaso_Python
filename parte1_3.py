'''
3. Funciones:
o Define una función llamada calcular_iva que tome como parámetro el precio de un producto y devuelva el precio con el IVA (21%) incluido.
o Llama a la función con un precio de 100 y muestra el resultado.
'''

def calcular_iva (precio):
    precioConIva = precio + ((precio*21)/100)
    return precioConIva

print(calcular_iva(100))