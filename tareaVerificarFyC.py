m=[ [100,250,450],[230,600,500]]

while True:
    fil = input("Ingrese fila: ")
    col = input("Ingrese columna: ")

    fil = int(fil)
    col = int (col)
    
    tF = len(m)-1
    for f in m:
        tC = (len(f)-1)
    
    print(tF)
    print(tC)    
    if(fil>tF or col>tC):
        print("La posicion ingresada es incorrecta, ingrese nuevamente!") 
    else:
        print("El numero dentro de esa posicion es: ",m[fil][col])
        break
        