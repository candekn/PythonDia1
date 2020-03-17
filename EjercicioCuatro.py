num = input("Ingrese un año: ")
num = int(num)
if(num%400==0 or (num%4==0 and num%100!=0)):
    print("Es año bisiesto")
else:
    print("No es bisiesto")

