#Bucle para garantizar que el mes elegido es correcto

#Ejercicio

mes = int(input("Introduzca el mes del año emtre el 1 y 12 "))

while mes >12 or mes <1:
    print("Mes introducido incorrecto. Intentelo de Nuevo ")
    mes = int(input("Introduzca el mes del año entre 1 y 12: "))

print(f'El mes {mes} es valido')