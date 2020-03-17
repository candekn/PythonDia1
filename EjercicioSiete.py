#lista vacia:
notas = [] 
i = 0
suma = 0
contador = 0
promedio = 0
while True:
    nota = input("Ingrese nota: ")
    nota = int(nota)
    notas.append(nota)
    contador = contador + 1
    if contador==3:
        break
    
while i < len(notas):
    suma= suma+notas[i]
    i = i+1

promedio = suma / len(notas)

print("Las notas ingresadas son: ", notas)
print("Su promedio es: ", promedio)