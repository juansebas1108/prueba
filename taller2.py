nummayor = 0
nummenor = 99999
for x in range(1,10,1):
    numero = int(input("ingrese un numero:"))
    if (numero > nummayor):
        nummayor = numero
        
    if (numero < nummenor):
        nummenor = numero
        
print("El numero mayor es: ", nummayor) 
print("El numero menor es: ", nummenor)
    
        