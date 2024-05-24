"""# Un bucle para garantizar que el mes introducido es correcto

#ejercicio
mes = int(input("Introduzca el mes del año (entre 1 y 12): "))

while mes > 12 or mes < 1:
    print("Mes introducido incorrecto. Inténtelo de nuevo.")
    mes = int(input("Introduzca el mes del año (entre 1 y 12):"))

print(f'El mes {mes} es válido.')

#ejercicio
# Un bucle para garantizar que el mes introducido es correcto. Versión alternativa (I).

mes = 0 # Inicializamos la variable con un valor que
        # hace que se evalúe a True la condición de control

while mes > 12 or mes < 1:
    mes = int(input("Introduzca el mes del año (entre 1 y 12):"))
    if mes > 12 or mes < 1:
        print("Mes introducido incorrecto. Inténtelo de nuevo")

print(f'El mes {mes} es válido.')


#ejercicio
# Bucle controlado por un contador que suma un determinado conjunto de reales. (Versión 1)

contador = int(input('Diga cuantos números reales quiere sumar: '))

suma = 0.0
while contador > 0:
    valor = float(input('Dame un valor real: '))
    suma += valor                                       # Equivalente a suma = suma + valor
    contador = contador - 1                             # Se podría usar: contador -= 1

print("La suma de los números introducidos es", suma)


#Ejercicio
# while con break o suspension
contador = 0
while contador < 10:
    contador += 1
    print(" el contador esta en ", contador)
    if contador == 5:
        break

        print("valor del contador es ", contador)

print("fin")

#ejercicio
# la instruccion continue
# con el siguiente print le digo al programa que se olvide ya del break
# el mismo programa y solo cambia break por continue
print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
contador = 0
while contador < 10:
    contador += 1
    print(" el contador esta en ", contador)
    if contador == 5:
        continue

        print("valor del contador es ", contador)

print("fin")


#ejercicio
#x = 5
#while x > 0:
#    x -=1
#    print(x)

# Salida: 4,3,2,1,0

#Hace lo mismo que el anterior


#ejercicio
x = 5
while x > 0: x-=1; print(x)

#ejercicio

# while - else

x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")


#ejercicio
x = 5
while True:
    x -= 1
    print(x) #4, 3, 2, 1, 0
    if x == 0:
        break
else:
    # El print no se ejecuta
    print("Fin del bucle")


# ejercicio
# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0


#Ejercicio

i, j, k = 0, 0, 0
while i < 3:
    while j < 3:
        while k < 3:
            print(i,j,k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0"""

