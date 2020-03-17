notas = [10,60,50,20]
#En python, los for funcionan como los foreach de otros lenguajes. 
#No existe un for 'normal'
suma = 0
for aux in notas:
    print(aux)
    suma = suma + aux
    
promedio = suma / len(notas)
print("El promedio es: ",promedio)

#Matrices: Son una lista de listas

m = [[10,20,30],[40,50,60],[100,500,200]]
print(m)

alumnos = [["Alan",10,2,8],["Blanca",9,10,10],["Pepe",9,7,5]]
for a in alumnos:
    print(a[0])
    
notas = [[10,2,8],[9,10,10],[9,7,5]]
for filas in notas:
    sumaNota = 0
    for colum in filas:
        sumaNota = sumaNota+colum
    prom = sumaNota/3
    print(prom)
        
        
        