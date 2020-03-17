#Tipos de colecciones: Listas, Tuplas y Dicionarios
lista = [10,40,50,100]
i = 0
suma = 0
while i < 4:
    print(lista[i])
    i = i+1
    


lista.append(1000)  #Agrega un nuevo obj al final de la lista

lista.insert(2,33) #Inserta un nuevo obj en el indice elegido 
#lista.insert(posicion, valor)

del(lista[0]) #elimina el elemento que se encuentra en esa posicion

lista[-1] #trae el ultimo elemento de la lista
#-2 ante ultimo
#-3 ante penultimo y asi sucesivamente...
len(lista) #permite saber la cantidad de elementos de la lista

j = 0
while j < len(lista)-1:
    suma = suma + lista[j]
    j = j+1
    
print(suma)