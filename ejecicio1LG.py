# -*- coding: utf-8 -*-
"""
Spyder Editor


This is a temporary script file.
"""

print("Realizado por: Leandro García")

print("Consultando los tipos de valores:")
print("El tipo de dato de 875 es:")
#validamos el dato con la función type que devuelve el tipo de dato
print (type(875))

print("El tipo de dato de 4.89 es:")
print (type(4.89))

print("El tipo de dato de del texto: Now is better than never. es:")
print (type('Now is better than never.'))

print("El tipo de dato de 1.32 es:")
print (type(1.32))

print("¿El valor 5 + 8i corresponde a un valor entero?")
#validamos el dato con la función isinstance que nos devuelve el true o false
print (isinstance(5 + 8j,int))

print("¿El valor 8.2 corresponde a un valor entero?")
print (isinstance(8.2,int))

print("¿El texto : Readability counts. corresponde a un string?")
print (isinstance("Readability counts.",str))


