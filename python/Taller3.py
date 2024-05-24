mayor=0
menor=99999
for x in range(1,3,1):
    numero= int(input("ingrese un numero: "))
    if (numero > mayor):
        mayor=numero
    if (numero < menor):
        menor=numero          
print("el numero mayor es: ",mayor)
print("el numero menor es: ",menor)