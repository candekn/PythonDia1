m = []
filas = input("Ingrese filas: ")
columnas = input("Ingrese columnas: ")

filas = int(filas)
columnas=int(columnas)

for i in range(filas):
    m.append([]) #Por cada fila, agrega una lista vacia '[]'
    for j in range(columnas):
        print("Fila: ",i, "Columna: ",j)
        dato = input("Ingrese dato: ")
        dato = int(dato)
        m[i].append(dato) 
        
for n in m:
    print(n)
        