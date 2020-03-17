peso = input("Ingrese su peso: ")
peso = float(peso)
altura = input("Ingrese su altura: ")
altura = float(altura)

imc = peso / (altura*altura)
print("Su peso es: ",peso,", y su altura es ",altura)
print("Su Indice de Masa Corporal es: ",imc)

if(imc<18.5):
    print("Peso insuficiente")
elif(imc>=18.5 and imc<25):
    print("Peso Normal")
elif(imc>=25 and imc<27):
    print("Sobrepeso grado 1")
elif(imc>=27 and imc<30):
    print("Sobrepeso grado 2")
elif(imc>=30 and imc<35):
    print("Obesidad tipo 1")
elif(imc>=35 and imc<40):
    print("Obesidad tipo 2")
elif(imc>=40 and imc<50):
    print("Obesidad tipo 3 Morbida")
elif(imc>=50):
    print("Obesidad tipo 4 Extrema")
