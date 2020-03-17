import time #Importamos la biblioteca Time
i = 1
while i <= 10:
    print(i)
    i = i+1 #No se puede poner i++ en python :(
    time.sleep(1) #Genera retardo (1 segundo)
    
while True:
    f = input("Desea continuar? si/no")
    if(f=="no"):
        break