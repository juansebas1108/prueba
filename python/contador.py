#Bucle controlado por un contador que suma determinado conjunto de reales

contador=int(input("Diga cuantos numeros reales quiere sumar: "))

suma = 0.0
while contador > 0:
    valor=float(input("Dame un valor real: "))
    suma += valor
    contador = contador - 1

print("La suma de los numeros es: ", suma)    