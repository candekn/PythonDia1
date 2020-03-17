#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Holaaaaa")
edad = input("Ingrese edad: ")
print("Su edad es: ", edad)
edad = int(edad)
#En phython no se usan llaves, las acciones despues de 
#un condicional se hacen con identaciones (tab)
#RECORDAR LOS DOS PUNTOS : PARA "ABRIR" las acciones despues de la condicion

if edad>=18:
    print("Usted es mayor de edad")
elif(edad>=65):
    print("Usted es jubilado")
else:
    print("Usted es menor de edad")

print("Fin del programa")


    