# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:43:37 2022

@author: LGT-5
"""
print ("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")
p1=input("Primera Interacción, ingrese un valor cualquiera: ")
print("Este tipo de dato en Python es:")
print (type(p1))
#No podemos utilizar un isinstance porque da error cuando hacemos el type casting de Int() si no es un entero y de igual manera con otros tipos de datos
#if(isinstance(int(p1),int)):
#    print("Es un entero")
#if(isinstance(p1,float)):
#    print("Es un decimal")
#if(isinstance(p1,str)):
#    print("Es un String")
p2=input("Segunda Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:")
print (type(p2))

p3=input("Tercera Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:")
print (type(p3))

p4=input("Cuarta Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:")
print (type(p4))

p5=input("Quinta Interacción, ingrese un valor cualquiera:")
print("Este tipo de dato en Python es:")
print (type(p5))

print("¡YA NO SE HARÁN MÁS INTERACCIONES!")

