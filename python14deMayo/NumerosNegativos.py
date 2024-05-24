contador=0

n=int(input("Ingrese cuantos numeros quiere introducir: "))

for i in range (n):
    numero=int(input("Ingrese el numero "))
    if numero < 0:
        contador=contador+1

print("Usted ha introducido ",contador," Numeros negativos")