n1=int(input("Ingrese el primer numero entero: "))
n2=int(input("Ingrese el segundo numero entero: "))

print("Los numeros pares son: ")
for i in range(n1,n2 + 1):
    if i % 2 == 0:
        print(i)

print("Los numeros impares son: ")
for i in range(n1,n2 + 1):
    if i % 2==1:
        print(i)